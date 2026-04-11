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
        if not self.data:
            self.reset()

        if self.index >= len(self.data):
            self.reset()

        current = self.data[self.index]
        correct = current["label"]

        reward = 1.0 if action == correct else 0.0

        self.index += 1
        done = self.index >= len(self.data)

        observation = self.data[self.index] if not done else current

        return observation, reward, done, {}