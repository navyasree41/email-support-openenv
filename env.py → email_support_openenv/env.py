class EmailEnv:
    def __init__(self):
        self.data = []
        self.index = 0

    def reset(self):
        self.data = [
            {"email": "I want refund", "label": "billing"},
            {"email": "App not working", "label": "tech"},
            {"email": "Payment failed", "label": "billing"}
        ]
        self.index = 0
        return self.data[self.index]

    def step(self, action):
        if self.index >= len(self.data):
            return {}, 0.0, True, {}

        correct = self.data[self.index]["label"]

        reward = 1.0 if action == correct else 0.0

        self.index += 1

        if self.index >= len(self.data):
            return {}, reward, True, {}

        return self.data[self.index], reward, False, {}

    def state(self):
        return {"index": self.index}
