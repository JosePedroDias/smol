from smolagents import (
    ToolCallingAgent,
    CodeAgent,
    InferenceClientModel,
    LiteLLMModel,
    OpenAIServerModel,
    TransformersModel,
    DuckDuckGoSearchTool,
    GradioUI,
)

from tools import get_weather, get_reuters_headlines
from gemini import geminiModel

available_inferences = ["inference_client", "transformers", "ollama", "litellm", "openai", "gemini"]
chosen_inference = "ollama"

if chosen_inference == "inference_client": # TODO?
    model = InferenceClientModel(
        #model_id="ollama_chat/llama3.2:3b-instruct-fp16",
        model_id="ollama_chat/qwen2.5-coder:14b-instruct-q2_K",
        provider="ollama",
    )
elif chosen_inference == "transformers":
    model = TransformersModel(model_id="HuggingFaceTB/SmolLM2-1.7B-Instruct", device_map="auto", max_new_tokens=1000)
elif chosen_inference == "ollama":
    model = LiteLLMModel(
        #model_id="ollama_chat/llama3.2",
        #model_id="ollama_chat/qwen2.5-coder:14b-instruct-q2_K",
        #model_id="ollama_chat/qwen2.5-coder:7b-instruct",
        model_id="ollama_chat/devstral",
        api_base="http://localhost:11434",  # replace with remote open-ai compatible server if necessary
        api_key="your-api-key",  # replace with API key if necessary
        num_ctx=8192,  # ollama default is 2048 which will often fail horribly. 8192 works for easy tasks, more is better. Check https://huggingface.co/spaces/NyxKrage/LLM-Model-VRAM-Calculator to calculate how much VRAM this will need for the selected model.
    )
elif chosen_inference == "litellm":
    # For anthropic: change model_id below to 'anthropic/claude-3-5-sonnet-latest'
    model = LiteLLMModel(model_id="gpt-4o")
elif chosen_inference == "openai":
    # For anthropic: change model_id below to 'anthropic/claude-3-5-sonnet-latest'
    model = OpenAIServerModel(model_id="gpt-4o")
elif chosen_inference == "gemini":
    model = geminiModel

if False:
    agent = ToolCallingAgent(
        tools=[
            #get_weather
            #WebSearchTool(),
            #DuckDuckGoSearchTool()
        ],
        add_base_tools=True,
        model=model,
        verbosity_level=2
    )
else:
    agent = CodeAgent(
        model=model,
        tools=[
            #get_weather,
            #WebSearchTool(),
            #DuckDuckGoSearchTool()
        ],
        add_base_tools=True,
        additional_authorized_imports=['*'], # dangerous...
        #additional_authorized_imports=['requests', 'bs4', 'datetime', "numpy", "pandas", "matplotlib", "seaborn"],
        
        #executor_type="docker", # optional, more secure. TODO
        #executor_type="e2b", #$$
        
        verbosity_level=2,
        planning_interval=3,
        #stream_outputs=False,
        #use_structured_outputs_internally=True, # TODO fails
        name="example_agent",
        description="This is an example agent.",
    )
    
if __name__ == "__main__":
    use_gradio = True
    
    if use_gradio:
        GradioUI(agent).launch(share=False)
    else:    
        #question = "What's the weather like in Lisbon?"
        #question = "What time is it?"
        #question = "which football club won the 2024/2025 portuguese liga?"
        _question = """What were the results of last week's portuguese election?
Create a CSV file with the parties and percentages they got.
Plot those results as a pie chart into a PNG file.
Which party won?"""
        #question = "create a table with the portuguese liga results for the 2024/2025 season, with the teams and their points. Which team won?"
        #question = "what's the formula 1 grand prix going on this weekend?"
        #question = "find out the names of the drivers and teams taking part in the 2025/2026 formula 1 season. Create a CSV file with the points each driver has. create a table as a PNG file with the data."
        #question = "how many days until the longer day in the year?"
        #question = "can you list all music albums the band Ghost has released, with the respective years they were released at?"
        question = "what's the colder month in the year?"
        
        print("CodeAgent:", agent.run(question))
        print(dir(agent))
    