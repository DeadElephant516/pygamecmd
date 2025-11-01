import pygame


bg_1 = pygame.image.load("assets/background1.jpg")
bg_2 = pygame.image.load("assets/background2.jpg")
bg_3 = pygame.image.load("assets/background3.jpg")
bg_4 = pygame.image.load("assets/background4.jpg")
bg_5 = pygame.image.load("assets/background5.jpg")
bg_6 = pygame.image.load("assets/background6.jpg")


areas = {
    "area_a": {
        "description": "first test room",
        "image" : bg_1,
        "area" : "test zone",
        "exits": {"east": "area_b"},
        "items": ["hp_pot", "atk_pot"],
        "enemy": None,
    },
    "area_b": {
        "description": "second test room",
        "image" : bg_2,
        "area" : "test zone",
        "exits": {"west": "area_a", "south": "area_c"},
        "items": ["dagger"],
        "enemy": None,
    },
    "area_c": {
        "description": "third test room",
        "image" : bg_3,
        "area" : "test zone",
        "exits": {"north": "area_b", "south": "area_d"},
        "items": [],
        "enemy": None,
    },
    "area_d": {
        "description": "the fourth place",
        "image" : bg_4,
        "exits": {"north": "area_c", "east": "area_e"},
        "items": [],
        "enemy": None,
    },
    "area_e": {
        "description": "another test place",
        "image" : bg_5,
        "area" : "test zone 2",
        "exits": {"west": "area_d", "south": "area_f"},
        "items": [],
        "enemy": None,
    },
    "area_f": {
        "description": "you know how it goes really",
        "image" : bg_6,
        "area" : "test zone 2",
        "exits": {"north": "area_e"},
        "items": [],
        "enemy": None,
    }
}

