from langchain_groq import ChatGroq
from langchain_tavily import TavilySearch
from langgraph.prebuilt import create_react_agent
from langchain_core.messages.ai import AIMessage
from typing import List, Optional

def get_response_from_ai_agents(
    llm_id: str,
    messages: List[str],
    allow_search: bool = True,
    system_prompt: Optional[str] = None
) -> str:
    """
    Sends messages to the AI agent and returns the latest AI response.
    """
    
    # Initialize LLM
    llm = ChatGroq(model=llm_id)

    # Initialize tools if allowed
    tools = [TavilySearch(max_results=2)] if allow_search else []

    # Create agent (modern API — no state_modifier or initial_state)
    agent = create_react_agent(model=llm, tools=tools)

    # Prepare the full input messages
    full_input = []
    if system_prompt:
        full_input.append(f"SYSTEM PROMPT: {system_prompt}")
    full_input.extend(messages)

    state = {"messages": " ".join(full_input)}

    # Invoke the agent
    response = agent.invoke(state)

    # Extract AI messages
    messages_resp: List[AIMessage] = response.get("messages", [])
    ai_messages: List[str] = [m.content for m in messages_resp if isinstance(m, AIMessage)]

    return ai_messages[-1] if ai_messages else "No response from AI"
