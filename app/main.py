from typing import Union,Dict
from fastapi import FastAPI

app : FastAPI = FastAPI()

@app.get('/')
def read_root()-> Dict[str,str]:
    return {'Hello': 'World'}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[None,str] = None):
    return {"item_id": item_id, "q" : q}