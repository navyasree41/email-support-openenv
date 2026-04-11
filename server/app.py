from fastapi import FastAPI, Request
from server.env import EmailSupportEnv

app = FastAPI()

@app.get("/")
def home():
    return {"status": "running"}

@app.post("/step")
async def step(request: Request):

    # ALWAYS create fresh env (fixes HF state issues)
    env = EmailSupportEnv()

    payload = await request.json()
    action = payload.get("action", "")

    observation, reward, done, info = env.step(action)

    return {
        "observation": observation,
        "reward": reward,
        "done": done,
        "info": info
    }