from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from typing import List
from app.core.ai_agent import get_response_from_ai_agents
from app.config.settings import settings
from app.common.logger import get_logger
from app.common.custom_exception import CustomException

logger = get_logger(__name__)

app = FastAPI(title="MULTI AI AGENT")

class RequestState(BaseModel):
    model_name:str
    system_prompt:str
    messages:List[str]
    allow_search: bool

@app.post("/chat")
async def chat_endpoint(request: RequestState):
    try:
        ai_response = get_response_from_ai_agents(
            llm_id=request.model_name,
            messages=request.messages,         # updated
            allow_search=request.allow_search,
            system_prompt=request.system_prompt
        )
        return {"response": ai_response}
    except Exception as e:
        import traceback
        traceback.print_exc()
        return {"detail": f"Failed to get AI response | Error: {str(e)}"}

