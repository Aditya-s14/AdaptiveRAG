"""
Core configuration and environment settings.
"""

import os
import sys

from dotenv import load_dotenv

# Force UTF-8 stdout/stderr so debug prints of non-ASCII content (e.g. emojis in
# web-search results) don't crash on Windows consoles using the cp1252 codec.
for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        pass

load_dotenv()


class Settings:
    """Application settings loaded from environment variables."""

    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    GOOGLE_API_KEY: str = os.getenv("GOOGLE_API_KEY", "")
    TAVILY_API_KEY: str = os.getenv("TAVILY_API_KEY", "")
    QDRANT_URL = os.getenv("QDRANT_URL")
    QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
    CODE_COLLECTION = os.getenv("QDRANT_CODE_COLLECTION", "codebase")
    DOCS_COLLECTION = os.getenv("QDRANT_DOCS_COLLECTION", "guidelines")


settings = Settings()

# Set env variables for LangChain integrations
os.environ["OPENAI_API_KEY"] = settings.OPENAI_API_KEY
os.environ["GOOGLE_API_KEY"] = settings.GOOGLE_API_KEY
os.environ["TAVILY_API_KEY"] = settings.TAVILY_API_KEY
