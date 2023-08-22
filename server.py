from fastapi import FastAPI, Depends, APIRouter
from pydantic import BaseModel
from sqlalchemy.orm import Session

from dependency import get_db, get_query_engine
from model import Club
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
router = APIRouter()


class ClubResponse(BaseModel):
    club_id: int


@router.get("/clubs/")
async def list_clubs(db: Session = Depends(get_db)):
    clubs = db.query(Club).all()
    return clubs


@router.get("/clubs/query/")
async def list_clubs(
    query: str,
    query_engine: Session = Depends(get_query_engine),
):
    response = query_engine.query(query)
    result = response.metadata["result"]
    return {
        "response_text": str(response),
        # "result": result,
    }


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run('server:app', host="127.0.0.1", port=8000, reload=True)
