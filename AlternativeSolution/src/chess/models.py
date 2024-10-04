from pydantic import BaseModel
from typing import List, Optional

# Model to represent a chess player
class Player(BaseModel):
    username: str
    rating: int
    rank: Optional[int] = None

# Model to represent a player's rating history
class RatingHistory(BaseModel):
    date: str
    rating: int

# Model to represent the response with the list of top players
class TopPlayersResponse(BaseModel):
    top_50_players: List[Player]

# Model to represent the response with the rating history of the top 1 player
class TopPlayerRatingHistoryResponse(BaseModel):
    username: str
    rating_history: List[RatingHistory]

# Template to represent CSV generation response
class CSVGenerationResponse(BaseModel):
    message: str
