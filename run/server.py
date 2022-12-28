from fastapi import FastAPI
import crawler

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/search/")
def home(query):
    return crawler.search(query)
