<<<<<<< HEAD
import requests

BASE = "http://127.0.0.1:8000"

print("[START]")

# Reset
obs = requests.post(f"{BASE}/reset").json()
print("[STEP] Reset:", obs)

done = False
total_reward = 0

while not done:
    email = obs["email"].lower()

    if "refund" in email or "payment" in email:
        action = "billing"
    else:
        action = "tech"

    res = requests.post(f"{BASE}/step", json={"action": action}).json()

    print("[STEP]", res)

    total_reward += res["reward"]
    done = res["done"]
    obs = res["observation"]

=======
import requests

BASE = "http://127.0.0.1:8000"

print("[START]")

# Reset
obs = requests.post(f"{BASE}/reset").json()
print("[STEP] Reset:", obs)

done = False
total_reward = 0

while not done:
    email = obs["email"].lower()

    if "refund" in email or "payment" in email:
        action = "billing"
    else:
        action = "tech"

    res = requests.post(f"{BASE}/step", json={"action": action}).json()

    print("[STEP]", res)

    total_reward += res["reward"]
    done = res["done"]
    obs = res["observation"]

>>>>>>> 8184471 (initial commit)
print("[END] Total Reward:", total_reward)