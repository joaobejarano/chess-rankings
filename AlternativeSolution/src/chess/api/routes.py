from fastapi import APIRouter, HTTPException
from src.chess.services.chess_service import ChessService

router = APIRouter()

# Route to get the list of top 50 classical chess players
@router.get("/top_50_classical_players")
def get_top_50_classical_players():
    try:
        list_top_players = ChessService.get_top_50_classical_players()
        return {"top_50_players": list_top_players}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Route to get the rating history of the top 1 player for the last 30 days
@router.get("/last_30_day_rating_for_top_player")
def get_top_player_rating_history():
    try:
        usernameTopPlayer, rating_history = ChessService.print_last_30_day_rating_for_top_player()
        return {"top_player":usernameTopPlayer, "top_player_rating_history": rating_history}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Route to generate CSV of top 50 players
@router.post("/rating_csv_for_top_50_classical_players")
def generate_top_50_classical_players_csv():
    try:
        ChessService.generate_rating_csv_for_top_50_classical_players()
        return {"message": "CSV generated successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
