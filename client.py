# from openai import OpenAI

# client = OpenAI(
#   api_key="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"
# )
# completion = client.chat.completions.create(
#       model="gpt-4o-mini",
#       messages=[
#           {"role": "system", "content": "You are a virtual assistant name jarvis."},
#           {
#               "role": "user",
#               "content": "Write an essay in money."
#           }
#       ]
#   )

# print(completion.choices[0].message)
from openai import OpenAI

client = OpenAI(
  api_key="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"
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
