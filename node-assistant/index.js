import { openai } from "@ai-sdk/openai";
import { generateText } from "ai";

export async function ask(prompt) {
  const { text } = await generateText({
    model: openai("gpt-4o-mini"),
    prompt,
  });
  return text;
}

if (import.meta.url === `file://${process.argv[1]}`) {
  ask("Summarize our cement sustainability roadmap.").then(console.log);
}
