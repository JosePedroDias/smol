import litellm
from litellm import completion

#litellm._turn_on_debug()

response = completion(
    #model="ollama_chat/llama3.2",
    model="ollama_chat/llama3.2:3b-instruct-fp16",
    api_key="ollama",
    api_base="http://localhost:11434",
    messages=[{
        "role": "user",
        "content": "respond in 20 words. who are you?"
    }],
    #stream=True
)
print(response)
print(response.get("choices")[0].get("message").get("content"))
