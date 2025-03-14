import time
from IPython.core.getipython import get_ipython

class NotebookManager:
    def __init__(self):
        self.shell = get_ipython()
        if self.shell is None:
            raise RuntimeError("This code must be run in a Jupyter notebook environment")

    def create_code_cell(self, content, cell_type='code'):
        """Create new code cell"""
        payload = dict(
            source = 'set_next_input',
            text = content,
            replace = False
        )
        self.shell.payload_manager.write_payload(payload)

    def create_markdown_cell(self, content, cell_type='markdown'):
        """Create new markdown cell"""
        payload = dict(
            source = 'set_next_input',
            text = content,
            replace = False
        )
        self.shell.payload_manager.write_payload(payload)

    def run_cell(self, code):
        result = self.shell.run_cell(code)
        return result

class AIAssistant:
    def __init__(self, model='ollama:phi4'):
        """
        初始化 AIAssistant
        :param model: AI模型名称，格式为 'provider:model_name'
        """
        try:
            self.nb_manager = NotebookManager()
            self._validate_model_name(model)
            # 移除之前的引号添加，因为会在 _setup_environment 中处理
            self.model = model
            self._setup_environment()
        except RuntimeError as e:
            print(f"初始化失败: {str(e)}")
            raise

    def _validate_model_name(self, model):
        """验证模型名称格式"""
        if not isinstance(model, str):
            raise ValueError("模型名称必须是字符串")
        if ':' not in model:
            raise ValueError("模型名称格式必须为 'provider:model_name'")

    def _setup_environment(self):
        """设置 Jupyter 环境和模型配置"""
        commands = [
            '%load_ext jupyter_ai_magics',
            f"%config AiMagics.default_language_model = '{self.model}'"  # 直接在这里添加引号
        ]
        self.init_prompt = '\n'.join(commands)
        print(f"Debug - Generated prompt:\n{self.init_prompt}")  # 调试输出
        self.nb_manager.create_code_cell(self.init_prompt)
        self.nb_manager.run_cell(self.init_prompt)
        print(f"NotebookAI initialized with model: '{self.model}'")
        print("You can now start using the AI assistant. BUT remember the following tips:")
        print("1. The assistant NEVER gives you the final anwser directly.")
        print("2. You can use `ask_cell()` method will give you helps on the cell content, when you use this method, you should specify the cell number first, then provide your questions.")

    def ask_cell(self):
        """修复代码"""
        input_idx = input("请输入要提问的代码块编号: | Please specify the cell number you want to ask: ")
        if not input_idx.isdigit():
            raise ValueError("代码块编号必须是数字! | The cell number must be a digit!")
        
        self.cell_idx = f"_i{input_idx}"
        self.cell_content = self.nb_manager.shell.user_ns[self.cell_idx]

        self.user_question = input("请输入你的问题: | Please enter your question: ")
        if not isinstance(self.user_question, str):
            raise ValueError("问题必须是字符串" | "The question must be a string!")

        self.sys_prompt = f"%%ai\n"
        self.sys_prompt += f"You are an experienced coding instructor, and you are asked to help a learner to improve his/her coding skills.\n"
        self.sys_prompt += f"The user will ask questions or express his/her confusions based on some code sections.\n"
        self.sys_prompt += f"Remember the following rules:\n"
        self.sys_prompt += f"1. You should NEVER give the user final anwser directly.\n"
        self.sys_prompt += f"2. You should give the user a step-by-step guidance based on their questions and provided cell content.\n"
        self.sys_prompt += f"3. You should give the user some hints or corresoonding examples to help the user understand the code better.\n"
        self.sys_prompt += f"4. If the user asked in English, you provide your answer in English; if the user asked in Chinese, you provide your answer in Chinese!\n"
        self.sys_prompt += f"The code block is: {self.cell_content}\n"
        self.sys_prompt += f"The user's question is: {self.user_question}\n"

        self.nb_manager.create_code_cell(self.sys_prompt)
        self.nb_manager.run_cell(self.sys_prompt)