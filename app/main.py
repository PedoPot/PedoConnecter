from fastapi import FastAPI, HTTPException
from app.Entity.DirectMessage import DirectMessage as DirectMessageModel
from contextlib import asynccontextmanager
from app.Entity.Authentication import Authentication
from app.Connector.Connectors import Connectors, ask_connectors

@asynccontextmanager
async def lifespan(app: FastAPI):
    ask_connectors()
    yield

app = FastAPI(lifespan=lifespan)
connectors = Connectors()

@app.post("/sendDirectMessage")
async def send_direct_message(direct_message: DirectMessageModel):
    token = direct_message.token
    user_id = direct_message.user_id
    message = direct_message.message

    connector = connectors.get_connector(token)
    if connector:
        await connector.send_direct_message(user_id, message)
    
    return direct_message

@app.post("/start")
async def start_connector(credentials: Authentication):
    try:
        connector_name = credentials.connector
        token = credentials.token
        
        if connectors.get_connector(token):
            return {"status": "already_running", "message": f"The connector {connector_name} is already running"}
        
        success = await connectors.start_connector_by_name(connector_name, token)
        
        if success:
            return {"status": "success", "message": f"Connector {connector_name} started successfully"}
        else:
            raise HTTPException(status_code=500, detail=f"Impossible to start the connector {connector_name}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to start the connector: {str(e)}")