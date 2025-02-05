from typing import Union
from fastapi import FastAPI
from modelsDB.players import Jugador
from sqlmodel import Field, SQLModel, create_engine, Session, select
from typing import Optional


app = FastAPI()

#Database connection
engine=create_engine("mysql+pymysql://genarodesarrollo:password@localhost:3306/fifa_male_players")
SQLModel.metadata.create_all(engine)

@app.get("/",tags=['home'])
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}



@app.get("/productos/{id_prod}",tags=['pag2'])
def productos(id_prod: int):
    return{"el producto": id_prod}


@app.get("/jugadores")
def mostar_jugadores():
    with Session(engine) as session:
        statement=select(Jugador.id, 
                         Jugador.long_name,
                         Jugador.age
                         ).where (Jugador.long_name=="Cristiano Ronaldo dos Santos Aveiro")
        resultados=session.exec(statement).first()
        return {
            "id": resultados.id,
            "long_name": resultados.long_name,
            "age": resultados.age,
        }
        