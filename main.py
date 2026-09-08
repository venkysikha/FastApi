from fastapi import FastAPI

app = FastAPI(
    title="My Enterprise Application",
    description= "An enterpris level application built with FastApi"
)

@app.get("/")
async def root():
    return {"message":"welcome to enterprise application"}

