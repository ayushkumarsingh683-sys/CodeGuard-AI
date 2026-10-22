import os
from dotenv import load_dotenv
from groq import Groq
import json
from backend.prompts import CODE_REVIEW_SYSTEM_PROMPT

load_dotenv()
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def analyze_code_with_ai(code_snippet: str):
    try:
        response = client.chat.completions.create(
            model="openai/gpt-oss-120b",  # Exact model ID from Groq playground
            messages=[
                {"role": "system", "content": CODE_REVIEW_SYSTEM_PROMPT},
                {"role": "user", "content": f"Please review and fix this code:\n\n{code_snippet}"}
            ],
            response_format={"type": "json_object"}
        )
        
        result = json.loads(response.choices[0].message.content)
        return result
    except Exception as e:
        return {
            "bugs_found": [f"Error during AI analysis: {str(e)}"],
            "explanation": "Failed to connect to AI model or parse response.",
            "fixed_code": code_snippet
        }