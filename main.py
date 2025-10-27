import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
import os

# Create a FastAPI app instance
app = FastAPI(
    title="DataMindz Landing Page Server",
    description="A simple API to serve the DataMindz landing page.",
    version="1.0.0"
)

# Define the path for the HTML file
html_file_path = "index.html"

@app.get("/", response_class=FileResponse)
async def get_landing_page():
    """
    Serves the main landing page (index.html).
    """
    if not os.path.exists(html_file_path):
        raise HTTPException(status_code=404, detail="index.html not found. Make sure the file is in the same directory as main.py.")
        
    return FileResponse(html_file_path)

# Add a simple health check endpoint
@app.get("/health")
async def health_check():
    """
    Simple health check endpoint.
    """
    return {"status": "ok"}

if __name__ == "__main__":
    """
    This allows you to run the server directly using `python main.py`
    It will be available at http://127.0.0.1:8000
    """
    print("Starting FastAPI server for DataMindz...")
    print("Access the landing page at http://127.0.0.1:8000")
    uvicorn.run(app, host="127.0.0.1", port=8000)
