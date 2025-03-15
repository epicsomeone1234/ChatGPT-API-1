from openai import OpenAI

client = OpenAI(
    api_key = ""
)

assistant_prompt = "You will lie in response to every prompt/message"
user_prompt = input("Input something for liarGPT to answer: ")
response = client.chat.completions.create(
    model="gpt-3.5-turbo-0125",
    messages=[
        {"role": "system", "content": assistant_prompt},
        {"role": "user", "content": user_prompt}
    ]
)

user_prompt = input(response.choices[0].message.content + " ")

response = client.chat.completions.create(
    model="gpt-3.5-turbo-0125",
    messages=[
        {"role": "system", "content": assistant_prompt},
        {"role": "user", "content": user_prompt}
    ]
)

print(response.choices[0].message.content + " ")