from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from agent import run_agent
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Query(BaseModel):
    message: str

@app.post("/chat")
def chat(query: Query):
    response = run_agent(query.message)
    return {"response": response}
