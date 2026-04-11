class EmailEnv:
    def __init__(self):
        self.emails = [
            {"email": "I want refund", "label": "billing"},
            {"email": "Payment failed", "label": "billing"},
            {"email": "App not working", "label": "tech"},
            {"email": "Login issue", "label": "tech"}
        ]
        self.index = 0
        self.current = None

    def reset(self):
        self.index = 0
        self.current = self.emails[self.index]
        return self.current

    def step(self, action):
        # get correct label
        correct_label = self.current["label"]

        # reward logic (FIXED)
        if action == correct_label:
            reward = 1.0
        else:
            reward = 0.0

        # move to next email
        self.index += 1

        # check if done
        if self.index >= len(self.emails):
            done = True
            observation = None
        else:
            done = False
            self.current = self.emails[self.index]
            observation = self.current

        return observation, reward, done, {}
    
    def state(self):
        return self.current