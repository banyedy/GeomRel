import openai  # Or any other local model inference library

# Set your OpenAI API key
openai.api_key = 'your-api-key-here'

def chat(prompt: str, model="gpt-4"):
    """
    Calls a large language model for inference and returns the generated text.
    You can replace the `openai` call with your own inference library for other models.
    """
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0  # Ensure stable answers
        )
        return response["choices"][0]["message"]["content"].strip()
    except openai.error.OpenAIError as e:
        print(f"OpenAI error occurred: {e}")
        return ""
    except Exception as e:
        print(f"Unexpected error occurred: {e}")
        return ""
