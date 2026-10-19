"""A hosted agent running on AWS Bedrock AgentCore Runtime.

The runtime ARN below is a fake placeholder in eu-central-1 (test only).
"""

from __future__ import annotations

from bedrock_agentcore.runtime import BedrockAgentCoreApp
from strands import Agent

RUNTIME_ARN = "arn:aws:bedrock-agentcore:eu-central-1:111111111111:runtime/cement-quality-inspector"

app = BedrockAgentCoreApp()
agent = Agent(model="anthropic.claude-3-5-sonnet-20241022-v2:0")


@app.entrypoint
def invoke(payload: dict) -> dict:
    return {"result": str(agent(payload.get("prompt", "")))}


if __name__ == "__main__":
    app.run()
