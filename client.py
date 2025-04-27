from openai import OpenAI

client = OpenAI(
  api_key="add your api"
)

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  store=True,
  messages=[
    {"role": "system", "content": "You are a virtual assistant name jarvis."},
    {"role": "user", "content": "write an essay about money"}
  ]
)

print(completion.choices[0].message.content);
