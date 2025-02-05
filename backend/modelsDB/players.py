
from sqlmodel import Field, SQLModel, create_engine, Session, select
from typing import Optional

engine=create_engine("mysql+pymysql://genarodesarrollo:password@localhost:3306/fifa_male_players")
SQLModel.metadata.create_all(engine)


class Jugador(SQLModel, table=True):
    # Configuración de la tabla
    __tablename__ = "players"

    # Campos del modelo
    id: int = Field(default=None, primary_key=True)
    fifa_version: Optional[str] = Field(default=None)
    fifa_update: Optional[str] = Field(default=None)
    player_face_url: Optional[str] = Field(default=None)
    long_name: str
    player_positions: str
    club_name: Optional[str] = Field(default=None)
    nationality_name: Optional[str] = Field(default=None)
    overall: int
    potential: Optional[int] = Field(default=None)
    value_eur: Optional[int] = Field(default=None)
    wage_eur: Optional[int] = Field(default=None)
    age: int
    height_cm: Optional[int] = Field(default=None)
    weight_kg: Optional[int] = Field(default=None)
    preferred_foot: Optional[str] = Field(default=None)
    weak_foot: Optional[int] = Field(default=None)
    skill_moves: Optional[int] = Field(default=None)
    international_reputation: Optional[int] = Field(default=None)
    work_rate: Optional[str] = Field(default=None)
    body_type: Optional[str] = Field(default=None)
    pace: Optional[int] = Field(default=None)
    shooting: Optional[int] = Field(default=None)
    passing: Optional[int] = Field(default=None)
    dribbling: Optional[int] = Field(default=None)
    defending: Optional[int] = Field(default=None)
    physic: Optional[int] = Field(default=None)
    attacking_crossing: Optional[int] = Field(default=None)
    attacking_finishing: Optional[int] = Field(default=None)
    attacking_heading_accuracy: Optional[int] = Field(default=None)
    attacking_short_passing: Optional[int] = Field(default=None)
    attacking_volleys: Optional[int] = Field(default=None)
    skill_dribbling: Optional[int] = Field(default=None)
    skill_curve: Optional[int] = Field(default=None)
    skill_fk_accuracy: Optional[int] = Field(default=None)
    skill_long_passing: Optional[int] = Field(default=None)
    skill_ball_control: Optional[int] = Field(default=None)
    movement_acceleration: Optional[int] = Field(default=None)
    movement_sprint_speed: Optional[int] = Field(default=None)
    movement_agility: Optional[int] = Field(default=None)
    movement_reactions: Optional[int] = Field(default=None)
    movement_balance: Optional[int] = Field(default=None)
    power_shot_power: Optional[int] = Field(default=None)
    power_jumping: Optional[int] = Field(default=None)
    power_stamina: Optional[int] = Field(default=None)
    power_strength: Optional[int] = Field(default=None)
    power_long_shots: Optional[int] = Field(default=None)
    mentality_aggression: Optional[int] = Field(default=None)
    mentality_interceptions: Optional[int] = Field(default=None)
    mentality_positioning: Optional[int] = Field(default=None)
    mentality_vision: Optional[int] = Field(default=None)
    mentality_penalties: Optional[int] = Field(default=None)
    mentality_composure: Optional[int] = Field(default=None)
    defending_marking: Optional[int] = Field(default=None)
    defending_standing_tackle: Optional[int] = Field(default=None)
    defending_sliding_tackle: Optional[int] = Field(default=None)
    goalkeeping_diving: Optional[int] = Field(default=None)
    goalkeeping_handling: Optional[int] = Field(default=None)
    goalkeeping_kicking: Optional[int] = Field(default=None)
    goalkeeping_positioning: Optional[int] = Field(default=None)
    goalkeeping_reflexes: Optional[int] = Field(default=None)
    goalkeeping_speed: Optional[int] = Field(default=None)
    player_traits: Optional[str] = Field(default=None)

def select_players():
    with Session(engine) as session:
        statement=select(Jugador)
        resultados=session.exec(statement).all()
        return resultados
    


select_players()