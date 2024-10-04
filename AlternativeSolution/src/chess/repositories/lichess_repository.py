import requests
from src.chess.core.config import settings

class LichessRepository:
    BASE_URL = settings.LICHESS_API_BASE_URL

    @staticmethod
    def get_top_classical_players(count=50):
        """
        Retorna uma lista com os usernames dos top `count` jogadores de xadrez clássico.
        """
        url = f"{LichessRepository.BASE_URL}/player/top/{count}/classical"
        response = requests.get(url)
        if response.status_code == 200:
            players = response.json()
            allTop50Users = players['users']
            return [player['username'] for player in allTop50Users]
        else:
            print(f"Erro ao buscar jogadores: {response.status_code}")
            return []

    @staticmethod
    def get_player_rating_history(username):
        """
        Retorna o histórico de rating de um jogador específico.
        """
        url = f"{LichessRepository.BASE_URL}/user/{username}/rating-history"
        response = requests.get(url)
        if response.status_code == 200:
            rating_history = response.json()
            # Encontrar a seção 'classical' no histórico de rating
            for history in rating_history:
                if history['name'].lower() == 'classical':
                    return history['points']
        print(f"Erro ao buscar histórico de rating para {username}: {response.status_code}")
        return []
