import litellm
from litellm import completion

import gradio as gr

#litellm._turn_on_debug()

#model="ollama_chat/llama3.2"
#model="ollama_chat/llama3.2:3b-instruct-fp16"
#model="ollama_chat/devstral"
model="ollama_chat/gemma3:12b"

messages = []

def add_to_chat(msg: str):
    messages.append({
        "role": "user",
        "content": msg
    })
    
    try:
        response = completion(
            api_base="http://localhost:11434",
            api_key="ollama",
            model=model,
            messages=messages,
            stream=False,
        )
        
        resp_msg = response.get("choices")[0].get("message").get("content")
        
        messages.append({
            "role": "assistant",
            "content": resp_msg
        })
    except Exception as e:
        print(f"Error: {e}")
        resp_msg = "Error: " + str(e)
    
    return resp_msg

def on_msg(message, history):
    print(f"User: {message}")
    response = add_to_chat(message)
    print(f"Assistant: {response}")
    return response

gr.ChatInterface(
    fn=on_msg, 
    type="messages"
).launch(share=False)
