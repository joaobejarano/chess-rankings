import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from chess.services.chess_service import ChessService

def main():
    # PART 1
    ChessService.print_top_50_classical_players()

    # PART 2
    ChessService.print_last_30_day_rating_for_top_player()

    # PART 3
    ChessService.generate_rating_csv_for_top_50_classical_players()

if __name__ == '__main__':
    main()
