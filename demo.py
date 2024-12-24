import chainlit as cl
from structural_agents import beam_design_agent
from configmanager import config


@cl.on_message
async def main(message: cl.Message):
    response = beam_design_agent.print_response(message.content, stream=False)
    await cl.Message(content=response).send()


message = cl.Message(content=config["beam_design_agent"]["query"])

cl.run(message)
