from fastapi import FastAPI, Request
from server.env import EmailSupportEnv

app = FastAPI()

env = EmailSupportEnv()


@app.get("/")
def home():
    return {"status": "running"}


@app.post("/step")
async def step(request: Request):
    try:
        payload = await request.json()
    except:
        payload = {}

    action = payload.get("action", "")

    obs, reward, done, info = env.step(action)

    return {
        "observation": obs,
        "reward": reward,
        "done": done,
        "info": info
    }