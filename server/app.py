from fastapi import FastAPI
from env import EmailSupportEnv

app = FastAPI()
env = EmailSupportEnv()

@app.get("/")
def home():
    return {"status": "running"}

@app.post("/step")
def step(payload: dict):
    action = payload.get("action", "")
    return dict(zip(
        ["observation", "reward", "done", "info"],
        env.step(action)
    ))