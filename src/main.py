from fastapi import FastAPI
from Entity.DirectMessage import DirectMessage as DirectMessageModel

app = FastAPI()

@app.post("/sendDirectMessage")
async def sendDirectMessage(directMessage: DirectMessageModel):
    return directMessage
