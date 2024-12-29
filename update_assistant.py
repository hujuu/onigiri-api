from openai import OpenAI

client = OpenAI()

# アシスタントID
assistant_id = "asst_dEhcT3BpNzgsWfZBB7LPm99y"

# アシスタントを更新
response = client.beta.assistants.update(
    assistant_id=assistant_id,
    name="競技プログラミングアシスタント",
    description="競技プログラミングに関する質問に答えるアシスタント",
)

print(response)
