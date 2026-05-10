"""
Model Configuration
Centralized model initialization for all agents.
Choose which model to use - by default, we use gpt-4o-mini, but you can uncomment and use other models as needed.
"""

from langchain_nvidia_ai_endpoints import ChatNVIDIA
from dotenv import load_dotenv

load_dotenv(override=True)

# NVIDIA - GLM-4.7 (Z.ai)
model = ChatNVIDIA(
    model="z-ai/glm4.7",
    temperature=0,
)
# Option 2: Anthropic Claude Sonnet 4.5 (uncomment to use)
# model = init_chat_model("claude-sonnet-4-5", temperature=0)

# Option 3: GPT OSS 120B (uncomment to use)
# model = ChatOpenAI(
#     model="openai/gpt-oss-120b",
#     base_url="https://your-path-to-gpt-oss-120b.dev/v1",
#     api_key="dummy_api_key",
#     default_headers={"X-API-KEY": "dummy_api_key"}
# )
