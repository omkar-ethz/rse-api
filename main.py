from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="RSE Talk Q&A API", description="A simple demo API written with FastAPI / Python")

# As it's a public API, allow cross origin request
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


# --- Models (These generate the OpenAPI schema) ---
class QuestionCreate(BaseModel):
    text: str


class Question(BaseModel):
    id: int
    text: str
    upvotes: int = 0


# --- In-Memory Database ---
db: list[Question] = []
current_id = 1


# --- Endpoints ---
@app.get("/questions")
async def get_questions() -> list[Question]:
    """Fetch all questions, sorted by upvotes."""
    return sorted(db, key=lambda q: q.upvotes, reverse=True)


@app.post("/questions")
async def ask_question(question_in: QuestionCreate) -> Question:
    """Submit a new question."""
    global current_id
    new_q = Question(id=current_id, text=question_in.text)
    db.append(new_q)
    current_id += 1
    return new_q


@app.patch("/questions/{q_id}/upvote")
async def upvote(q_id: int) -> Question:
    """Add +1 to a specific question."""
    for q in db:
        if q.id == q_id:
            q.upvotes += 1
            return q
    raise HTTPException(status_code=404, detail="Question not found")
