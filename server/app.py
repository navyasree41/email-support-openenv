from fastapi import FastAPI, Request
import sys
import os

# ensure root path is accessible (fix HF import issues)
sys.path.append(os.path.abspath("."))

from env import EmailSupportEnv

app = FastAPI()

env = EmailSupportEnv()


@app.get("/")
def home():
    return {"status": "Email Support OpenEnv running"}


@app.post("/reset")
def reset():
    return env.reset()


@app.post("/step")
async def step(request: Request):
    """
    Safe HF-compatible endpoint:
    - prevents None payload crashes
    - ensures JSON safety
    """

    try:
        payload = await request.json()
    except:
        payload = {}

    if not isinstance(payload, dict):
        payload = {}

    action = payload.get("action", "")
    if action is None:
        action = ""

    observation, reward, done, info = env.step(action)

    return {
        "observation": observation,
        "reward": reward,
        "done": done,
        "info": info
    }