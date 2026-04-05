def price_converter(price_kws: float) ->float:
    """Convert electricity price from s/kwh to eur/mwh"""
    price_kws = input("Sisesta elektri hind sentides: ")
    price_mwh = float(price_kws) * 1000
    return price_mwh


def banner(slogan: str) -> str:
    return slogan.upper()


if __name__ == '__main__':
    repeat_count =int(input("Mitu korda soovid sloganit korrata? "))
    slogan = input("Milline on sinu slogan? ")
    banner_text = banner(slogan)
    print(f"{banner_text}\n" * repeat_count)


 def party_budget(guests: int) -> int:
     """Calculate party budget. Place rental 55 euros + 10 per guest."""
     place_rent = 55
     cost_per_guest = 10
     return place_rent + cost_per_guest * guests

 if __name__ == '__main__':
     invited_guests = int(input("Mitu inimest on kutsutud? "))
     confirmed_guests = int(input("Mitu inimest tuleb? "))
     min_budget = party_budget(confirmed_guests)
     max_budget = party_budget(invited_guests)
     print(f"Maksimaalne eelarve on {max_budget} eurot")
     print(f"Minimaalne eelarve on {min_budget} eurot")
