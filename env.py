from fastapi import FastAPI, Request
from env import EmailSupportEnv

app = FastAPI()

# initialize environment
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
    SAFE VERSION:
    - prevents None payload crash
    - handles invalid JSON
    - ensures action always exists
    """

    # Default safe payload
    payload = {}

    try:
        payload = await request.json()
        if payload is None:
            payload = {}
    except Exception:
        payload = {}

    # Extract action safely
    action = payload.get("action", "")
    if action is None:
        action = ""

    # Call environment safely
    observation, reward, done, info = env.step(action)

    return {
        "observation": observation,
        "reward": reward,
        "done": done,
        "info": info
    }