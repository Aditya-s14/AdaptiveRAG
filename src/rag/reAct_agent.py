"""
ReAct agent setup for document retrieval and question answering.
"""

from langchain.agents import create_react_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate

from src.config.settings import Config
from src.llms.openai import llm
from src.rag.retriever_setup import get_retriever

config = Config()

# Create ReAct agent prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", config.prompt("system_prompt")),
    ("human", "{input}"),
    ("ai", "{agent_scratchpad}")
])


def build_agent_executor() -> AgentExecutor:
    """
    Build a fresh ReAct agent executor bound to the current retriever.

    The retriever tool must be created on each call because the underlying
    FAISS vector store is replaced whenever a new document is uploaded.
    Binding the agent once at import time would leave it pointing at the
    initial empty (dummy) store and ignore all uploaded documents.

    Returns:
        A configured AgentExecutor using the latest retriever.
    """
    tools = [get_retriever()]
    react_agent = create_react_agent(llm, tools, prompt)
    return AgentExecutor(
        agent=react_agent,
        tools=tools,
        handle_parsing_errors=True,
        max_iterations=2,
        verbose=True,
        return_intermediate_steps=True
    )
