import os
from dotenv import load_dotenv

load_dotenv()  # loads .env in project root

def get_str(key: str, default: str = None) -> str:
    return os.getenv(key, default)

def get_int(key: str, default: int = None) -> int:
    val = os.getenv(key)
    return int(val) if val is not None else default

def get_bool(key: str, default: bool = False) -> bool:
    val = os.getenv(key)
    return val.lower() in ("1","true","yes") if val else default
