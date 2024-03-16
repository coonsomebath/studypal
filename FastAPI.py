from fastapi import FastAPI 
import random

app = FastAPI()

@app.get('/')
async def root():
    return{'cards?':'Flashcards','data':0}
    