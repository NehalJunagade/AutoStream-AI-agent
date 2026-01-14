## How to run the project locally
step1. Make a copy of the repository
step2. Install dependencies: pip install -r requirements.txt
step3. Configure OPENAI_API_KEY
step4.  Run: python main.py

## Architecture Explanation
In this project, a stateful conversational AI agent for AutoStream is implemented using LangGraph. LangGraph was selected because it offers explicit control over the state and flow of conversations, which is essential for controlling tool execution and intent transitions.
To achieve context retention without excessive memory development, the agent uses a shared state object to preserve conversation memory, which is restricted to the latest 5 to 6 turns. To guarantee stable behavior for high-intent actions, intent detection is rule-based. For RAG-based responses, a local JSON knowledge base is utilized, guaranteeing precise and well-founded responses for pricing and policies.Lead capture, or tool execution, is tightly regulated and only initiated if all necessary user information has been collected.

## Explain how you would integrate this agent with WhatsApp using Webhooks
This agent can be integrated with WhatsApp via a webhook-based method through providers like Meta WhatsApp Cloud API or Twilio. A webhook endpoint (such as FastAPI) is used to receive incoming communications.Every message calls the agent and modifies the LangGraph state. The provider's API is used to send the responses back to WhatsApp.