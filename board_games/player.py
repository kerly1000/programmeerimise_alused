"""Player class."""

class Player:
    """Player class."""

    def __init__(self, name: str):
        self.__name = name
        self.__games = []


    def get_played_game_amount(self) ->int:
        """Return the amount of game played.

        "/player/{name}/amount"  tagastab int-i, mis kirjeldab, mitu mängu on mängija
        nimega player_name mänginud
        """
        return len(self.__games)

    def get_favourite_game_name(self) -> str:
        """
        "/player/{name}/favourite" - tagastab mängu (str, kus on mängu nimi), mida mängija
        nimega player_name on enim mänginud
        """
        pass

    def get_won_game_count(self) -> int:
        """
        return the number on games won.
        "/player/{name}/won" tagastab int-i, mis kirjeldab, mitu mängu mängija nimega
        player_name on võitnud
        """
        pass

    def get_name(self):

        return self.__name