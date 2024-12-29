from openai import OpenAI

client = OpenAI()

response = client.audio.speech.create(
    model="tts-1",
    voice="alloy",
    input="こんにちは！犬と猫の見分け方を教えてください",
)

response.stream_to_file("output.mp3")
