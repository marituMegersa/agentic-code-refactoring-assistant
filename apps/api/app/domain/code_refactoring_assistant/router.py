from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.domain.code_refactoring_assistant.schemas import AgenticCodeRefactoringAssistantSessionCreate, AgenticCodeRefactoringAssistantSessionResponse
from app.domain.code_refactoring_assistant.service import AgenticCodeRefactoringAssistantService

router = APIRouter(prefix="/api/v1/code_refactoring_assistant", tags=["Agentic Code Refactoring Assistant Domain"])

@router.post("/sessions", response_model=AgenticCodeRefactoringAssistantSessionResponse, status_code=status.HTTP_201_CREATED)
def create_domain_session(data: AgenticCodeRefactoringAssistantSessionCreate, db: Session = Depends(get_db)):
    """
    Creates a new FastAPI domain session for Agentic Code Refactoring Assistant.
    """
    return AgenticCodeRefactoringAssistantService.create_session(db, data)

@router.get("/sessions/{session_id}", response_model=AgenticCodeRefactoringAssistantSessionResponse)
def get_domain_session(session_id: str, db: Session = Depends(get_db)):
    obj = AgenticCodeRefactoringAssistantService.get_session(db, session_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Domain session not found")
    return obj
