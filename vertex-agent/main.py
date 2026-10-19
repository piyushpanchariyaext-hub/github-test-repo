"""An agent deployed to Vertex AI Agent Engine (reasoning engine).

The reasoning-engine resource name below is a fake placeholder (test only).
"""

from __future__ import annotations

import vertexai
from google.adk.agents import Agent
from vertexai import agent_engines

root_agent = Agent(
    name="quality_inspector",
    model="gemini-1.5-pro",
    instruction="Inspect cement-plant quality metrics.",
)

REASONING_ENGINE = "projects/acp-test-proj/locations/europe-west1/reasoningEngines/cement-quality-inspector"

vertexai.init(project="acp-test-proj", location="europe-west1")


def query(prompt: str) -> str:
    engine = agent_engines.get(REASONING_ENGINE)
    return engine.query(input=prompt)["output"]


if __name__ == "__main__":
    print(query("What is the clinker ratio target?"))
