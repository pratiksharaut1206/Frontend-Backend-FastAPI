from fastapi import FastAPI
from pydantic import BaseModel  ## <--- Importing BaseModel from Pydantic which is used for data validation and settings management

## Create FastAPI instance
app = FastAPI()


## Create pydantic model which defines the structure of the data
## We have to define the request body i.e. what json structure we expect
class UserRequest(BaseModel):
    name: str  ## Validation: name should be string

## Get API - return a simple message. 
## Get is used to fetch the data
@app.get("/hello")
def hello():
    return {"message": "Hello from the FastAPI backend!"}  ## Function executed when endpoint is called

## POST API- creates post endpoint
## Post is used to send data to backend
@app.post("/greet")
def greet_user(user: UserRequest):
    username = user.name  ## Accessing the name from the request body

    message = f"Hello, {username}! Welcome to the FastAPI backend!"  ## Logic: Creating a personalized message

    return {"response": message}