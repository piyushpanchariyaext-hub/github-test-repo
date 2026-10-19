"""A two-agent research crew: a searcher and a writer, orchestrated by CrewAI.

Talks to the OpenAI API at https://api.openai.com/v1 (fake key, test only).
"""

from __future__ import annotations

import os

from crewai import Agent, Crew, Task

os.environ.setdefault("OPENAI_API_BASE", "https://api.openai.com/v1")
os.environ.setdefault("OPENAI_API_KEY", "sk-fake-placeholder-for-testing-only")

researcher = Agent(
    role="Researcher",
    goal="Find relevant sources on a topic",
    backstory="A diligent analyst.",
    llm="gpt-4o",
)

writer = Agent(
    role="Writer",
    goal="Summarize findings into a brief",
    backstory="A concise technical writer.",
    llm="gpt-4o",
)

crew = Crew(
    agents=[researcher, writer],
    tasks=[
        Task(description="Research {topic}", agent=researcher, expected_output="notes"),
        Task(description="Write a summary", agent=writer, expected_output="brief"),
    ],
)

if __name__ == "__main__":
    print(crew.kickoff(inputs={"topic": "carbon-neutral cement"}))
