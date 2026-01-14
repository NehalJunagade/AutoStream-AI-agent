def detect_intent(text: str) -> str:
    text = text.lower()

    if any(word in text for word in ["hi", "hello", "hey", "hii"]):
        return "greeting"

    if any(word in text for word in ["price", "pricing", "cost", "plan"]):
        return "pricing"

    # High-intent phrases (expanded)
    if any(phrase in text for phrase in [
        "i want to try",
        "want to try",
        "sign up",
        "signup",
        "subscribe",
        "buy",
        "get started",
        "start pro",
        "try pro",
        "use pro",
        "pro plan"
    ]):
        return "high_intent"

    return "unknown"
