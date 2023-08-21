# simple example of fastapi with get , post and delete methods

from fastapi import FastAPI, HTTPException

app = FastAPI()

# create a list of dictionaries to store the data
students = [
    {
        "id": 1,
        "name": "john",
        "age": 17,
        "year": "year 12"
    },
    {
        "id": 2,
        "name": "jane",
        "age": 16,
        "year": "year 11"
    }
]


# get method to get all the students
@app.get("/students")
async def get_students():
    return students


# get method to get a student by id
@app.get("/students/{student_id}")
async def get_student(student_id: int):
    for student in students:
        if student["id"] == student_id:
            return student
    raise HTTPException(status_code=404, detail="student not found")


# post method to add a student
@app.post("/students")
async def add_student(student: dict):
    students.append(student)
    return students[-1]


# delete method to delete a student by id
@app.delete("/students/{student_id}")
async def delete_student(student_id: int):
    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            return {"message": "student deleted successfully"}
    raise HTTPException(status_code=404, detail="student not found")

# unvcon command to run the app
# uvicorn main:app --reload

