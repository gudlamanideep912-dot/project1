# ============================================================
# PHISHGUARD AI - URL FEATURE EXTRACTION
# ============================================================

import math
import re
from urllib.parse import urlparse


def _safe_url(url):
    """Normalize URL before processing."""

    if not isinstance(url, str):
        return ""

    url = url.strip()

    if not url:
        return ""

    if not re.match(
        r"^[a-zA-Z][a-zA-Z0-9+.-]*://",
        url
    ):
        url = "http://" + url

    return url


def _calculate_entropy(value):
    """Calculate Shannon entropy."""

    if not value:
        return 0.0

    frequencies = {}

    for character in value:
        frequencies[character] = (
            frequencies.get(character, 0) + 1
        )

    length = len(value)
    entropy = 0.0

    for count in frequencies.values():

        probability = count / length

        entropy -= (
            probability *
            math.log2(probability)
        )

    return entropy


def _has_ip_address(hostname):
    """Check whether hostname is an IPv4 address."""

    if not hostname:
        return 0

    pattern = r"^(?:\d{1,3}\.){3}\d{1,3}$"

    return int(
        bool(
            re.match(
                pattern,
                hostname
            )
        )
    )


def extract_url_features(url):
    """
    Extract 23 lexical features from a URL.
    """

    normalized_url = _safe_url(url)

    parsed = urlparse(
        normalized_url
    )

    hostname = parsed.hostname or ""
    path = parsed.path or ""
    query = parsed.query or ""
    fragment = parsed.fragment or ""

    features = {

        "url_length":
            len(normalized_url),

        "hostname_length":
            len(hostname),

        "path_length":
            len(path),

        "query_length":
            len(query),

        "digit_count":
            sum(
                character.isdigit()
                for character in normalized_url
            ),

        "letter_count":
            sum(
                character.isalpha()
                for character in normalized_url
            ),

        "special_character_count":
            sum(
                not character.isalnum()
                for character in normalized_url
            ),

        "dot_count":
            normalized_url.count("."),

        "slash_count":
            normalized_url.count("/"),

        "hyphen_count":
            normalized_url.count("-"),

        "underscore_count":
            normalized_url.count("_"),

        "question_count":
            normalized_url.count("?"),

        "equal_count":
            normalized_url.count("="),

        "ampersand_count":
            normalized_url.count("&"),

        "percent_count":
            normalized_url.count("%"),

        "subdomain_count":
            max(
                hostname.count(".") - 1,
                0
            ),

        "has_https":
            int(
                parsed.scheme.lower() == "https"
            ),

        "has_http":
            int(
                parsed.scheme.lower() == "http"
            ),

        "has_at_symbol":
            int(
                "@" in normalized_url
            ),

        "has_ip_address":
            _has_ip_address(hostname),

        "has_query":
            int(
                bool(query)
            ),

        "has_fragment":
            int(
                bool(fragment)
            ),

        "has_percent_encoding":
            int(
                "%" in normalized_url
            ),

        "has_suspicious_double_slash":
            int(
                "//" in path
            ),

        "url_entropy":
            _calculate_entropy(
                normalized_url
            )
    }

    return features


def extract_features_from_dataframe(
    dataframe,
    url_column="URL"
):
    """
    Extract URL features from every URL
    in a DataFrame.
    """

    if url_column not in dataframe.columns:
        raise ValueError(
            f"Column '{url_column}' not found."
        )

    feature_rows = []

    for url in dataframe[url_column]:

        feature_rows.append(
            extract_url_features(url)
        )

    return feature_rows