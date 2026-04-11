class EmailSupportEnv:
    def __init__(self):
        self.reset()

    def reset(self):
        self.data = [
            {"email": "I want refund", "label": "billing"},
            {"email": "App not working", "label": "tech"},
            {"email": "Payment failed", "label": "billing"}
        ]
        self.index = 0
        return self.data[0]

    def step(self, action):
        # safety: ensure string input
        if action is None:
            action = ""
        if not isinstance(action, str):
            action = str(action)

        # reset if index out of range
        if self.index >= len(self.data):
            self.reset()

        current = self.data[self.index]
        correct = current["label"]

        reward = 1.0 if action == correct else 0.0

        self.index += 1
        done = self.index >= len(self.data)

        observation = self.data[self.index] if not done else current

        return observation, reward, done, {}

    def state(self):
        return {"index": self.index}