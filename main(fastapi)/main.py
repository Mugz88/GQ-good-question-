from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"": "gig"}

@app.get("/profile")
def profile():
    return {"": "profile"}