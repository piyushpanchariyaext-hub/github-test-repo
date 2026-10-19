"""Customer-support triage agent built on LangGraph + Anthropic Claude."""

from __future__ import annotations

import anthropic
from langgraph.graph import StateGraph, END


client = anthropic.Anthropic()


def classify(state: dict) -> dict:
    message = client.messages.create(
        model="claude-3-5-sonnet-latest",
        max_tokens=256,
        messages=[{"role": "user", "content": state["ticket"]}],
    )
    state["category"] = message.content[0].text
    return state


def build_graph():
    graph = StateGraph(dict)
    graph.add_node("classify", classify)
    graph.set_entry_point("classify")
    graph.add_edge("classify", END)
    return graph.compile()


if __name__ == "__main__":
    app = build_graph()
    print(app.invoke({"ticket": "My invoice is wrong"}))
