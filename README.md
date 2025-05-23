```
uv init asd
cd asd
uv add x
uv venv
source .venv/bin/activate.fish

python agent.py
```

https://ollama.com/library/llama3.2/tags
https://ollama.com/library/qwen2.5-coder/tags

```
OLLAMA_FLASH_ATTENTION=true OLLAMA_KV_CACHE_TYPE=f16 ollama serve &
#ollama run llama3.2
#ollama run llama3.2:3b-instruct-fp16
#ollama run qwen2.5-coder:14b-instruct-q2_K
#ollama run qwen2.5-coder:7b-instruct
ollama run devstral
ollama run gemma3:12b
/exit
```

```
du ~/.ollama
system_profiler SPDisplaysDataType
vm_stat
```

# should run in 32MB shared RAM

✅ llama3:8b-instruct
✅ phi3:mini
✅ mistral:instruct
✅ gemma:7b
