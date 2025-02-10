# Web Content Q&A Tool

This tool allows users to enter URLs, extract their content, and ask questions based on the retrieved information. It is developed using Python and FastAPI.

## Key Features

- **URL Extraction**: Enter one or more URLs to fetch and store text content.
- **Question Answering**: Ask queries based on the extracted data.
- **Simple Interface**: Easy-to-use web-based interface.
- **Reliable Responses**: Answers are generated strictly from the ingested content.

## Project Structure

```
web-content-qa-tool/
│
├── main.py            # FastAPI application (entry point)
├── scrape.py          # Web scraping logic
├── qa.py              # Question answering logic
├── requirements.txt   # List of dependencies
├── README.md          # Project documentation
```

## Code Overview

### main.py
- The FastAPI application.
- Handles URL ingestion and question answering.
- Serves the web interface.

### scrape.py
- Scrapes text content from the provided URLs using requests and BeautifulSoup.

### qa.py
- Answers questions based on the ingested content using keyword matching.

## Advanced: Using NLP Models
For more accurate answers, we integrate an NLP model OpenAI GPT.

## Prerequisites

Before setting up the tool, ensure you have:

- Python 3.7 or newer

## Setup Guide

### 1. Clone the Repository

Download the project to your local system:

```sh
git clone [https://github.com/your-username/web-content-qa-tool.git](https://github.com/anilpankaj/Web-Content-Q-A-Tool.git)
cd web-content-qa-tool
```

### 2. Create a Virtual Environment

Set up and activate a virtual environment:

```sh
python -m venv myenv
source myenv/bin/activate  # For Windows: myenv\Scripts\activate
```

### 3. Install Dependencies

Install the necessary Python packages:

```sh
pip install -r requirements.txt
```

## Running the Application

### 1. Start the FastAPI Server

Use the following command to launch the server:

```sh
uvicorn main:app --reload
```

The application will be available at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

The `--reload` flag enables automatic reloading when you modify the code.

### 2. Access the Web Interface

Open your browser and visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/). You will find these options:

#### Web Content Q&A Tool

- **Enter URLs (one per line)**: Provide one or more URLs to extract their content.
- **Ask a question**: Submit questions based on the extracted content.

## How to Use

### Ingest URLs

1. Enter one or more URLs in the textarea (one URL per line).
2. Click **Ingest Content**.
3. The tool will scrape the content from the provided URLs and store it for Q&A.

### Ask Questions

1. Enter a question in the input field.
2. Click **Get Answer**.
3. The tool will search the ingested content and display a concise answer.

## Acknowledgments
- Built with FastAPI.
- Uses BeautifulSoup for web scraping.

---

Enjoy using the Web Content Q&A Tool!

