import openai

def chat_completion(
    messages=None,
    model="gpt-3.5-turbo",
    temperature=1,
    top_p=1,
    n=1,
    stream=False,
    stop=None,
    max_tokens=None,
    presence_penalty=0,
    frequency_penalty=0,
    logit_bias=None,
    user=None,
    type="messages"
):
    openai.api_key = "YOUR_OPENAI_API_KEY"
    
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages or [],
        temperature=temperature,
        top_p=top_p,
        n=n,
        stream=stream,
        stop=stop,
        max_tokens=max_tokens,
        presence_penalty=presence_penalty,
        frequency_penalty=frequency_penalty,
        logit_bias=logit_bias,
        user=user
    )
    
    if type == "console":
        print(response['choices'][0]['message']['content'])
    elif type == "viewer":
        from IPython.display import display
        display(response['choices'][0]['message']['content'])
    else:
        return response['choices'][0]['message']['content']

# 예시 메시지
if __name__ == "__main__":
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello! How can you help me today?"}
    ]
    
    response = chat_completion(messages=messages)
    print(response)
