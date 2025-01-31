from phi.agent import Agent
from phi.model.openai import OpenAIChat
from yaml import safe_load

from dotenv import load_dotenv

load_dotenv(".env")

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
)


def main():
    beam_design_agent.print_response(
        query=config["beam_design_agent"]["query"],
        stream=True,
    )


if __name__ == "__main__":
    main()
