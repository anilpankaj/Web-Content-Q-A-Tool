from fastapi import FastAPI, Form, Request, HTTPException
from fastapi.responses import HTMLResponse
from scrape import scrape_url
from qa import answer_question

app = FastAPI()

# In-memory storage for scraped content
content_store = {}

# Homepage with UI
@app.get("/", response_class=HTMLResponse)
async def home():
    return """
    <html>
        <head>
            <title>Web Content Q&A Tool</title>
            <style>
                body { font-family: Arial, sans-serif; margin: 20px; }
                textarea, input { width: 100%; padding: 10px; margin: 10px 0; }
                button { padding: 10px 20px; background: #007BFF; color: white; border: none; cursor: pointer; }
                button:hover { background: #0056b3; }
            </style>
        </head>
        <body>
            <h1>Web Content Q&A Tool</h1>
            <form action="/ingest" method="post">
                <label for="urls">Enter URLs (one per line):</label><br>
                <textarea id="urls" name="urls" rows="5"></textarea><br>
                <button type="submit">Ingest Content</button>
            </form>
            <hr>
            <form action="/ask" method="post">
                <label for="question">Ask a question:</label><br>
                <input type="text" id="question" name="question" required><br>
                <button type="submit">Get Answer</button>
            </form>
            <h2>Answer:</h2>
            <p id="answer"></p>
        </body>
    </html>
    """

# Ingest URLs and scrape content
@app.post("/ingest")
async def ingest(urls: str = Form(...)):
    global content_store
    urls_list = urls.strip().split("\n")
    content_store = {}
    for url in urls_list:
        url = url.strip()
        if url:
            try:
                content = scrape_url(url)
                content_store[url] = content
            except Exception as e:
                raise HTTPException(status_code=400, detail=f"Failed to scrape {url}: {str(e)}")
    return {"message": "Content ingested successfully!"}

# Answer questions based on ingested content
@app.post("/ask")
async def ask(question: str = Form(...)):
    if not content_store:
        raise HTTPException(status_code=400, detail="No content ingested. Please provide URLs first.")
    combined_content = "\n".join(content_store.values())
    answer = answer_question(combined_content, question)
    return {"answer": answer}

# Run the app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)