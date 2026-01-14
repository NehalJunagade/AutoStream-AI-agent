
# AutoStream Conversational AI Agent

from langgraph.graph import StateGraph, END
from typing import TypedDict, List

# Knowledge Base (RAG)

KNOWLEDGE_BASE = {
    "pricing": (
        "📦 AutoStream Pricing:\n"
        "• Basic Plan – $29/month (10 videos, 720p)\n"
        "• Pro Plan – $79/month (Unlimited videos, 4K, AI captions)"
    ),
    "policies": (
        "📜 AutoStream Policies:\n"
        "• No refunds after 7 days\n"
        "• 24/7 support only for Pro users"
    )
}

# Mock Tool


def mock_lead_capture(name, email, platform):
    print(f"\n✅ Lead captured successfully: {name}, {email}, {platform}\n")


# Intent Detection

import string

def detect_intent(text: str) -> str:
    text = text.lower()
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))

    # HIGH INTENT FIRST
    if any(w in text for w in [
        "buy", "subscribe", "signup", "sign up", "try", "i want"
    ]):
        return "high_intent"

    if any(w in text for w in ["hi", "hello", "hii", "hey"]):
        return "greeting"

    if any(w in text for w in [
        "price", "pricing", "cost", "plan", "cheaper", "basic", "pro"
    ]):
        return "product_inquiry"

    if any(w in text for w in [
        "policy", "policies", "refund", "support", "terms"
    ]):
        return "policy_inquiry"

    return "general_question"

# Agent Logic
from typing import TypedDict, List

class AgentState(TypedDict):
    messages: List[str]
    lead: dict

def agent_node(state: AgentState) -> AgentState:
    state["messages"] = state["messages"][-6:]
    user_input = state["messages"][-1]
    lead = state["lead"]


    # Lead Capture State Machine

    if lead.get("high_intent", False):
        if "name" not in lead or lead["name"] is None:
            lead["name"] = user_input
            response = "Thanks! Please share your email."
        elif "email" not in lead or lead["email"] is None:
            lead["email"] = user_input
            response = "Which platform do you create content on? (YouTube, Instagram, etc.)"
        elif "platform" not in lead or lead["platform"] is None:
            lead["platform"] = user_input
            mock_lead_capture(lead["name"], lead["email"], lead["platform"])
            response = "🎉 You’re all set! Our team will contact you shortly."
            lead.clear()  # reset lead after completion
        state["messages"].append(response)
        return state

    # Regular Intent Detection
    
    intent = detect_intent(user_input)

    if intent == "greeting":
        response = "Hi 👋 Welcome to AutoStream! How can I help you?"

    elif intent == "product_inquiry":
        response = KNOWLEDGE_BASE["pricing"]

    elif intent == "policy_inquiry":
        response = KNOWLEDGE_BASE["policies"]

    elif intent == "high_intent":
        response = "Great! May I know your name?"
        lead["high_intent"] = True  # start lead capture
        lead["name"] = None
        lead["email"] = None
        lead["platform"] = None

    else:
        response = "I can help you with pricing, policies, or getting started."

    state["messages"].append(response)
    return state



# CLI Runner

if __name__ == "__main__":
    # Build the state graph
    workflow = StateGraph(AgentState)
    workflow.add_node("agent", agent_node)
    workflow.set_entry_point("agent")
    workflow.add_edge("agent", END)
    app = workflow.compile()

    print("\n🎬 AutoStream Conversational AI Agent")
    print("Type 'exit' to quit\n")

    state = {
        "messages": [],
        "lead": {}
    }

    while True:
        user_input = input("User: ")
        if user_input.lower() == "exit":
            break

        state["messages"].append(user_input)
        state = app.invoke(state)

        print("Agent:", state["messages"][-1])
