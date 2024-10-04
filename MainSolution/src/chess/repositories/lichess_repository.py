import requests

class LichessRepository:
    BASE_URL = "https://lichess.org/api"

    @staticmethod
    def get_top_classical_players(count=50):
        """
        Returns a list of the usernames of the top 50 classical chess players.
        """
        url = f"{LichessRepository.BASE_URL}/player/top/{count}/classical"
        response = requests.get(url)
        if response.status_code == 200:
            players = response.json()
            allTop50Users = players['users']
            return [player['username'] for player in allTop50Users]
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

            for history in rating_history:
                if history['name'].lower() == 'classical':
                    return history['points']
        print(f"Error fetching rating history for {username}: {response.status_code}")
        return []
