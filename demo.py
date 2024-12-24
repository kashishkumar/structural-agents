import chainlit as cl
#from structural_agents import beam_design_agent
from configmanager import config
from chainlit.types import ThreadDict

from dotenv import load_dotenv

load_dotenv(".env")


@cl.on_chat_start
async def start():
    print("Chat started")


@cl.on_message
async def on_message(message: cl.Message):
    #response = beam_design_agent.print_response(query=message.content, stream=False)
    response = "Hello"
    await cl.Message(content=response).send()


@cl.on_stop
async def stop():
    print("Chat stopped")


@cl.on_chat_end
async def end():
    print("Chat ended")


@cl.on_chat_resume
async def resume(thread: ThreadDict):
    print("Chat resumed")
