# acp-test-agents

A **fixture repository** for testing the AI Governance Cockpit's GitHub repo-scan
connector. It is a monorepo containing several independently-anchored agent
directories, each built to trigger a different family of the discovery
scanner's detectors, plus one non-agentic directory to confirm precision.

When the GitHub connector scans this repo, the discovery service should surface
**one candidate agent per anchored directory** (monorepo clustering), and skip
the plain web app.

## What's inside

| Directory             | Should be detected as                         | Signal family |
|-----------------------|-----------------------------------------------|---------------|
| `support-agent/`      | LangGraph (Python framework) + Anthropic SDK  | manifest + import |
| `research-agent/`     | CrewAI (Python framework) + OpenAI endpoint   | manifest + import + endpoint |
| `node-assistant/`     | Vercel AI SDK + OpenAI SDK (Node)             | manifest + import |
| `bedrock-agent/`      | AWS Bedrock AgentCore + Bedrock ARN endpoint  | manifest + endpoint |
| `mcp-tools/`          | Model Context Protocol server                 | protocol marker |
| `vertex-agent/`       | Vertex AI + Vertex reasoning-engine endpoint  | import + endpoint |
| `plain-website/`      | *(nothing — non-agentic control)*             | — |

> This repo contains **no real credentials**. Every ARN, project id, host, and
> key is a syntactically valid but fake placeholder, purely to exercise the
> regex detectors.
