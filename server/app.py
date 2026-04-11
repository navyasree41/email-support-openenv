from fastapi import FastAPI
from env import EmailSupportEnv

app = FastAPI()
env = EmailSupportEnv()

@app.get("/")
def home():
    return {"status": "running"}

@app.post("/step")
def step(payload: dict = None):
    if not payload:
        payload = {}

    action = payload.get("action", "")

    obs, reward, done, info = env.step(action)

    return {
        "observation": obs,
        "reward": reward,
        "done": done,
        "info": info
    }