from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from src.mcp.mcp_client import MCPClient
from src.llm.groq_llm import GroqLLM

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

mcp_client = MCPClient()
llm = GroqLLM()

@app.get("/tools")
def list_tools():
    return mcp_client.list_tools()

@app.post("/ask")
async def ask_mcp(request: Request):
    data = await request.json()
    question = data.get("question", "").lower()

    try:
        llm_reply = llm.get_response(f"Customer asked: {question}. Do we need MCP data?")
    except Exception as e:
        llm_reply = f"LLM error: {e}"

    if "monitor" in question:
        result = mcp_client.call_tool("get_product_info", {"product": "monitor"})
    else:
        result = "No tool triggered."

    return {
        "llm_decision": llm_reply,
        "tool_response": result
    }
