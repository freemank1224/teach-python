s = input("Please enter the model name in format 'provider:model_name': ")
if ':' not in s:
    raise ValueError("模型名称格式必须为 'provider:model_name'")
else:
    print(f"Model name: {s}")
    print(isinstance(s, str))
# Compare this snippet from Utility/NotebookAI.py:ol