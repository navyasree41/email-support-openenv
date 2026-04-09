from pydantic import BaseModel

class Observation(BaseModel):
    email: str
    urgency: str

class Action(BaseModel):
    action: str  # reply / billing / tech

class StepResult(BaseModel):
    observation: Observation
    reward: float
    done: bool
    info: dict