from typing import List, Dict
from src.chess.repositories.lichess_repository import LichessRepository
from src.chess.models import Player, RatingHistory
from datetime import datetime, timedelta
import csv
import os

class ChessService:

    @staticmethod
    def get_top_50_classical_players() -> List[Player]:
        """
        Retorna a lista dos usernames dos top 50 jogadores de xadrez clássico.
        """
        return LichessRepository.get_top_classical_players()

    @staticmethod
    def print_last_30_day_rating_for_top_player() -> Dict:
        """
        Retorna o histórico de rating dos últimos 30 dias para o top 1 jogador.
        """
        top_player = LichessRepository.get_top_classical_players(count=1)
        if not top_player:
            return "Top player not found"
        return top_player[0],ChessService.get_last_30_days_ratings(top_player[0])

    @staticmethod
    def get_last_30_days_ratings(username, last_30_days=None) -> Dict:
        """
        Retorna o histórico de rating dos últimos 30 dias para um jogador específico.
        """
        today = datetime.today()
        if not last_30_days:
            last_30_days = [(today - timedelta(days=i)).strftime('%Y-%m-%d') for i in range(29, -1, -1)]

        ratings = LichessRepository.get_player_rating_history(username)
        if not ratings:
            return {}

        last_30_days_ratings = {}
        for record in ratings:
            year, month, day, rating = record
            date = datetime(year, month + 1, day).strftime('%Y-%m-%d')
            if date in last_30_days:
                last_30_days_ratings[date] = rating

        # Preenche os dias que não tiveram alterações com o último valor conhecido
        filled_ratings = {}
        last_rating = None
        for date in last_30_days:
            if date in last_30_days_ratings:
                last_rating = last_30_days_ratings[date]
            filled_ratings[date] = last_rating if last_rating is not None else ""
        return filled_ratings

    @staticmethod
    def generate_rating_csv_for_top_50_classical_players(filename="top_50_classical_players_ratings.csv"):
        """
        Gera um arquivo CSV contendo o histórico de rating dos últimos 30 dias dos top 50 jogadores.
        """
        top_players = LichessRepository.get_top_classical_players()
        if not top_players:
            return "Unable to retrieve top 50 players list."

        today = datetime.today()
        last_30_days = [(today - timedelta(days=i)).strftime('%Y-%m-%d') for i in range(29, -1, -1)]

        csv_data = [['username'] + last_30_days]

        for player in top_players:
            player_ratings = ChessService.get_last_30_days_ratings(player, last_30_days)
            row = [player] + [player_ratings.get(date, "") for date in last_30_days]
            csv_data.append(row)

        output_dir = "output"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        output_filepath = os.path.join(output_dir, filename)
        with open(output_filepath, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(csv_data)
