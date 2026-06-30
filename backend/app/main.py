from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text
from pydantic import BaseModel
from .database import engine

app = FastAPI(title="Student Management System")

# Allow frontend to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://student-management-system-3g3.pages.dev",
        "http://localhost:5173",
        "http://127.0.0.1:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class StudentCreate(BaseModel):
    roll_no: str
    name: str
    department: str
    year_of_study: int
    email: str
    phone: str

class StudentUpdate(BaseModel):
    name: str | None = None
    department: str | None = None
    year_of_study: int | None = None
    email: str | None = None
    phone: str | None = None

@app.get("/")
def home():
    return {"message": "Student Management API Running"}

@app.get("/students")
def get_students():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM students"))
        return [dict(row._mapping) for row in result]

@app.post("/students")
def create_student(student: StudentCreate):
    with engine.connect() as conn:
        conn.execute(text("""
            INSERT INTO students (roll_no, name, department, year_of_study, email, phone)
            VALUES (:roll_no, :name, :department, :year_of_study, :email, :phone)
        """), student.dict())
        conn.commit()
    return {"message": "Student added successfully"}

@app.get("/students/{student_id}")
def get_student(student_id: int):
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM students WHERE id = :id"), {"id": student_id})
        student = result.fetchone()
        if not student:
            raise HTTPException(status_code=404, detail="Student not found")
        return dict(student._mapping)

@app.put("/students/{student_id}")
def update_student(student_id: int, student: StudentUpdate):
    with engine.connect() as conn:
        update_data = {k: v for k, v in student.dict().items() if v is not None}
        if not update_data:
            return {"message": "No fields to update"}
        
        set_clause = ", ".join([f"{k} = :{k}" for k in update_data.keys()])
        query = text(f"UPDATE students SET {set_clause} WHERE id = :id")
        update_data["id"] = student_id
        conn.execute(query, update_data)
        conn.commit()
    return {"message": "Student updated successfully"}

@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    with engine.connect() as conn:
        result = conn.execute(text("DELETE FROM students WHERE id = :id"), {"id": student_id})
        conn.commit()
        if result.rowcount == 0:
            raise HTTPException(status_code=404, detail="Student not found")
    return {"message": "Student deleted successfully"}
