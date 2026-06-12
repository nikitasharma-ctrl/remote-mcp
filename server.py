# server.py
from fastmcp import FastMCP
import os

mcp = FastMCP("my-remote-server")

@mcp.tool()
def summarize_text(text: str) -> str:
    return f"Summary: {text[:100]}..."

if __name__ == "__main__":
    import os
    
    # Render automatically assigns an operational port variable dynamically.
    # We must listen on 0.0.0.0 so the global internet can find the service.
    port = int(os.getenv("PORT", 8000))
    
    # FIX: Changed "streamable-http" to "http"
    mcp.run(transport="http", host="0.0.0.0", port=port)