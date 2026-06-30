from fastapi import FastAPI
app=FastAPI()

@app.get("/")
def hello():
    return {'message':'hello ji'}

@app.get('/2')
def hello2():
    return {'message':'hello ji2'}