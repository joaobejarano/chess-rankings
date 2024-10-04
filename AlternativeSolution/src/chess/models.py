from pydantic import BaseModel
from typing import List, Optional

# Modelo para representar um jogador de xadrez
class Player(BaseModel):
    username: str
    rating: int
    rank: Optional[int] = None

# Modelo para representar o histórico de rating de um jogador
class RatingHistory(BaseModel):
    date: str
    rating: int

# Modelo para representar a resposta com a lista dos top jogadores
class TopPlayersResponse(BaseModel):
    top_50_players: List[Player]

# Modelo para representar a resposta com o histórico de rating do top 1 jogador
class TopPlayerRatingHistoryResponse(BaseModel):
    username: str
    rating_history: List[RatingHistory]

# Modelo para representar a resposta de geração de CSV
class CSVGenerationResponse(BaseModel):
    message: str
