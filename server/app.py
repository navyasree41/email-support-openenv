from fastapi import FastAPI, Request
from env import EmailSupportEnv

app = FastAPI()
env = EmailSupportEnv()

@app.get("/")
def home():
    return {"status": "running"}

@app.post("/step")
async def step(request: Request):

    # STEP 1: SAFE RAW BODY READ
    body = await request.body()

    try:
        payload = await request.json()
    except:
        payload = {}

    # STEP 2: FORCE DICT SAFETY
    if not isinstance(payload, dict):
        payload = {}

    # STEP 3: EXTRACT ACTION SAFELY
    action = payload.get("action") if payload else None
    if action is None:
        action = ""

    # STEP 4: CALL ENV SAFELY
    result = env.step(action)

    # STEP 5: FINAL SAFETY CHECK
    if result is None or not isinstance(result, tuple) or len(result) != 4:
        return {
            "error": "env.step failure",
            "debug": str(result)
        }

    observation, reward, done, info = result

    return {
        "observation": observation,
        "reward": reward,
        "done": done,
        "info": info
    }