from dataclasses import dataclass

@dataclass
class Location:
    name: str
    longtitude: float = 0.0
    latitude: float = 0.0

@dataclass
class City(Location):
    country: str  # Does NOT work
