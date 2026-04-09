from fastapi import FastAPI, Body
from env import EmailEnv

app = FastAPI()

# Initialize environment
env = EmailEnv()


# -------- HOME --------
@app.get("/")
def home():
    return {"message": "Email Support OpenEnv is running"}


# -------- RESET --------
@app.post("/reset")
def reset():
    return env.reset()


# -------- STEP (FINAL SAFE VERSION) --------
@app.post("/step")
def step(data=Body(...)):
    try:
        print("Received:", data)  # debug log

        # Accept both formats safely
        if isinstance(data, dict):
            action = data.get("action", "")
        else:
            action = str(data)

        observation, reward, done, info = env.step(action)

        return {
            "observation": observation,
            "reward": reward,
            "done": done,
            "info": info
        }

    except Exception as e:
        return {"error": str(e)}


# -------- STATE --------
@app.get("/state")
def state():
    return env.state()
