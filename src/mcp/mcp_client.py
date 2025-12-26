import os
import httpx
from dotenv import load_dotenv

load_dotenv()

class MCPClient:
    def __init__(self):
        self.base_url = os.getenv("MCP_SERVER_URL", "").rstrip("/")

    def call_tool(self, method: str, arguments: dict):
        url = self.base_url
        payload = {
            "jsonrpc": "2.0",
            "id": "1",
            "method": method,
            "params": arguments
        }

        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

        try:
            response = httpx.post(url, json=payload, headers=headers, timeout=10)
            print("🛰 MCP status:", response.status_code)
            print("📦 MCP response:", response.text)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            return {"error": str(e)}
