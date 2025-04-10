
import os
import chainlit as cl
from agents import Agent, OpenAIChatCompletionsModel,AsyncOpenAI,RunConfig,Runner
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

gemini_api_key =os.getenv("GEMINI_API_KEY") 


provider=AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=provider
)

run_confige =RunConfig(
    model=model,
    model_provider=provider,
    tracing_disabled=True
)

agent = Agent(
    name="Python Assistant",
    instructions="You are a python assistant if you asked about any python related quiry you answer it consisely, remember you are talking to humen be polite, if you asked about anything that is not releted to the python you answer'i am a python assistant this question does not come under my experties'"

)


@cl.on_chat_start
async def start():
    await cl.Message(content = "Hello how can i help you today?").send()

@cl.on_message
async def main(message:cl.Message):
    response = f"your masssege {message.content}"
    result =Runner.run_sync(
    agent,
    input=response,
    run_config=run_confige
    )
    await cl.Message(content=result.final_output).send()

    
