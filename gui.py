# ============================================================
# PHISHGUARD AI - GUI
# ============================================================

import tkinter as tk
from tkinter import messagebox

from app import predict_url


# ============================================================
# ANALYZE BUTTON
# ============================================================

def analyze():

    url = url_entry.get().strip()

    if not url:
        messagebox.showwarning(
            "Missing URL",
            "Please enter a URL."
        )
        return

    try:

        result = predict_url(url)

        if not result["success"]:

            result_label.config(
                text="ERROR"
            )

            risk_label.config(
                text="-"
            )

            explanation_label.config(
                text=result["message"]
            )

            return

        # Prediction
        result_label.config(
            text=result["result"]
        )

        # Risk
        risk_label.config(
            text=(
                f"{result['risk_level']} "
                f"({result['risk_score']}/100)"
            )
        )

        # Probabilities
        probability_label.config(
            text=(
                f"Phishing: "
                f"{result['phishing_probability'] * 100:.2f}%\n"
                f"Legitimate: "
                f"{result['legitimate_probability'] * 100:.2f}%"
            )
        )

        # Explanation
        if result["result"] == "PHISHING":

            explanation = (
                "⚠ This URL has been classified as "
                "potentially dangerous."
            )

        else:

            explanation = (
                "✓ This URL has been classified as "
                "legitimate."
            )

        explanation_label.config(
            text=explanation
        )

    except Exception as error:

        messagebox.showerror(
            "Analysis Error",
            str(error)
        )


# ============================================================
# CLEAR BUTTON
# ============================================================

def clear():

    url_entry.delete(
        0,
        tk.END
    )

    result_label.config(
        text="-"
    )

    risk_label.config(
        text="-"
    )

    probability_label.config(
        text="-"
    )

    explanation_label.config(
        text="Enter a URL and click Analyze."
    )


# ============================================================
# MAIN WINDOW
# ============================================================

root = tk.Tk()

root.title(
    "PhishGuard AI - Phishing URL Detector"
)

root.geometry(
    "700x520"
)

root.resizable(
    False,
    False
)


# ============================================================
# TITLE
# ============================================================

title_label = tk.Label(
    root,
    text="PHISHGUARD AI",
    font=("Arial", 24, "bold")
)

title_label.pack(
    pady=(25, 5)
)


subtitle_label = tk.Label(
    root,
    text="AI-Based Phishing URL Detection",
    font=("Arial", 12)
)

subtitle_label.pack(
    pady=(0, 20)
)


# ============================================================
# URL INPUT
# ============================================================

url_label = tk.Label(
    root,
    text="Enter URL:",
    font=("Arial", 12, "bold")
)

url_label.pack(
    pady=(5, 5)
)


url_entry = tk.Entry(
    root,
    width=70,
    font=("Arial", 11)
)

url_entry.pack(
    ipady=7
)


# ============================================================
# BUTTONS
# ============================================================

button_frame = tk.Frame(
    root
)

button_frame.pack(
    pady=20
)


analyze_button = tk.Button(
    button_frame,
    text="Analyze URL",
    command=analyze,
    font=("Arial", 11, "bold"),
    width=18
)

analyze_button.pack(
    side=tk.LEFT,
    padx=10
)


clear_button = tk.Button(
    button_frame,
    text="Clear",
    command=clear,
    font=("Arial", 11),
    width=12
)

clear_button.pack(
    side=tk.LEFT,
    padx=10
)


# ============================================================
# RESULT SECTION
# ============================================================

result_title = tk.Label(
    root,
    text="Prediction:",
    font=("Arial", 12, "bold")
)

result_title.pack(
    pady=(10, 2)
)


result_label = tk.Label(
    root,
    text="-",
    font=("Arial", 18, "bold")
)

result_label.pack()


# ============================================================
# RISK
# ============================================================

risk_title = tk.Label(
    root,
    text="Risk:",
    font=("Arial", 12, "bold")
)

risk_title.pack(
    pady=(15, 2)
)


risk_label = tk.Label(
    root,
    text="-",
    font=("Arial", 15, "bold")
)

risk_label.pack()


# ============================================================
# PROBABILITY
# ============================================================

probability_title = tk.Label(
    root,
    text="Model Probability:",
    font=("Arial", 12, "bold")
)

probability_title.pack(
    pady=(15, 2)
)


probability_label = tk.Label(
    root,
    text="-",
    font=("Arial", 11)
)

probability_label.pack()


# ============================================================
# EXPLANATION
# ============================================================

explanation_label = tk.Label(
    root,
    text="Enter a URL and click Analyze.",
    font=("Arial", 11),
    wraplength=600
)

explanation_label.pack(
    pady=20
)


# ============================================================
# START GUI
# ============================================================

root.mainloop()