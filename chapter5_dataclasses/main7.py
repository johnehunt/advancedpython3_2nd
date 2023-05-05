from dataclasses import dataclass

@dataclass
class Location:
    name: str
    longitude: float = 0.0
    latitude: float = 0.0

@dataclass
class City(Location):
    country: str = None  # Does NOT work

city = City('Dublin', country='Ireland')
print(city)