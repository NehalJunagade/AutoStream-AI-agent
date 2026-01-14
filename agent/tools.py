import json

def get_autostream_info(query: str) -> str:
    """Retrieves pricing and policy info from the local knowledge base."""
    with open("knowledge_base.json", "r") as f:
        data = json.load(f)
    return f"AutoStream Info: {json.dumps(data)}"

def mock_lead_capture(name: str, email: str, platform: str):
    """
    Captures high-intent lead details. 
    ONLY call this when you have the user's Name, Email, AND Creator Platform.
    """
    print(f"\n>>> Lead captured successfully: {name}, {email}, {platform}")
    return "SUCCESS: Lead recorded. Our team will contact you soon!"
