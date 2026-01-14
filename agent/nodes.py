from .intents import detect_intent
from .knowledge import retrieve_knowledge

def mock_lead_capture(name, email, platform):
    print(f"Lead captured successfully: {name}, {email}, {platform}")

def agent_node(state: dict) -> dict:
    state["messages"] = state["messages"][-6:]

    user_input = state["messages"][-1]
    intent = detect_intent(user_input)

    if intent == "greeting":
        response = "Hi 👋 Welcome to AutoStream! How can I help you?"

    elif intent == "pricing":
        response = retrieve_knowledge(user_input)

    elif intent == "high_intent":
        lead = state.get("lead", {})

        if "name" not in lead:
            response = "Great! May I know your name?"
        elif "email" not in lead:
            lead["name"] = user_input
            response = "Thanks! Please share your email."
        elif "platform" not in lead:
            lead["email"] = user_input
            response = "Which platform do you create content on?"
        else:
            lead["platform"] = user_input
            mock_lead_capture(
                lead["name"], lead["email"], lead["platform"]
            )
            response = "You're all set! Our team will contact you soon 🚀"

        state["lead"] = lead

    else:
        response = "I can help with pricing or getting you started."

    state["messages"].append(response)
    return state
