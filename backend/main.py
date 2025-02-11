from typing import Union
from fastapi import FastAPI
from modelsDB.players import Jugador
from sqlmodel import Field, SQLModel, create_engine, Session, select
from typing import Optional


app = FastAPI()

#Database connection
engine=create_engine("mysql+pymysql://genarodesarrollo:password@localhost:3306/fifa_male_players")
SQLModel.metadata.create_all(engine)


#1-listado de jugadores, paginado.
@app.get("/jugadores")
def jugadores():
    with Session(engine) as session:
        consulta=select(Jugador).limit(5).offset(2) #se puede hacer paginacion con esto
        resultados=session.exec(consulta).all()
        return resultados

#2- Crear endpoint y pantalla que devuelva los detalles de un jugador específico, dado su ID e implementar algun grafico para mostrar sus skills (Hint: pueden utilizar
numero : int =161587
@app.get("/jugadorEspecifico/{id_jugador}")
def jugador_especifico(id_jugador: int):
    with Session(engine) as session:
        statement=select(Jugador.id, 
                         Jugador.long_name,
                         Jugador.age
                         ).where (Jugador.id==id_jugador)
        resultados=session.exec(statement).first()
        return {
            "id": resultados.id,
            "long_name": resultados.long_name,
            "age": resultados.age,
        }
    
class JugadorUpdate(SQLModel):
    long_name: Optional[str]= None

#3-Crear endpoint y pantalla que permita modificar la información de un jugado
@app.patch("/editarJugador/{numero}")
def editarJugador(numero: int, datos:JugadorUpdate):
    with Session(engine) as session:
        
        jugador=session.get(Jugador, numero)

        jugador.long_name=datos.long_name


        session.add(jugador)
        session.commit()
        session.refresh(jugador)

        return({"mensaje": "jugador actulizado", "jugador":jugador})
    

@app.delete("/borrarJugador/{id_jugador}")
def borrarJugador(id_jugador: int):
    with Session(engine) as session:
        sentencia=select(Jugador).where(Jugador.id==id_jugador)
        resultado=session.exec(sentencia)
        jugadorSeleccionado=resultado.one()

        session.delete(jugadorSeleccionado)
        session.commit()
        return {"jugador eliminado": jugadorSeleccionado}
    
class DatosJugador(SQLModel):
    long_name: str
    club_name: str
    age: int


#4-Crear un endpoint que te permita crear un jugador
@app.post("/crearJugador")
def crearJugador(datos: DatosJugador):
    with Session(engine) as session:

        jugador = Jugador(**datos.dict())
        session.add(jugador)
        session.commit()
        session.refresh(jugador)

        return {"Jugador creado": jugador}

#5-Crear un Login para solo ver la info de forma autenticada

        