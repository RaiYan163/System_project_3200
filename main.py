from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

students = {
    1: {
        "name" : "raiyan",
        "age" : 23,
        "year": "3rd year"
    },

    2: {
        "name" : "Ashraf",
        "age": 24,
        "year": "3rd Year",
        }
}

class Student(BaseModel):
    name: str
    age: int
    year: str

class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[str] = None
    year: Optional[str] = None


@app.get("/")
def index():
    return {"name": "First Data"}

@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path()):
    return students[student_id] 

@app.get("/get-by-name/{student_id}")
def get_student(*, student_id: int, name: Optional[str]= None, test : int):
    for student_id in students:
        if students[student_id]["name"] == name and students[student_id]["age"] == test:
            return students[student_id]
    return {"Data" : "Not Found"}

@app.post("/create-student/{student_id}")
def create_student(student_id: int, student : Student):
    if student_id in students:
        return {"Error": "Student Exists"}
    
    students[student_id] = student
    return students[student_id]

@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in students:
        return {"Error": "Student does not exist"}
    
    students[student_id] = student
    return students[student_id]



