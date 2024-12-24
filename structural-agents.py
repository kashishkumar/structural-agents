from phi.agent import Agent
from phi.model.openai import OpenAIChat
from markdown import Markdown
from mdx_math import MathExtension
from yaml import safe_load

from dotenv import load_dotenv

load_dotenv(".env")

# Create custom markdown renderer with LaTeX support
md = Markdown(extensions=["mdx_math"])


def load_config(path):
    with open(path) as f:
        return safe_load(f)


config = load_config("config.yaml")

beam_design_agent = Agent(
    name=config["beam_design_agent"]["name"],
    model=OpenAIChat(id=config["beam_design_agent"]["model"]),
    tools=[],
    instructions=config["beam_design_agent"]["instructions"],
    show_tool_calls=True,
    markdown=True,
    markdown_renderer=md,
)

def main():
    beam_design_agent.print_response(
        config["beam_design_agent"]["query"],
        stream=False,
    )


if __name__ == "__main__":
    main()
