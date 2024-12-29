from openai import OpenAI

client = OpenAI()

assistant = client.beta.assistants.create(
    name="Math Tutor",
    instructions="あなたはラッパーです。韻を踏むようにしてください。",
    tools=[{"type": "code_interpreter"}],
    model="gpt-4o-mini",
)
