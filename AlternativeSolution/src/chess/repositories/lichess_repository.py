import requests
from src.chess.core.config import settings

class LichessRepository:
    BASE_URL = settings.LICHESS_API_BASE_URL

    @staticmethod
    def get_top_classical_players(count=50):
        """
        Returns a list of usernames of the top `count` classical chess players.
        """
        url = f"{LichessRepository.BASE_URL}/player/top/{count}/classical"
        response = requests.get(url)
        if response.status_code == 200:
            players = response.json()
            allTop50Users = players['users']
            return [player['username'] for player in allTop50Users]
        else:
            print(f"Error searching for players: {response.status_code}")
            return []

    @staticmethod
    def get_player_rating_history(username):
        """
        Returns the rating history of a specific player.
        """
        url = f"{LichessRepository.BASE_URL}/user/{username}/rating-history"
        response = requests.get(url)
        if response.status_code == 200:
            rating_history = response.json()
            # Finding the 'classical' section in the rating history
            for history in rating_history:
                if history['name'].lower() == 'classical':
                    return history['points']
        print(f"Error fetching rating history for {username}: {response.status_code}")
        return []
