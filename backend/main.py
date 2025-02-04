from typing import Union

from fastapi import FastAPI

app = FastAPI()
app.title="fifa analisis"

@app.get("/",tags=['home'])
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

jugador1={
    "id":1,
    "nombre": "leo messi",
    "media": 91

}

app.get("/jugador")


@app.get("/productos/{id_prod}",tags=['pag2'])
def productos(id_prod: int):
    return{"el producto": id_prod}
