from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, Field
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    try:
        db = SessionLocal()
        print("Connected to DB successfully")
        yield db
    finally:
        db.close()

# Seed data
SEED_DATA = [
    {
        "reminder": True,
        "text": "Doctor's Appointment",
        "day": "March 1st at 2.30PM"
    },
    {
        "reminder": False,
        "text": "Meeting at School",
        "day": "March 3rd at 1.30PM"
    },
    {
        "reminder": True,
        "text": "Food Shopping",
        "day": "March 16th at 11.00AM"
    }
]

# Function to seed data on startup
@app.on_event("startup")
def seed_data():
    db = SessionLocal()
    try:
        if not db.query(models.Tasks).first():
            for task in SEED_DATA:
                task_model = models.Tasks(
                    text=task["text"],
                    day=task["day"],
                    reminder=task["reminder"]
                )
                db.add(task_model)

            db.commit()
        print("Seeded DB successfully")
    finally:
        db.close()

class Task(BaseModel):
    text: str = Field(min_length=1)
    day: str = Field(min_length=1, max_length=100)
    reminder: bool = Field(default=False)

@app.get("/")
def read_api(db: Session = Depends(get_db)):
    return db.query(models.Tasks).all()


@app.post("/")
def create_task(task: Task, db: Session = Depends(get_db)):

    task_model = models.Tasks()
    task_model.text = task.text
    task_model.day = task.day
    task_model.reminder = task.reminder

    db.add(task_model)
    db.commit()

    return task


@app.put("/{task_id}")
def update_task(task_id: int, task: Task, db: Session = Depends(get_db)):

    task_model = db.query(models.Tasks).filter(models.Tasks.id == task_id).first()

    if task_model is None:
        raise HTTPException(
            status_code=404,
            detail=f"ID {task_id} : Does not exist"
        )

    task_model.text = task.text
    task_model.day = task.day
    task_model.reminder = task.reminder

    db.add(task_model)
    db.commit()

    return task


@app.delete("/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):

    task_model = db.query(models.Tasks).filter(models.Tasks.id == task_id).first()

    if task_model is None:
        raise HTTPException(
            status_code=404,
            detail=f"ID {task_id} : Does not exist"
        )

    db.query(models.Tasks).filter(models.Tasks.id == task_id).delete()

    db.commit()
