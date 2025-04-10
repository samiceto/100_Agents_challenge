import os
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
def main():
    agent = Agent(
        name="Python Assistant",
        instructions="You are a python assistant if you asked about any python related quiry you answer it consisely, remember you are talking to humen be polite, if you asked about anything that is not releted to the python you answer'i am a python assistant this question does not come under my experties'"

    )
    user_input = input("Ask anythin about python")

    result =Runner.run_sync(
        agent,
        input=user_input,
        run_config=run_confige
    )
    print(result.final_output)




    


if __name__ == "__main__":
    main()
