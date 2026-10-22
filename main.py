from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from backend.agents import analyze_code_with_ai

app = FastAPI(title="AI Code Reviewer & Bug Fixing Agent")

# Enable CORS for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class CodeRequest(BaseModel):
    code: str

@app.get("/")
def home():
    return {"message": "AI Code Reviewer API is running successfully!"}

@app.post("/api/review")
def review_code(request: CodeRequest):
    if not request.code.strip():
        raise HTTPException(status_code=400, detail="Code snippet cannot be empty")
    
    analysis_result = analyze_code_with_ai(request.code)
    return analysis_result