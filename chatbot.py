import openai

#Use your API key for OpenAPI account
openai.api_key = "Your_API-key"

model_Engine = "text-davinci-002"

#Loop to Generate a response from chatgpt
while True:
    message = input("You: ")
    response = openai.Completion.create(
    engine = model_Engine,
    prompt =f"You: {message}\n Bot: ",
    max_tokens = 1024,
    temperature = 0.5,
    )
#print response
    print(f"Bot: {response.choices[0].text.rstrip()}\n")
