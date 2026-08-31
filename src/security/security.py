# ============================================================
# PHISHGUARD AI - SECURITY MODULE
# ============================================================

from urllib.parse import urlparse


def validate_url(url):
    """
    Validate a URL before analysis.
    """

    if not isinstance(url, str):
        return False, "URL must be a string."

    url = url.strip()

    if not url:
        return False, "URL cannot be empty."

    if len(url) > 2048:
        return False, "URL is too long."

    try:
        parsed = urlparse(url)
    except Exception:
        return False, "Invalid URL format."

    if parsed.scheme not in ("http", "https"):
        return False, "Only HTTP and HTTPS URLs are supported."

    if not parsed.netloc:
        return False, "URL does not contain a valid hostname."

    return True, "URL is structurally valid."


def security_check(url):
    """
    Perform basic security checks before ML analysis.
    """

    valid, message = validate_url(url)

    if not valid:
        return {
            "safe_to_analyze": False,
            "message": message
        }

    parsed = urlparse(url)

    hostname = parsed.hostname or ""

    if ".." in hostname:
        return {
            "safe_to_analyze": False,
            "message": "Hostname contains consecutive dots."
        }

    if hostname.startswith(".") or hostname.endswith("."):
        return {
            "safe_to_analyze": False,
            "message": "Hostname format is invalid."
        }

    return {
        "safe_to_analyze": True,
        "message": "URL passed security checks."
    }


def sanitize_url(url):
    """
    Remove unnecessary whitespace from a URL.
    """

    if not isinstance(url, str):
        raise ValueError("URL must be a string.")

    return url.strip()


def secure_analyze_url(url, analysis_function):
    """
    Validate and security-check a URL before
    sending it to the analysis function.
    """

    url = sanitize_url(url)

    security_result = security_check(url)

    if not security_result["safe_to_analyze"]:
        return {
            "success": False,
            "url": url,
            "message": security_result["message"]
        }

    try:
        result = analysis_function(url)

        return {
            "success": True,
            "url": url,
            "message": "Analysis completed successfully.",
            "analysis": result
        }

    except Exception as error:
        return {
            "success": False,
            "url": url,
            "message": f"Analysis failed safely. Reason: {error}"
        }


if __name__ == "__main__":

    test_url = "https://www.google.com"

    print("=" * 70)
    print("PHISHGUARD AI - SECURITY MODULE TEST")
    print("=" * 70)

    result = security_check(test_url)

    print("\nURL:")
    print(test_url)

    print("\nSecurity result:")
    print(result)

    print("\nSecurity module test completed successfully. ✅")