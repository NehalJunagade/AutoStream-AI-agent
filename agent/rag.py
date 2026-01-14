import json
from pathlib import Path

KB_PATH = Path("data/knowledge_base.json")

def retrieve_knowledge(query: str) -> str:
    if not KB_PATH.exists():
        return "Knowledge base not found."

    with open(KB_PATH, "r", encoding="utf-8") as f:
        kb = json.load(f)

    query = query.lower()

    # Pricing related
    if "price" in query or "pricing" in query or "plan" in query:
        pricing = kb["pricing"]
        return (
            f"📦 AutoStream Pricing:\n"
            f"• Basic Plan: $29/month, 10 videos/month, 720p resolution\n"
            f"• Pro Plan: $79/month, Unlimited videos, 4K resolution, AI captions"
        )

    # Policy related
    if "refund" in query or "support" in query:
        policies = kb["policies"]
        return (
            f"📜 Company Policies:\n"
            f"• No refunds after 7 days\n"
            f"• 24/7 support available only on Pro plan"
        )

    return "I couldn't find relevant information. Can you rephrase?"

