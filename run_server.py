# run_server.py

import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",      # Accessible from anywhere (use 127.0.0.1 for localhost only)
        port=8080,           # You can change this port if needed
        reload=True          # Auto-reload on code changes (great for development)
    )
