from fastapi import FastAPI, Request
from env import EmailSupportEnv

app = FastAPI()
env = EmailSupportEnv()

@app.get("/")
def home():
    return {"status": "running"}

@app.post("/step")
async def step(request: Request):
    # SAFE BODY PARSING (fixes NoneType crash)
    try:
        payload = await request.json()
    except:
        payload = {}

    # SAFETY: ensure dict
    if payload is None:
        payload = {}

    action = payload.get("action", "")

    result = env.step(action)

    # FINAL SAFETY CHECK
    if not result or len(result) != 4:
        return {
            "error": "Invalid env response",
            "debug": str(result)
        }

    observation, reward, done, info = result

    return {
        "observation": observation,
        "reward": reward,
        "done": done,
        "info": info
    }