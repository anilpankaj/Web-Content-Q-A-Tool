import openai

# Set your OpenAI API key
openai.api_key = "your-openai-api-key"

def answer_question(content: str, question: str) -> str:
    try:
        # Use OpenAI GPT to answer the question
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"Context: {content}\n\nQuestion: {question}\n\nAnswer:"}
            ]
        )
        return response.choices[0].message["content"].strip()
    except Exception as e:
        return f"Error generating answer: {str(e)}"