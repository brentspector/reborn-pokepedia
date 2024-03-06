from configparser import (ConfigParser, MissingSectionHeaderError,
                          ParsingError, DEFAULTSECT)
from string import printable
import json

eventLocations = {
    "Zigzagoon": {
        "location": "Opal Ward",
        "point": "Julia",
        "method": "Bridge Event (50%)"
    },
    "Pachirisu": {
        "location": "Opal Ward",
        "point": "Julia",
        "method": "Bridge Event (50%)"
    },
    "Tynamo": {
        "location": "Lower Peridot Alley",
        "point": "Julia",
        "method": "Thunderstorm Event (100%)"
    },
    "Whismur": {
        "location": "Lower Peridot Ward",
        "point": "Julia",
        "method": "House Pokesnax Event (100%)"
    },
    "Minccino": {
        "location": "Lower Peridot Ward",
        "point": "Julia",
        "method": "$50 Bum Pokesnax Event (25%)"
    },
    "Espurr": {
        "location": "Lower Peridot Ward",
        "point": "Julia",
        "method": "$50 Bum Pokesnax Event (25%)"
    },
    "Swinub": {
        "location": "Lower Peridot Ward",
        "point": "Julia",
        "method": "MonoIce/MonoGround $50 Bum Pokesnax Event (25%)"
    },
    "Aron": {
        "location": "Lower Peridot Ward",
        "point": "Julia",
        "method": "MonoSteel/MonoRock $50 Bum Pokesnax Event (25%)"
    },
    "Teddiursa": {
        "location": "Lower Peridot Ward",
        "point": "Julia",
        "method": "Afternoon Clear Day Hide and Seek (100%)"
    },
    "Kricketot": {
        "location": "Lower Peridot Ward",
        "point": "Julia",
        "method": "House NPC (50%)"
    },
    "Dwebble": {
        "location": "Lower Peridot Ward",
        "point": "Julia",
        "method": "MonoRock House NPC (50%)"
    },
    "Delibird": {
        "location": "Lower Peridot Ward",
        "point": "Julia",
        "method": "Gift Box House Event (100%)"
    },
    "Skitty": {
        "location": "Lower Peridot Ward",
        "point": "Julia",
        "method": "Oran Berry Event (100%)"
    },
    "Blitzle": {
        "location": "Lower Peridot Ward",
        "point": "Julia",
        "method": "Thunderstorm Event Next to Gym (100%)"
    },
    "Gulpin": {
        "location": "Lower Peridot Ward",
        "point": "Julia",
        "method": "Trashcan South of Gym Near Dish Pokesnax (100%)"
    },
    "Pansear": {
        "location": "Lower Peridot Ward",
        "point": "Julia",
        "method": "Rainstorm Event Under Bridge (50%)"
    },
    "Panpour": {
        "location": "Lower Peridot Ward",
        "point": "Julia",
        "method": "Rainstorm Event Under Bridge (50%)"
    },
    "Woobat": {
        "location": "Peridot Underground Railnet",
        "point": "Julia",
        "method": "Dark Spots (100%)"
    },
    "Grubbin": {
        "location": "Peridot Ward",
        "point": "Julia",
        "method": "Nighttime House Pokesnax Event (50%)"
    },
    "Joltik": {
        "location": "Peridot Ward",
        "point": "Julia",
        "method": "Nighttime House Pokesnax Event (50%)"
    },
    "Igglybuff": {
        "location": "Peridot Ward",
        "point": "Julia",
        "method": "House NPC (100%)"
    },
    "Surskit": {
        "location": "Peridot Ward",
        "point": "Julia",
        "method": "Fountain Rainstorm Event (100%)"
    },
    "Budew": {
        "location": "Peridot Ward",
        "point": "Julia",
        "method": "Rose Incense Clear Day Event (100%)"
    },
    "Munna": {
        "location": "Peridot Ward",
        "point": "Julia",
        "method": "Trade Bibarel"
    },
    "Drifloon": [
        {
            "location": "Peridot Ward",
            "point": "Julia",
            "method": "MonoGhost Night Event (100%)"
        },
        {
            "location": "Yureyu Power Plant",
            "point": "Corey",
            "method": "Windy Outside Plant Event (100%)"
        }
    ],
    "Numel": {
        "location": "Lower Peridot Ward",
        "point": "ZEL/Pulse Tangrowth 1",
        "method": "Train Station Rainstorm Event (100%)"
    },
    "Onix": {
        "location": "Lower Peridot Ward",
        "point": "ZEL/Pulse Tangrowth 1",
        "method": "Hiker House Event (100%)"
    },
    "Castform": {
        "location": "Obsidia Ward",
        "point": "ZEL/Pulse Tangrowth 1",
        "method": "Trade Furret"
    },
    "Castform (Sunny Form)": {
        "location": "Obsidia Ward",
        "point": "ZEL/Pulse Tangrowth 1",
        "method": "Trade Furret"
    },
    "Castform (Rainy Form)": {
        "location": "Obsidia Ward",
        "point": "ZEL/Pulse Tangrowth 1",
        "method": "Trade Furret"
    },
    "Castform (Snowy Form)": {
        "location": "Obsidia Ward",
        "point": "ZEL/Pulse Tangrowth 1",
        "method": "Trade Furret"
    },
    "Vanillite": [
        {
            "location": "Obsidia Ward",
            "point": "ZEL/Pulse Tangrowth 1",
            "method": "Candy Shop Vanilla Ice Cream (100%)"
        }, {
            "location": "Spinel Town",
            "point": "Serra",
            "method": "Vending Machine Vanilla Ice Cream (100%)"
        },
        {
            "location": "7th Street",
            "point": "Subseven Sanctum",
            "method": "Purchase (100%)"
        }
    ],
    "Swirlix": {
        "location": "Obsidia Ward",
        "point": "ZEL/Pulse Tangrowth 1",
        "method": "Candy Shop Puzzle (100%)"
    },
    "Bounsweet": {
        "location": "Obsidia Ward",
        "point": "ZEL/Pulse Tangrowth 1",
        "method": "Hair Salon Competition Event (100%)"
    },
    "Glameow": {
        "location": "Obsidia Ward",
        "point": "ZEL/Pulse Tangrowth 1",
        "method": "Hair Salon Competition Event (100%)"
    },
    "Wigglytuff": {
        "location": "Obsidia Slums",
        "point": "ZEL/Pulse Tangrowth 1",
        "method": "Moon Stone"
    },
    "Delcatty": {
        "location": "Obsidia Slums",
        "point": "ZEL/Pulse Tangrowth 1",
        "method": "Moon Stone"
    },
    "Musharna": {
        "location": "Obsidia Slums",
        "point": "ZEL/Pulse Tangrowth 1",
        "method": "Moon Stone"
    },
    "Electrike": {
        "location": "Obsidia Alleyway",
        "point": "Florina",
        "method": "Nighttime Event (100%)"
    },
    "Plusle": {
        "location": "Obsidia Alleyway",
        "point": "Florina",
        "method": "Repeatable Alternating Pokesnax Event (100%)"
    },
    "Minun": {
        "location": "Obsidia Alleyway",
        "point": "Florina",
        "method": "Repeatable Alternating Pokesnax Event (100%)"
    },
    "Litleo": {
        "location": "Obsidia Underground Railnet",
        "point": "Florina",
        "method": "Daytime Obsidia Alleyway Chase Event (100%)"
    },
    "Hoppip": {
        "location": "Obsidia Slums",
        "point": "ZEL/Pulse Tangrowth 1",
        "method": "Windy Weather (100%)"
    },
    "Drowzee": {
        "location": "Obsidia Slums",
        "point": "ZEL/Pulse Tangrowth 1",
        "method": "Egg (33%)"
    },
    "Bronzor": {
        "location": "Obsidia Slums",
        "point": "ZEL/Pulse Tangrowth 1",
        "method": "Egg (33%)"
    },
    "Ducklett": {
        "location": "Obsidia Slums",
        "point": "ZEL/Pulse Tangrowth 1",
        "method": "Egg (33%)"
    },
    "Lotad": {
        "location": "Coral Ward",
        "point": "ZEL/Pulse Tangrowth 1",
        "method": "Pier Rainstorm Event (100%)"
    },
    "Spoink": {
        "location": "Coral Ward",
        "point": "ZEL/Pulse Tangrowth 1",
        "method": "South Obsidia Chase Event (100%)"
    },
    "Happiny": {
        "location": "Coral Ward",
        "point": "ZEL/Pulse Tangrowth 1",
        "method": "Day Care Couple Event (100%)"
    },
    "Nosepass": {
        "location": "Coral Ward",
        "point": "ZEL/Pulse Tangrowth 1",
        "method": "Trade Watchog"
    },
    "Lillipup": {
        "location": "Onyx Ward",
        "point": "Florina",
        "method": "South Obsidia Chase Event (100%)"
    },
    "Nidoran♂": {
        "location": "Onyx Ward",
        "point": "Florina",
        "method": "Game Corner Prize"
    },
    "Slugma": {
        "location": "Onyx Ward",
        "point": "Florina",
        "method": "Game Corner Prize"
    },
    "Shinx": {
        "location": "Onyx Ward",
        "point": "Florina",
        "method": "Game Corner Prize"
    },
    "Mantyke": {
        "location": "Onyx Ward",
        "point": "Florina",
        "method": "Game Corner Prize"
    },
    "Snover": {
        "location": "Onyx Ward",
        "point": "Florina",
        "method": "Game Corner Prize"
    },
    "Remoraid": [
        {
            "location": "Onyx Ward",
            "point": "Florina",
            "method": "Egg (17%)"
        }, {
            "location": "Chrysolia Forest",
            "point": "Serra",
            "method": "Interact with Fountain After Visiting Spinel Town"
        }
    ],
    "Clauncher": {
        "location": "Onyx Ward",
        "point": "Florina",
        "method": "Egg (17%)"
    },
    "Seel": {
        "location": "Onyx Ward",
        "point": "Florina",
        "method": "Egg (17%)"
    },
    "Spheal": {
        "location": "Onyx Ward",
        "point": "Florina",
        "method": "Egg (17%)"
    },
    "Clamperl": {
        "location": "Onyx Ward",
        "point": "Florina",
        "method": "Egg (17%)"
    },
    "Frillish": {
        "location": "Onyx Ward",
        "point": "Florina",
        "method": "Egg (17%)"
    },
    "Pichu": {
        "location": "Onyx Ward",
        "point": "Taka/Pulse Tangrowth 2",
        "method": "Rooftop Garden Pokesnax Event (100%)"
    },
    "Zangoose": [
        {
            "location": "Lower Peridot Alley",
            "point": "Taka/Pulse Tangrowth 2",
            "method": "Friday Night Alleyway Event (100%)"
        },
        {
            "location": "North Peridot Alley",
            "point": "Taka/Pulse Tangrowth 2",
            "method": "Thursday Night Alleyway Event (100%)"
        },
        {
            "location": "Obsidia Alleyway",
            "point": "Taka/Pulse Tangrowth 2",
            "method": "Monday Night Alleyway Event (100%)"
        },
        {
            "location": "North Obsidia Alleyway",
            "point": "Shade",
            "method": "Tuesday Night Alleyway Event (100%)"
        },
        {
            "location": "Lapis Alleyway",
            "point": "Shelly",
            "method": "Wednesday Night Alleyway Event (100%)"
        }
    ],
    "Stufful": {
        "location": "Peridot Ward",
        "point": "Taka/Pulse Tangrowth 2",
        "method": "House NPC (50%)"
    },
    "Snubbull": {
        "location": "Peridot Ward",
        "point": "Taka/Pulse Tangrowth 2",
        "method": "House NPC (50%)"
    },
    "Petilil": {
        "location": "Obsidia Ward",
        "point": "Taka/Pulse Tangrowth 2",
        "method": "Sunny Pokesnax Event (100%)"
    },
    "Makuhita": [
        {
            "location": "Obsidia Slums",
            "point": "Taka/Pulse Tangrowth 2",
            "method": "Pokesnax Event (100%)"
        }, {
            "location": "7th Street",
            "point": "Subseven Sanctum",
            "method": "Purchase (100%)"
        }
    ],
    "Growlithe": {
        "location": "Jasper Ward",
        "point": "Taka/ZEL/Pulse Tangrowth 3",
        "method": "Police Officer Rescue Event (100%)"
    },
    "Azurill": {
        "location": "Jasper Ward",
        "point": "Taka/ZEL/Pulse Tangrowth 3",
        "method": "Mystery Egg Event (~5%)"
    },
    "Mareanie": [
        {
            "location": "Jasper Ward",
            "point": "Taka/ZEL/Pulse Tangrowth 3",
            "method": "Mystery Egg Event (~5%)"
        }, {
            "location": "Citrine Mountain",
            "point": "Charlotte",
            "method": "Citrine Mountain Puzzle (100%)"
        }
    ],
    "Staryu": {
        "location": "Jasper Ward",
        "point": "Taka/ZEL/Pulse Tangrowth 3",
        "method": "Mystery Egg Event (~5%)"
    },
    "Togepi": [
        {
            "location": "Jasper Ward",
            "point": "Taka/ZEL/Pulse Tangrowth 3",
            "method": "Mystery Egg Event (~5%)"
        }, {
            "location": "Coral Ward",
            "point": "Titania",
            "method": "Railnet Restoration Trade Probopass"
        }
    ],
    "Sneasel": [
        {
            "location": "Jasper Ward",
            "point": "Taka/ZEL/Pulse Tangrowth 3",
            "method": "Mystery Egg Event (~5%)"
        }, {
            "location": "Ametrine Mountain",
            "point": "Ciel",
            "method": "Ametrine Mountain (100%)"
        }
    ],
    "Shroomish": {
        "location": "Jasper Ward",
        "point": "Taka/ZEL/Pulse Tangrowth 3",
        "method": "Mystery Egg Event (~5%)"
    },
    "Gastly": [
        {
            "location": "Jasper Ward",
            "point": "Taka/ZEL/Pulse Tangrowth 3",
            "method": "Mystery Egg Event (~5%)"
        }, {
            "location": "Route 4",
            "point": "Hardy",
            "method": "Route 4 Puzzle (100%)"
        }
    ],
    "Axew": [
        {
            "location": "Jasper Ward",
            "point": "Taka/ZEL/Pulse Tangrowth 3",
            "method": "Mystery Egg Event (~5%)"
        }, {
            "location": "The Underroot",
            "point": "Luna",
            "method": "Crystal Key Event (100%)"
        }
    ],
    "Vulpix (Alolan)": {
        "location": "Jasper Ward",
        "point": "Taka/ZEL/Pulse Tangrowth 3",
        "method": "Mystery Egg Event (~5%)"
    },
    "Pawniard": {
        "location": "Jasper Ward",
        "point": "Taka/ZEL/Pulse Tangrowth 3",
        "method": "Mystery Egg Event (~5%)"
    },
    "Litwick": [
        {
            "location": "Jasper Ward",
            "point": "Taka/ZEL/Pulse Tangrowth 3",
            "method": "Mystery Egg Event (~5%)"
        }, {
            "location": "7th Street",
            "point": "Luna",
            "method": "Soul Candle Subseven Sanctum Event (100%)"
        }
    ],
    "Trapinch": {
        "location": "Jasper Ward",
        "point": "Taka/ZEL/Pulse Tangrowth 3",
        "method": "Mystery Egg Event (~5%)"
    },
    "Cottonee": {
        "location": "Jasper Ward",
        "point": "Taka/ZEL/Pulse Tangrowth 3",
        "method": "Mystery Egg Event (~5%)"
    },
    "Vulpix": [
        {
            "location": "Jasper Ward",
            "point": "Taka/ZEL/Pulse Tangrowth 3",
            "method": "Mystery Egg Event (~5%)"
        }, {
            "location": "Agate Circus",
            "point": "Samson",
            "method": "Trade Stunfisk"
        }
    ],
    "Elekid": [
        {
            "location": "Jasper Ward",
            "point": "Taka/ZEL/Pulse Tangrowth 3",
            "method": "Mystery Egg Event (~5%)"
        }, {
            "location": "Calcenon City",
            "point": "T3RR4",
            "method": "Trade Electirizer (100%)"
        }
    ],
    "Starly": {
        "location": "Jasper Ward",
        "point": "Taka/ZEL/Pulse Tangrowth 3",
        "method": "Mystery Egg Event (~5%)"
    },
    "Rockruff": {
        "location": "Jasper Ward",
        "point": "Taka/ZEL/Pulse Tangrowth 3",
        "method": "Mystery Egg Event (~5%)"
    },
    "Larvesta": [
        {
            "location": "Jasper Ward",
            "point": "Taka/ZEL/Pulse Tangrowth 3",
            "method": "Mystery Egg Event (~5%)"
        }, {
            "location": "Teknite Cave",
            "point": "Hardy",
            "method": "Beryl Ward Entrance Event (100%)"
        }
    ],
    "Mareep": {
        "location": "Jasper Ward",
        "point": "Taka/Pulse Tangrowth 2",
        "method": "House Pokesnax Event (100%)"
    },
    "Emolga": {
        "location": "Jasper Ward",
        "point": "Taka/Pulse Tangrowth 2",
        "method": "Night Event (100%)"
    },
    "Girafarig": {
        "location": "Malchous Forest",
        "point": "Taka/ZEL/Pulse Tangrowth 3",
        "method": "Egg (25%)"
    },
    "Nincada": {
        "location": "Malchous Forest",
        "point": "Taka/ZEL/Pulse Tangrowth 3",
        "method": "Egg (25%)"
    },
    "Deerling": {
        "location": "Malchous Forest",
        "point": "Taka/ZEL/Pulse Tangrowth 3",
        "method": "Egg (25%)"
    },
    "Skiddo": {
        "location": "Malchous Forest",
        "point": "Taka/ZEL/Pulse Tangrowth 3",
        "method": "Egg (25%)"
    },
    "Stantler": {
        "location": "Rhodochrine Jungle",
        "point": "Taka/ZEL/Pulse Tangrowth 3",
        "method": "Western Area Event (100%)"
    },
    "Taillow": {
        "location": "Rhodochrine Jungle",
        "point": "Taka/ZEL/Pulse Tangrowth 3",
        "method": "Western Area Pit Trap Event (100%)"
    },
    "Seviper": {
        "location": "The Underroot",
        "point": "Corey",
        "method": "Pokesnax Event (100%)"
    },
    "Mime Jr.": {
        "location": "Rhodochrine Jungle",
        "point": "Corey",
        "method": "Trade Sunkern (25%)"
    },
    "Cryogonal": {
        "location": "Rhodochrine Jungle",
        "point": "Corey",
        "method": "Trade Sunkern (25%)"
    },
    "Furfrou": {
        "location": "Rhodochrine Jungle",
        "point": "Corey",
        "method": "Trade Sunkern (25%)"
    },
    "Carbink": {
        "location": "Rhodochrine Jungle",
        "point": "Corey",
        "method": "Trade Sunkern (25%)"
    },
    "Helioptile": {
        "location": "Beryl Ward",
        "point": "Corey",
        "method": "Sunny Rooftop Event (100%)"
    },
    "Shuppet": {
        "location": "Beryl Cemetery",
        "point": "Corey",
        "method": "Gravestone Event (100%)"
    },
    "Pumpkaboo (Super Size)": {
        "location": "Beryl Cemetery",
        "point": "Corey",
        "method": "Soul Candle Event (100%)"
    },
    "Mamoswine": {
        "location": "The Underroot",
        "point": "Corey",
        "method": "Breed Ancient Power from Kecleon"
    },
    "Tropius": {
        "location": "Rhodochrine Jungle",
        "point": "Shelly",
        "method": "Sunny Western Area Event (100%)"
    },
    "Gothita": {
        "location": "Beryl Ward",
        "point": "Shelly",
        "method": "Clean Library Event (100%)"
    },
    "Skrelp": {
        "location": "The Underroot",
        "point": "Shelly",
        "method": "Silver Ring Event (100%)"
    },
    "Simisage": {
        "location": "Grand Stairway",
        "point": "Shelly",
        "method": "Leaf Stone"
    },
    "Victreebel": {
        "location": "Grand Stairway",
        "point": "Shelly",
        "method": "Leaf Stone"
    },
    "Vileplume": {
        "location": "Grand Stairway",
        "point": "Shelly",
        "method": "Leaf Stone"
    },
    "Arcanine": [
        {
            "location": "Lapis Ward",
            "point": "Shelly",
            "method": "Fire Stone - Magma Gang 1 Event (100%)"
        }, {
            "location": "Grand Stairway",
            "point": "Shelly",
            "method": "Fire Stone"
        }
    ],
    "Ludicolo": [
        {
            "location": "Lapis Ward",
            "point": "Shelly",
            "method": "Water Stone - Aqua Gang 1 Event (100%)"
        },
        {
            "location": "Grand Stairway",
            "point": "Shelly",
            "method": "Water Stone"
        }
    ],
    "Eelektross": {
        "location": "Grand Stairway",
        "point": "Shelly",
        "method": "Thunder Stone"
    },
    "Raichu": {
        "location": "Grand Stairway",
        "point": "Shelly",
        "method": "Thunder Stone"
    },
    "Solrock": [
        {
            "location": "Grand Stairway",
            "point": "Shelly",
            "method": "Area Above EXPCandy NPC (50%)"
        }, {
            "location": "Grand Stairway",
            "point": "Shade",
            "method": "Trapped Behind Rock Smash (50%)"
        }, {
            "location": "Tanzan Mountain",
            "point": "Serra",
            "method": "Pokesnax Event (50%)"
        }
    ],
    "Lunatone": [
        {
            "location": "Grand Stairway",
            "point": "Shelly",
            "method": "Area Above EXPCandy NPC (50%)"
        }, {
            "location": "Grand Stairway",
            "point": "Shade",
            "method": "Trapped Behind Rock Smash (50%)"
        }, {
            "location": "Tanzan Mountain",
            "point": "Serra",
            "method": "Pokesnax Event (50%)"
        }
    ],
    "Houndour": [
        {
            "location": "North Obsidia Alleyway",
            "point": "Shade",
            "method": "Aqua Gang 2 Event (100%)"
        },
        {
            "location": "North Obsidia Alleyway",
            "point": "Shade",
            "method": "Magma Gang 2 Event (100%)"
        }
    ],
    "Carvanha": {
        "location": "Lapis Alleyway",
        "point": "Shade",
        "method": "Aqua Gang 2 Event (100%)"
    },
    "Buizel": {
        "location": "North Obsidia Alleyway",
        "point": "Shelly",
        "method": "Magma Gang 1 Event (100%)"
    },
    "Ponyta": {
        "location": "North Obsidia Ward",
        "point": "Shelly",
        "method": "Aqua Gang 1 Event (100%)"
    },
    "Spritzee": {
        "location": "Lapis Ward",
        "point": "Shelly",
        "method": "Flower Shop Puzzle (100%)"
    },
    "Golem": {
        "location": "North Obsidia Ward",
        "point": "Shade",
        "method": "Link Stone"
    },
    "Gourgeist (Super Size)": {
        "location": "North Obsidia Ward",
        "point": "Shade",
        "method": "Link Stone"
    },
    "Aromatisse": {
        "location": "North Obsidia Ward",
        "point": "Shade",
        "method": "Link Stone and Sachet"
    },
    "Slurpuff": {
        "location": "North Obsidia Ward",
        "point": "Shade",
        "method": "Link Stone and Whipped Dream"
    },
    "Bellossom": {
        "location": "Grand Stairway",
        "point": "Shade",
        "method": "Sun Stone"
    },
    "Lilligant": {
        "location": "Grand Stairway",
        "point": "Shade",
        "method": "Sun Stone"
    },
    "Heliolisk": {
        "location": "Grand Stairway",
        "point": "Shade",
        "method": "Sun Stone"
    },
    "Roserade": {
        "location": "Grand Stairway",
        "point": "Shade",
        "method": "Shiny Stone"
    },
    "Chansey": {
        "location": "Grand Stairway",
        "point": "Shade",
        "method": "Oval Stone"
    },
    "Scraggy": {
        "location": "Slums Playground",
        "point": "Shade",
        "method": "Dull Key Event (100%)"
    },
    "Porygon": {
        "location": "Onyx Ward",
        "point": "Shade",
        "method": "Data Chip Academy Computer Event (100%)"
    },
    "Nidorina": {
        "location": "Beryl Cave",
        "point": "Shade",
        "method": "Silver Ring Event (100%)"
    },
    "Nuzleaf": {
        "location": "Beryl Cave",
        "point": "Shade",
        "method": "Windy Shiftry Event (100%)"
    },
    "Natu": {
        "location": "Beryl Cave",
        "point": "Shade",
        "method": "Totem Pole Event (100%)"
    },
    "Golett": {
        "location": "Beryl Cave",
        "point": "Shade",
        "method": "Ill Fated Doll Totem Pole Event (33%)"
    },
    "Baltoy": {
        "location": "Beryl Cave",
        "point": "Shade",
        "method": "Ill Fated Doll Totem Pole Event (33%)"
    },
    "Elygem": {
        "location": "Beryl Cave",
        "point": "Shade",
        "method": "Ill Fated Doll Totem Pole Event (33%)"
    },
    "Smoochum": {
        "location": "Citrine Mountain",
        "point": "Shade",
        "method": "Beartic Event (100%)"
    },
    "Amaura": [
        {
            "location": "Citrine Mountain",
            "point": "Shade",
            "method": "Ice Heal Event (100%)"
        }, {
            "location": "7th Street",
            "point": "Subseven Sanctum",
            "method": "Helix Cult Event (50%)"
        }
    ],
    "Croagunk": {
        "location": "Citrine Mountain",
        "point": "Shade",
        "method": "Silver Ring Event (100%)"
    },
    "Ditto": [
        {
            "location": "Peridot Ward",
            "point": "Kiki",
            "method": "Day Care Couple Event Blackstream Factory Event (100%)"
        },
        {
            "location": "7th Street",
            "point": "Subseven Sanctum",
            "method": "Purchase If Missed Previously (100%)"
        }
    ],
    "Murkrow": {
        "location": "Lapis Alleyway",
        "point": "Kiki",
        "method": "Windy Nighttime Event (100%)"
    },
    "Corsola": {
        "location": "Apophyll Beach",
        "point": "Kiki",
        "method": "Storm Pokesnax Event (100%)"
    },
    "Pyukumuku": {
        "location": "Apophyll Beach",
        "point": "Kiki",
        "method": "Lying On Beach (100%)"
    },
    "Shieldon": [
        {
            "location": "Apophyll Cave",
            "point": "Kiki",
            "method": "Trade Ledian"
        }, {
            "location": "Spinel Town",
            "point": "Serra",
            "method": "Fossil Reviver (100%)"
        }
    ],
    "Meditite": {
        "location": "Apophyll Academy",
        "point": "Kiki",
        "method": "Lessons Learned Event (100%)"
    },
    "Turtonator": {
        "location": "Pyrous Mountain",
        "point": "Kiki",
        "method": "Rock Smash Column (50%)"
    },
    "Heatmor": {
        "location": "Pyrous Mountain",
        "point": "Kiki",
        "method": "Pokesnax Floor B1 If Column Did Not Have Turtonator (50%)"
    },
    "Raichu (Alolan)": {
        "location": "Apophyll Beach",
        "point": "Kiki",
        "method": "Thunder Stone on Beach"
    },
    "Foongus": {
        "location": "Azurine Island",
        "point": "Aya",
        "method": "Fake Pokeballs (100%)"
    },
    "Spiritomb": {
        "location": "Byxbysion Tunnels",
        "point": "Aya",
        "method": "Odd Keystone Event (100%)"
    },
    "Misdreavus": {
        "location": "Byxbysion Tunnels",
        "point": "Serra",
        "method": "Kiki Tombstone Event (100%)"
    },
    "Squirtle": {
        "location": "Byxbysion Wasteland",
        "point": "Serra",
        "method": "Rainstorm Event (100%)"
    },
    "Tepig": {
        "location": "Pyrous Mountain",
        "point": "Serra",
        "method": "Pyrous Mountain Strength Puzzle (100%)"
    },
    "Darumaka": {
        "location": "Apophyll Academy",
        "point": "Serra",
        "method": "Trade Luvdisc"
    },
    "Bruxish": {
        "location": "Chrysolia Forest",
        "point": "Serra",
        "method": "Trade Mothim"
    },
    "Mantine": {
        "location": "Chrysolia Forest",
        "point": "Serra",
        "method": "Level Mantyke With Remoraid"
    },
    "Maractus": {
        "location": "Chrysolia Forest",
        "point": "Serra",
        "method": "Egg on Train (50%)"
    },
    "Cacnea": {
        "location": "Chrysolia Forest",
        "point": "Serra",
        "method": "Egg on Train (50%)"
    },
    "Eevee": {
        "location": "Lost Railcave",
        "point": "Serra",
        "method": "Diary Event (100%)"
    },
    "Karrablast": {
        "location": "Spinel Town",
        "point": "Serra",
        "method": "Trade Shelmet"
    },
    "Shelmet": {
        "location": "Spinel Town",
        "point": "Serra",
        "method": "Trade Karrablast"
    },
    "Omanyte": {
        "location": "Spinel Town",
        "point": "Serra",
        "method": "Fossil Reviver (100%)"
    },
    "Kabuto": {
        "location": "Spinel Town",
        "point": "Serra",
        "method": "Fossil Reviver (100%)"
    },
    "Anorith": {
        "location": "Spinel Town",
        "point": "Serra",
        "method": "Fossil Reviver (100%)"
    },
    "Lileep": {
        "location": "Spinel Town",
        "point": "Serra",
        "method": "Fossil Reviver (100%)"
    },
    "Cranidos": {
        "location": "Spinel Town",
        "point": "Serra",
        "method": "Fossil Reviver (100%)"
    },
    "Archen": [
        {
            "location": "Spinel Town",
            "point": "Serra",
            "method": "Nighttime Meteor Grunt Event (50%)"
        },
        {
            "location": "Agate Circus",
            "point": "Adrienn",
            "method": "Agate Circus Puzzle (100%)"
        }
    ],
    "Tirtouga": [
        {
            "location": "Spinel Town",
            "point": "Serra",
            "method": "Nighttime Meteor Grunt Event (50%)"
        },
        {
            "location": "Agate Circus",
            "point": "Adrienn",
            "method": "Agate Circus Puzzle (100%)"
        }
    ],
    "Chikorita": [
        {
            "location": "Azurine Island",
            "point": "Serra",
            "method": "Trade Chimecho"
        }, {
            "location": "Azurine Island",
            "point": "Adrienn",
            "method": "Azurine Island Nature Center Rooftop (100%)"
        }
    ],
    "Heracross": {
        "location": "South Aventurine Woods",
        "point": "Radomus",
        "method": "Honey Puzzle (50%)"
    },
    "Pinsir": {
        "location": "South Aventurine Woods",
        "point": "Radomus",
        "method": "Honey Puzzle (50%)"
    },
    "Flabebe": [
        {
            "location": "South Aventurine Woods",
            "point": "Radomus",
            "method": "Floral Charm Event (100%)"
        },
        {
            "location": "North Aventurine Woods",
            "point": "Radomus",
            "method": "Floral Charm Event (100%)"
        }
    ],
    "Wormadam (Sandy Cloak)": [
        {
            "location": "South Aventurine Woods",
            "point": "Radomus",
            "method": "HeadbuttLow"
        },
        {
            "location": "North Aventurine Woods",
            "point": "Radomus",
            "method": "HeadbuttLow"
        }
    ],
    "Wormadam (Trash Cloak)": [
        {
            "location": "South Aventurine Woods",
            "point": "Radomus",
            "method": "HeadbuttLow"
        },
        {
            "location": "North Aventurine Woods",
            "point": "Radomus",
            "method": "HeadbuttLow"
        }
    ],
    "Mega Pinsir": {
        "location": "North Aventurine Woods",
        "point": "Amaria",
        "method": "Give Nyu Blue Moon Ice Cream (100%)"
    },
    "Mega Heracross": {
        "location": "North Aventurine Woods",
        "point": "Amaria",
        "method": "Give Nyu Blue Moon Ice Cream (100%)"
    },
    "Tyrogue": {
        "location": "Route 1",
        "point": "Radomus",
        "method": "Trade Dunsparce"
    },
    "Crabominable": {
        "location": "Celestinine Mountain",
        "point": "Radomus",
        "method": "Evolve in Celestinine Mountain"
    },
    "Jigglypuff": {
        "location": "7th Street",
        "point": "Subseven Sanctum",
        "method": "Purchase (100%)"
    },
    "Abra": {
        "location": "7th Street",
        "point": "Subseven Sanctum",
        "method": "Purchase (100%)"
    },
    "Lickitung": {
        "location": "7th Street",
        "point": "Subseven Sanctum",
        "method": "Purchase (100%)"
    },
    "Loudred": {
        "location": "7th Street",
        "point": "Subseven Sanctum",
        "method": "Purchase (100%)"
    },
    "Roggenrola": {
        "location": "7th Street",
        "point": "Subseven Sanctum",
        "method": "Purchase (100%)"
    },
    "Cyndaquil": {
        "location": "7th Street",
        "point": "Subseven Sanctum",
        "method": "Purchase (100%)"
    },
    "Tyrunt": {
        "location": "7th Street",
        "point": "Subseven Sanctum",
        "method": "Helix Cult Event (50%)"
    },
    "Piplup": {
        "location": "7th Street",
        "point": "Subseven Sanctum",
        "method": "'Rare Candy' Event (100%)"
    },
    "Chespin": {
        "location": "7th Street",
        "point": "Subseven Sanctum",
        "method": "Oddishweed Event (100%)"
    },
    "Type:Null": {
        "location": "7th Street",
        "point": "Luna",
        "method": "Frankenstein Event (100%)"
    },
    "Rotom": {
        "location": "Yureyu Power Plant",
        "point": "Luna",
        "method": "Yureyu Key Event (100%)"
    },
    "Dhelmise": {
        "location": "Byxbysion Wasteland",
        "point": "Luna",
        "method": "Wasteland Wall Event (100%)"
    },
    "Clefairy": {
        "location": "Agate Circus",
        "point": "Samson",
        "method": "Win High Striker Event Twice (100%)"
    },
    "Timburr": {
        "location": "Agate Circus",
        "point": "Samson",
        "method": "Agate Circus Puzzle (100%)"
    },
    "Salandit": {
        "location": "Route 2",
        "point": "Charlotte",
        "method": "Rage Power Event (100%)"
    },
    "Munchlax": {
        "location": "Calcenon City",
        "point": "Charlotte",
        "method": "Trade Qwilfish"
    },
    "Steelix": {
        "location": "Route 3",
        "point": "Charlotte",
        "method": "Link Stone and Metal Coat"
    },
    "Dusknoir": {
        "location": "Route 3",
        "point": "Charlotte",
        "method": "Link Stone and Reaper Cloth"
    },
    "Mega Banette": {
        "location": "Ametrine City",
        "point": "Amaria",
        "method": "Trade Floral Charm (100%)"
    },
    "Magby": {
        "location": "Calcenon City",
        "point": "T3RR4",
        "method": "Trade Magmarizer (100%)"
    },
    "Turtwig": {
        "location": "Agate Circus",
        "point": "T3RR4",
        "method": "Agate Circus Post-Dive Puzzle (100%)"
    },
    "Riolu": {
        "location": "Ametrine City",
        "point": "T3RR4",
        "method": "Lucario Event (100%)"
    },
    "Heat Rotom": {
        "location": "Ametrine City",
        "point": "T3RR4",
        "method": "Data Chip PC"
    },
    "Wash Rotom": {
        "location": "Ametrine City",
        "point": "T3RR4",
        "method": "Data Chip PC"
    },
    "Fan Rotom": {
        "location": "Ametrine City",
        "point": "T3RR4",
        "method": "Data Chip PC"
    },
    "Frost Rotom": {
        "location": "Ametrine City",
        "point": "T3RR4",
        "method": "Data Chip PC"
    },
    "Mow Rotom": {
        "location": "Ametrine City",
        "point": "T3RR4",
        "method": "Data Chip PC"
    },
    "Porygon-Z": {
        "location": "Glitch World",
        "point": "T3RR4",
        "method": "Link Stone and Dubious Disc"
    },
    "Mega Abomasnow": {
        "location": "Celestinine Cascade",
        "point": "Amaria",
        "method": "Ice Puzzle (100%)"
    },
    "Milotic": {
        "location": "Citrine Mountain",
        "point": "Ciel",
        "method": "Link Stone and Prism Scale"
    },
    "Gliscor": {
        "location": "Ametrine Mountain",
        "point": "Ciel",
        "method": "Link Stone and Razor Fang"
    },
    "Electivire": {
        "location": "Water Treatment Center",
        "point": "Ciel",
        "method": "Link Stone and Electirizer"
    },
    "Lapras": {
        "location": "Ametrine Mountain",
        "point": "Ciel",
        "method": "Underwater B2F Friday Event (100%)"
    },
    "Totodile": {
        "location": "Ametrine Mountain",
        "point": "Ciel",
        "method": "Ametrine Mountain (100%)"
    },
    "Fennekin": {
        "location": "Water Treatment Center",
        "point": "Ciel",
        "method": "Storage Room Event (100%)"
    },
    "Skuntank": {
        "location": "Celestinine Cascade",
        "point": "Ciel",
        "method": "Silver Ring Event (100%)"
    },
    "Zorua": {
        "location": "Beryl Ward",
        "point": "Adrienn",
        "method": "Fake Corey Event (100%)"
    },
    "Ralts": {
        "location": "Obsidia Ward",
        "point": "Adrienn",
        "method": "Corrupted Pokeball Event (100%)"
    },
    "Mega Steelix": {
        "location": "Obsidia Ward",
        "point": "Adrienn",
        "method": "Devon Corp Railnet Reconstruction Project (100%)"
    },
    "Aerodactyl": {
        "location": "Spinel Town",
        "point": "Adrienn",
        "method": "Trade Powerful Staraptor Event (100%)"
    },
    "Mega Camerupt": {
        "location": "Chrysolia Spring",
        "point": "Amaria",
        "method": "Chrysolia Spring Puzzle (100%)"
    },
    "Mega Sharpedo": {
        "location": "Celestinine Mountain",
        "point": "Amaria",
        "method": "North Aventurine Woods Hidden Entrance (100%)"
    },
    "Mega Audino": {
        "location": "Azurine Lake",
        "point": "Amaria",
        "method": "Azurine Lake Dive Puzzle (100%)"
    },
    "Mega Venusaur": {
        "location": "Peridot Ward",
        "point": "Amaria",
        "method": "Mulch Gathering Event (100%)"
    },
    "Mega Glalie": {
        "location": "Coral Ward",
        "point": "Amaria",
        "method": "Underwater City Sunrise Area (100%)"
    },
    "Mega Aggron": {
        "location": "Underground Railnet",
        "point": "Amaria",
        "method": "Railnet Restoration Aron Event (100%)"
    },
    "Klefki": {
        "location": "Jasper Ward",
        "point": "Adrienn",
        "method": "Diamond Ring Event (100%)"
    },
    "Beldum": {
        "location": "Byxbysion Wasteland",
        "point": "Adrienn",
        "method": "Data Chip Event (100%)"
    },
    "Goomy": {
        "location": "Water Treatment Center",
        "point": "Adrienn",
        "method": "G.U.M. Room Event (100%)"
    },
    "Treecko": {
        "location": "The Underroot",
        "point": "Adrienn",
        "method": "Kecleon Event (100%)"
    },
    "Mudkip": {
        "location": "Azurine Lake",
        "point": "Adrienn",
        "method": "Underwater Puzzle (100%)"
    },
    "Popplio": {
        "location": "Coral Lighthouse",
        "point": "Adrienn",
        "method": "Lighthouse Event (100%)"
    },
    "Oshawott": [
        {
            "location": "North Obsidia Alleyway",
            "point": "Adrienn",
            "method": "Magma Gang 3 Event (100%)"
        },
        {
            "location": "Agate City",
            "point": "Hardy",
            "method": "Trade Stantler or Ledian to Aqua Grunt"
        }
    ],
    "Litten": [
        {
            "location": "North Obsidia Alleyway",
            "point": "Titania",
            "method": "Aqua Gang 3 Event (100%)"
        },
        {
            "location": "Agate City",
            "point": "Hardy",
            "method": "Trade Stantler or Ledian to Magma Grunt"
        }
    ],
    "Meowstic (Female)": [
        {
            "location": "Lapis Ward",
            "point": "Adrienn",
            "method": "LandMorning"
        },
        {
            "location": "South Peridot Alley",
            "point": "Adrienn",
            "method": "Cave"
        },
        {
            "location": "North Peridot Alley",
            "point": "Adrienn",
            "method": "Cave"
        }
    ],
    "Weavile": {
        "location": "South Aventurine Woods",
        "point": "Adrienn",
        "method": "Link Stone and Razor Claw"
    },
    "Chimchar": {
        "location": "Azurine Island",
        "point": "Titania",
        "method": "Azurine Island Renovation Trade Carnivine"
    },
    "Exeggutor (Alolan)": {
        "location": "Tourmaline Desert",
        "point": "Titania",
        "method": "Palm Tree Event (100%)"
    },
    "Mimikyu": {
        "location": "Mirage Tower",
        "point": "Titania",
        "method": "Mirage Tower Puzzle (100%)"
    },
    "Honedge": {
        "location": "Mirage Tower",
        "point": "Titania",
        "method": "Mirage Tower Puzzle (100%)"
    },
    "Gible": {
        "location": "Sugiline Cave",
        "point": "Titania",
        "method": "Sugiline Cave Puzzle (100%)"
    },
    "Darmanitan (Zen Mode)": {
        "location": "Tourmaline Desert",
        "point": "Titania",
        "method": "Cave"
    },
    "Rowlet": {
        "location": "Teknite Ridge",
        "point": "Titania",
        "method": "Teknite Ridge Puzzle (100%)"
    },
    "Lycanroc (Midnight Form)": [
        {
            "location": "Teknite Ridge",
            "point": "Hardy",
            "method": "LandMorning"
        },
        {"location": "Tourmaline Desert", "point": "Titania", "method": "Cave"}
    ],
    "Lycanroc (Dusk Form)": [
        {
            "location": "Teknite Ridge",
            "point": "Hardy",
            "method": "LandMorning"
        },
        {"location": "Tourmaline Desert", "point": "Titania", "method": "Cave"}
    ],
    "Mega Medicham": {
        "location": "Sugiline Cave",
        "point": "Amaria",
        "method": "Sugiline Cave Puzzle (100%)"
    },
    "Magikarp": {
        "location": "Desert Town",
        "point": "Titania",
        "method": "Corin-Rogue Event (100%)"
    },
    "Mega Houndoom": {
        "location": "Desert Town",
        "point": "Amaria",
        "method": "Teknite Ridge PC Event (100%)"
    },
    "Mega Pidgeot": {
        "location": "Teknite Ridge",
        "point": "Amaria",
        "method": "Strong Winds Event (100%)"
    },
    "Mega Ampharos": {
        "location": "Opal Ward",
        "point": "Amaria",
        "method": "Grand Hall Basement (100%)"
    },
    "Mega Lopunny": {
        "location": "Opal Ward",
        "point": "Amaria",
        "method": "Grand Hall Director's Office (100%)"
    },
    "Torchic": {
        "location": "Calcenon City",
        "point": "Amaria",
        "method": "Caroline Event (100%)"
    },
    "Larvitar": {
        "location": "Tanzan Depths",
        "point": "Hardy",
        "method": "Rock Climb (100%)"
    },
    "Mega Gallade": {
        "location": "North Aventurine Woods",
        "point": "Hardy",
        "method": "Pokedex Event - 100 Caught (100%)"
    },
    "Mega Mawile": {
        "location": "North Aventurine Woods",
        "point": "Hardy",
        "method": "Pokedex Event - 400 Caught (100%)"
    },
    "Mega Kangaskhan": {
        "location": "North Aventurine Woods",
        "point": "Hardy",
        "method": "Pokedex Event - 700 Caught (100%)"
    },
    "Deino": {
        "location": "7th Street",
        "point": "Hardy",
        "method": "Dark Material Soul Candle Subseven Sanctum Event (100%)"
    },
    "Mega Aerodactyl": {
        "location": "Calcenon City",
        "point": "Hardy",
        "method": "Rock Climb (100%)"
    },
    "Mega Charizard X": {
        "location": "Calcenon City",
        "point": "Hardy",
        "method": "Rock Climb (100%)"
    },
    "Mega Altaria": {
        "location": "Route 4",
        "point": "Hardy",
        "method": "Glassworks Factory Puzzle (100%)"
    },
    "Mega Beedrill": {
        "location": "Route 4",
        "point": "Hardy",
        "method": "Glassworks Factory Puzzle (100%)"
    },
    "Mega Sableye": {
        "location": "Route 4",
        "point": "Hardy",
        "method": "Glassworks Factory Puzzle (100%)"
    },
    "Mega Gardevoir": {
        "location": "Obsidia Ward",
        "point": "Hardy",
        "method": "Magic Square Puzzle (100%)"
    },
    "Mega Manectric": {
        "location": "Obsidia Ward",
        "point": "Hardy",
        "method": "Magic Square Puzzle (100%)"
    },
    "Jangmo-o": {
        "location": "Teknite Ridge",
        "point": "Hardy",
        "method": "Rock Climb (100%)"
    },
    "Mega Sceptile": {
        "location": "Route 4",
        "point": "Hardy",
        "method": "Golem Pokesnax Event (100%)"
    },
    "Bagon": {
        "location": "Route 4",
        "point": "Hardy",
        "method": "Route 4 Event (100%)"
    },
    "Mega Blastoise": {
        "location": "Charous Mountain",
        "point": "Hardy",
        "method": "Charous Mountain Puzzle (100%)"
    },
    "Mega Garchomp": {
        "location": "Opal Ward",
        "point": "Hardy",
        "method": "Starter Pokemon Egg Event (100%)"
    },
    "Froakie": {
        "location": "Agate City",
        "point": "Hardy",
        "method": "Bee 200 Pokedex Event (100%)"
    },
    "Poipole": {
        "location": "North Aventurine Woods",
        "point": "Saphira",
        "method": "Bee 700 Pokedex Event (100%)"
    },
    "Cresselia": {
        "location": "New World",
        "point": "Post-Champion",
        "method": "Tier 1"
    },
    "Zapdos": {
        "location": "Yureyu Power Plant",
        "point": "Post-Champion",
        "method": "Tier 2"
    },
    "Moltres": {
        "location": "Pyrous Mountain",
        "point": "Post-Champion",
        "method": "Tier 2"
    },
    "Articuno": {
        "location": "Ametrine City",
        "point": "Post-Champion",
        "method": "Tier 2"
    },
    "Uxie": {
        "location": "Azurine Lake",
        "point": "Post-Champion",
        "method": "Tier 2"
    },
    "Mesprit": {
        "location": "Azurine Cave",
        "point": "Post-Champion",
        "method": "Tier 2"
    },
    "Azelf": {
        "location": "Apophyll Beach",
        "point": "Post-Champion",
        "method": "Tier 2"
    },
    "Regice": {
        "location": "New World",
        "point": "Post-Champion",
        "method": "Tier 2"
    },
    "Regirock": {
        "location": "New World",
        "point": "Post-Champion",
        "method": "Tier 2"
    },
    "Registeel": {
        "location": "New World",
        "point": "Post-Champion",
        "method": "Tier 2"
    },
    "Entei": {
        "location": "New World",
        "point": "Post-Champion",
        "method": "Tier 2"
    },
    "Suicune": {
        "location": "New World",
        "point": "Post-Champion",
        "method": "Tier 2"
    },
    "Raikou": {
        "location": "New World",
        "point": "Post-Champion",
        "method": "Tier 2"
    },
    "Terrakion": {
        "location": "Route 3",
        "point": "Post-Champion",
        "method": "Tier 3"
    },
    "Cobalion": {
        "location": "New World",
        "point": "Post-Champion",
        "method": "Tier 3"
    },
    "Virizion": {
        "location": "New World",
        "point": "Post-Champion",
        "method": "Tier 3"
    },
    "Keldeo": {
        "location": "New World",
        "point": "Post-Champion",
        "method": "Tier 3"
    },
    "Landorus": {
        "location": "New World",
        "point": "Post-Champion",
        "method": "Tier 3"
    },
    "Thundurus": {
        "location": "New World",
        "point": "Post-Champion",
        "method": "Tier 3"
    },
    "Tornadus": {
        "location": "Route 3",
        "point": "Post-Champion",
        "method": "Tier 3"
    },
    "Regigigas": {
        "location": "New World",
        "point": "Post-Champion",
        "method": "Tier 3"
    },
    "Zygarde": {
        "location": "The Underroot",
        "point": "Post-Champion",
        "method": "Tier 4"
    },
    "Volcanion": {
        "location": "Chrysolia Spring",
        "point": "Post-Champion",
        "method": "Tier 4"
    },
    "Meloetta": {
        "location": "Agate Circus",
        "point": "Post-Champion",
        "method": "Tier 4"
    },
    "Hoopa": {
        "location": "Lower Peridot Ward",
        "point": "Post-Champion",
        "method": "Tier 4"
    },
    "Magearna": {
        "location": "Route 4",
        "point": "Post-Champion",
        "method": "Tier 4"
    },
    "Celebi": {
        "location": "Agate City",
        "point": "Post-Champion",
        "method": "Tier 4"
    },
    "Zeraora": {
        "location": "Chrysolia Deepwoods",
        "point": "Post-Champion",
        "method": "Tier 4"
    },
    "Victini": {
        "location": "Aegir Cave",
        "point": "Post-Champion",
        "method": "Tier 4"
    },
    "Latias": {
        "location": "Unexplored Territory",
        "point": "Post-Champion",
        "method": "Tier 5"
    },
    "Latios": {
        "location": "Unexplored Territory",
        "point": "Post-Champion",
        "method": "Tier 5"
    },
    "Diancie": {
        "location": "Aegir Cave Depths",
        "point": "Post-Champion",
        "method": "Tier 5"
    },
    "Manaphy": {
        "location": "Splash Grounds",
        "point": "Post-Champion",
        "method": "Tier 5"
    },
    "Tapubulu": {
        "location": "Victory Road",
        "point": "Post-Champion",
        "method": "Tier 5"
    },
    "Tapufini": {
        "location": "Victory Road",
        "point": "Post-Champion",
        "method": "Tier 5"
    },
    "Tapukoko": {
        "location": "Victory Road",
        "point": "Post-Champion",
        "method": "Tier 5"
    },
    "Tapulele": {
        "location": "Victory Road",
        "point": "Post-Champion",
        "method": "Tier 5"
    },
    "Jirachi": {
        "location": "New World",
        "point": "Post-Champion",
        "method": "Tier 5"
    },
    "Heatran": {
        "location": "Ametrine Core",
        "point": "Post-Champion",
        "method": "Tier 5"
    },
    "Marshadow": {
        "location": "Apophyll Academy",
        "point": "Post-Champion",
        "method": "Tier 6"
    },
    "Dialga": {
        "location": "7th Street",
        "point": "Post-Champion",
        "method": "Tier 6"
    },
    "Genesect": {
        "location": "Peridot Ward",
        "point": "Post-Champion",
        "method": "Tier 6"
    },
    "Palkia": {
        "location": "7th Street",
        "point": "Post-Champion",
        "method": "Tier 6"
    },
    "Shaymin": {
        "location": "Idyll of Panaceance",
        "point": "Post-Champion",
        "method": "Tier 6"
    },
    "Darkrai": {
        "location": "Iolia Valley",
        "point": "Post-Champion",
        "method": "Tier 6"
    },
    "Ho-Oh": {
        "location": "Mirage Tower?",
        "point": "Post-Champion",
        "method": "Tier 7"
    },
    "Lugia": {
        "location": "Mirage Tower?",
        "point": "Post-Champion",
        "method": "Tier 7"
    },
    "Giratina": {
        "location": "Byxbysion Wasteland",
        "point": "Post-Champion",
        "method": "Tier 7"
    },
    "Reshiram": {
        "location": "New World",
        "point": "Post-Champion",
        "method": "Tier 7"
    },
    "Zekrom": {
        "location": "New World",
        "point": "Post-Champion",
        "method": "Tier 7"
    },
    "Kyurem": {
        "location": "New World",
        "point": "Post-Champion",
        "method": "Tier 7"
    },
    "Deoxys": {
        "location": "New World",
        "point": "Post-Champion",
        "method": "Tier 7"
    },
    "Zygarde": {
        "location": "The Underroot",
        "point": "Post-Champion",
        "method": "Tier 8"
    },
    "Groudon": {
        "location": "Aegir Cave",
        "point": "Post-Champion",
        "method": "Tier 8"
    },
    "Rayquaza": {
        "location": "Aegir Cave",
        "point": "Post-Champion",
        "method": "Tier 8"
    },
    "Xerneas": {
        "location": "Rhodochrine Tree",
        "point": "Post-Champion",
        "method": "Tier 8"
    },
    "Yveltal": {
        "location": "Rhodochrine Tree",
        "point": "Post-Champion",
        "method": "Tier 8"
    },
    "Mew": {
        "location": "Neoteric Isle",
        "point": "Post-Champion",
        "method": "Tier 8"
    },
    "Mewtwo": {
        "location": "Neoteric Isle",
        "point": "Post-Champion",
        "method": "Tier 8"
    },
    "Necrozma": {
        "location": "Citae Prisma",
        "point": "Post-Champion",
        "method": "Tier 8"
    },
    "Kyogre": {
        "location": "New World",
        "point": "Post-Champion",
        "method": "Tier 8"
    },
    "Arceus": {
        "location": "New World",
        "point": "Post-Champion",
        "method": "End"
    }
}

tmLocations = [
    {"name": "WORKUP", "location": "Ametrine Mountain",
        "point": "Adrienn", "method": "B3F"},
    {"name": "DRAGONCLAW", "location": "Route 3",
        "point": "Elite 4/Champion", "method": "Saphira Prize"},
    {"name": "PSYSHOCK", "location": "Celestinine Mountain",
        "point": "Ciel", "method": "4F"},
    {"name": "CALMMIND", "location": "Mirage Tower",
        "point": "Titania", "method": "Mirage Tower Puzzle"},
    {"name": "ROAR", "location": "Rhodochrine Jungle",
        "point": "Shade", "method": "Rhodochrine Jungle Puzzle"},
    {"name": "TOXIC", "location": "Peridot Ward",
        "point": "Adrienn", "method": "Simon ID Tag Event"},
    {"name": "HAIL", "location": "Lapis Ward",
        "point": "Shelly", "method": "Purchase at Pokemart"},
    {"name": "BULKUP", "location": "Tourmaline Desert",
     "point": "Titania", "method": "Search Desert"},
    {"name": "VENOSHOCK", "location": "Byxbysion Wasteland",
     "point": "Aya", "method": "Mr. Bigglesworth Event"},
    {"name": "HIDDENPOWER", "location": "Tanzan Cove",
     "point": "Radomus", "method": "Noel Prize"},
    {"name": "SUNNYDAY", "location": "7th Street", "point": "Luna",
     "method": "Side with Magma Gang or Beat Maxwell"},
    {"name": "TAUNT", "location": "Byxbysion Wasteland",
     "point": "Aya", "method": "Search Byxbysion Wasteland"},
    {"name": "ICEBEAM", "location": "Agate City",
        "point": "Hardy", "method": "Bee 300 Pokedex Event"},
    {"name": "BLIZZARD", "location": "Obsidia Ward",
        "point": "Hardy", "method": "Obsidia Department Store Penthouse Give Kid Lemonade"},
    {"name": "HYPERBEAM", "location": "Spinel Town", "point": "Amaria",
     "method": "Defeat McKrezzy During Mega Ring Event"},
    {"name": "LIGHTSCREEN", "location": "Azurine Island",
     "point": "Titania", "method": "NPC Gift"},
    {"name": "PROTECT", "location": "North Obsidia Alleyway", "point": "Shelly",
     "method": "Inside Night Club Lobby"},
    {"name": "RAINDANCE", "location": "7th Street", "point": "Luna",
     "method": "Side with Aqua Gang or Beat Archer"},
    {"name": "ROOST", "location": "1R253 Scrapyard",
     "point": "Titania", "method": "1R253 Scrapyard Puzzle"},
    {"name": "SAFEGUARD", "location": "Beryl Ward",
     "point": "Corey", "method": "Beryl Library Bookshelf Puzzle"},
    {"name": "FRUSTRATION", "location": "Lapis Ward",
     "point": "Shelly", "method": "Magma/Aqua Gang 1 Event"},
    {"name": "SOLARBEAM", "location": "Obsidia Ward",
     "point": "Adrienn", "method": "Obsidia Department Store 9F"},
    {"name": "SMACKDOWN", "location": "Celestinine Mountain",
     "point": "Radomus", "method": "B2F Strength Puzzle"},
    {"name": "THUNDERBOLT", "location": "Obsidia Ward",
     "point": "Adrienn", "method": "Magic Square Puzzle"},
    {"name": "THUNDER", "location": "Obsidia Ward", "point": "Hardy",
        "method": "Obsidia Department Store Penthouse Give Kid Fresh Water"},
    {"name": "EARTHQUAKE", "location": "Opal Ward",
        "point": "Hardy", "method": "Starter Pokemon Egg Event"},
    {"name": "RETURN", "location": "Peridot Ward",
     "point": "Adrienn", "method": "Blackstream Shelter 1F, Betting Guy"},
    {"name": "LEECHLIFE", "location": "Celestinine Cascade", "point": "Hardy",
     "method": "Rock Climb Near Fiore Mansion"},
    {"name": "PSYCHIC", "location": "Route 4", "point": "Hardy",
     "method": "Search Glass Workstation B2F"},
    {"name": "SHADOWBALL", "location": "Beryl Ward",
     "point": "Adrienn", "method": "Beryl Library Hidden Room"},
    {"name": "BRICKBREAK", "location": "Agate Circus",
     "point": "Charlotte", "method": "Samson Prize"},
    {"name": "DOUBLETEAM", "location": "Lost Railcave",
     "point": "Serra", "method": "Lost Railcave Puzzle"},
    {"name": "REFLECT", "location": "The Underroot",
     "point": "Adrienn", "method": "Search Area with Silvon Scope"},
    {"name": "SLUDGEWAVE", "location": "Byxbysion Wasteland",
     "point": "Serra", "method": "Aya Prize"},
    {"name": "FLAMETHROWER", "location": "Calcenon City",
     "point": "T3RR4", "method": "Charlotte Prize"},
    {"name": "SLUDGEBOMB", "location": "Tourmaline Desert",
        "point": "Titania", "method": "Search Desert"},
    {"name": "SANDSTORM", "location": "Pyrous Mountain",
     "point": "Serra", "method": "Search B1F By Tepig"},
    {"name": "FIREBLAST", "location": "Obsidia Ward", "point": "Hardy",
        "method": "Obsidia Department Store Penthouse Give Kid Soda Pop"},
    {"name": "ROCKTOMB", "location": "Celestinine Cascade",
     "point": "Samson", "method": "Beat Clown Bindra"},
    {"name": "AERIALACE", "location": "South Aventurine Woods",
     "point": "Radomus", "method": "Search Woods"},
    {"name": "TORMENT", "location": "Lapis Ward",
     "point": "Shelly", "method": "Search Lapis Ward"},
    {"name": "FACADE", "location": "Onyx Ward",
     "point": "Florina", "method": "Game Corner Prize"},
    {"name": "FLAMECHARGE", "location": "Route 3",
     "point": "Charlotte", "method": "Search Labradorra Calcenon Control Center"},
    {"name": "REST", "location": "Underground Railnet", "point": "Serra",
     "method": "Search Underground Railnet"},
    {"name": "ATTRACT", "location": "Onyx Ward",
     "point": "Florina", "method": "Game Corner Prize"},
    {"name": "THIEF", "location": "North Obsidia Alleyway",
     "point": "Shelly", "method": "Search Area"},
    {"name": "LOWSWEEP", "location": "Celestinine Mountain",
     "point": "T3RR4", "method": "Celestinine Mountain Puzzle"},
    {"name": "ROUND", "location": "Obsidia Ward",
     "point": "Aya", "method": "Obsidia Department Store 4F"},
    {"name": "ECHOEDVOICE", "location": "Peridot Ward",
     "point": "Kiki", "method": "Search Blackstream Factor B2F"},
    {"name": "OVERHEAT", "location": "Chrysolia Spring", "point": "Adrienn",
     "method": "Search Area"},
    {"name": "STEELWING", "location": "South Aventurine Woods",
     "point": "Radomus", "method": "Search Woods"},
    {"name": "FOCUSBLAST", "location": "Apophyll Beach",
     "point": "Hardy", "method": "Rock Climb Near Pyrous Mountain"},
    {"name": "ENERGYBALL", "location": "Route 3",
        "point": "Hardy", "method": "Rock Climb"},
    {"name": "FALSESWIPE", "location": "Obsidia Ward", "point": "Florina",
     "method": "Room with Day Care Couple Key"},
    {"name": "SCALD", "location": "Celestinine Cascade",
     "point": "Hardy", "method": "Amaria Prize"},
    {"name": "FLING", "location": "North Obsidia Alleyway",
     "point": "Shelly", "method": "The Spyce Trashcan"},
    {"name": "CHARGEBEAM", "location": "Peridot Ward",
     "point": "ZEL/Pulse Tangrowth 1", "method": "Julia Prize"},
    {"name": "SKYDROP", "location": "Route 2",
     "point": "Samson", "method": "Search Route 2"},
    {"name": "BRUTALSWING", "location": "Azurine Cave",
     "point": "Adrienn", "method": "King Pyukumuku Event"},
    {"name": "QUASH", "location": "Obsidia Slums",
     "point": "ZEL/Pulse Tangrowth 1", "method": "Search 2F Top Right"},
    {"name": "WILLOWISP", "location": "Chrysolia Spring",
     "point": "Adrienn", "method": "Search Area"},
    {"name": "ACROBATICS", "location": "Agate Circus", "point": "Adrienn",
     "method": "Talk to Ringmaster After Defeating Ciel"},
    {"name": "EMBARGO", "location": "Onyx Ward",
     "point": "Florina", "method": "Search Area"},
    {"name": "EXPLOSION", "location": "7th Street", "point": "Subseven Sanctum",
     "method": "Purchase from Street Rat Merchant"},
    {"name": "SHADOWCLAW", "location": "Yureyu Power Plant",
     "point": "Kiki", "method": "Shade Prize"},
    {"name": "PAYBACK", "location": "Byxbysion Wasteland",
     "point": "Aya", "method": "Search Byxbysion Grotto Middle Fork"},
    {"name": "SMARTSTRIKE", "location": "Water Treatment Center",
     "point": "Ciel", "method": "Search Area"},
    {"name": "GIGAIMPACT", "location": "Coral Lighthouse",
     "point": "Adrienn", "method": "Search Lighthouse Upper Area"},
    {"name": "ROCKPOLISH", "location": "Grand Stairway",
     "point": "Shelly", "method": "B2F Grand Stairway Puzzle"},
    {"name": "AURORAVEIL", "location": "Spinel Town",
     "point": "Noel", "method": "Serra Prize"},
    {"name": "STONEEDGE", "location": "Sugiline Ruin", "point": "Titania",
     "method": "Search 1F Left of Arceus Statue Upper Middle"},
    {"name": "VOLTSWITCH", "location": "Tourmaline Desert",
        "point": "Titania", "method": "Search Desert"},
    {"name": "THUNDERWAVE", "location": "Route 4",
     "point": "Hardy", "method": "Search Mechanic Shed"},
    {"name": "GYROBALL", "location": "Citrine Mountain", "point": "Ciel",
     "method": "Search 3F"},
    {"name": "SWORDSDANCE", "location": "Teknite Ridge",
        "point": "Titania", "method": "Search Area"},
    {"name": "STRUGGLEBUG", "location": "Lapis Ward",
     "point": "Shade", "method": "Shelly Prize"},
    {"name": "PSYCHUP", "location": "Rhodochrine Jungle", "point": "Corey",
     "method": "Search Area"},
    {"name": "BULLDOZE", "location": "Glitch World",
     "point": "Ciel", "method": "T3RR4 Prize"},
    {"name": "FROSTBREATH", "location": "Ametrine City", "point": "Ciel",
     "method": "Search Area"},
    {"name": "ROCKSLIDE", "location": "Agate City",
     "point": "Saphira", "method": "Hardy Prize"},
    {"name": "XSCISSOR", "location": "Obsidia Ward",
     "point": "Adrienn", "method": "Devon Corp 6F"},
    {"name": "DRAGONTAIL", "location": "Celestinine Mountain", "point": "T3RR4",
     "method": "Search 1F"},
    {"name": "INFESTATION", "location": "Azurine Island",
     "point": "Aya", "method": "West-side of Island Where Boat is Docked"},
    {"name": "POISONJAB", "location": "Water Treatment Center",
     "point": "Titania", "method": "GUM Room Puzzle"},
    {"name": "DREAMEATER", "location": "Spinel Town",
     "point": "Serra", "method": "Voclain Estate"},
    {"name": "GRASSKNOT", "location": "North Aventurine Woods",
     "point": "Radomus", "method": "Search Area"},
    {"name": "SWAGGER", "location": "Agate Circus",
     "point": "Samson", "method": "High Striker Prize"},
    {"name": "SLEEPTALK", "location": "Peridot Ward", "point": "Aya",
     "method": "Search Area"},
    {"name": "UTURN", "location": "Iolia Valley",
        "point": "Adrienn", "method": "Surf"},
    {"name": "SUBSTITUTE", "location": "Onyx Ward",
     "point": "Florina", "method": "Game Corner Prize"},
    {"name": "FLASHCANNON", "location": "Once Upon a Somewhere/Waste of Time",
     "point": "Amaria", "method": "Titania Prize"},
    {"name": "TRICKROOM", "location": "Vanhanen Labyrinth",
     "point": "Subseven Sanctum", "method": "Radomus Prize"},
    {"name": "WILDCHARGE", "location": "Water Treatment Center", "point": "Ciel",
     "method": "Search Area"},
    {"name": "SECRETPOWER", "location": "Citrine Mountain",
     "point": "Ciel", "method": "Search 2F"},
    {"name": "SNARL", "location": "Ametrine City",
     "point": "Ciel", "method": "Search Area"},
    {"name": "NATUREPOWER", "location": "Onyx Ward",
     "point": "Taka/Pulse Tangrowth 2", "method": "Florina Prize"},
    {"name": "DARKPULSE", "location": "Iolia Valley",
     "point": "Point of No Return", "method": "Luna Prize"},
    {"name": "POWERUPPUNCH", "location": "Azurine Island", "point": "Titania",
     "method": "Search Area"},
    {"name": "DAZZLINGGLEAM", "location": "Coral Ward",
     "point": "Titania", "method": "Adrienn Prize"},
    {"name": "CONFIDE", "location": "Lost Railcave",
     "point": "Serra", "method": "Lost Railcave Puzzle"},
    {"name": "CUT", "location": "Obsidia Ward", "point": "ZEL/Pulse Tangrowth 1",
     "method": "Given by Amaria During Stroy"},
    {"name": "FLY", "location": "Celestinine Cascade", "point": "Ciel",
     "method": "Given by Florina After Water Treatment Center"},
    {"name": "SURF", "location": "Celestinine Cascade",
     "point": "Charlotte", "method": "Given by Titania After Samson"},
    {"name": "STRENGTH", "location": "Apophyll Academy", "point": "Aya",
     "method": "Given by Victoria After Pulse Camerupt"},
    {"name": "WATERFALL", "location": "Ametrine City",
     "point": "T3RR4", "method": "Given by Blake or Aster"},
    {"name": "DIVE", "location": "Agate Circus",
     "point": "Samson", "method": "Agate Circus Puzzle"},
    {"name": "ROCKSMASH", "location": "Grand Stairway", "point": "Shelly",
     "method": "Given by Black Belt on Middle-Left Ledges"},
    {"name": "FLASH", "location": "Underground Railnet",
     "point": "Serra", "method": "Search Aron Room"},
    {"name": "ROCKCLIMB", "location": "Route 4", "point": "Hardy", "method": "Given by Hardy"}]

tutorLocations = [
    {"name": "AFTERYOU", "location": "Onyx Ward",
     "point": "Florina", "method": "Left Upper Room Onyx School"},
    {"name": "AIRCUTTER", "location": "", "point": "", "method": ""},
    {"name": "ALLYSWITCH", "location": "Onyx Ward",
     "point": "Florina", "method": "Left Upper Room Onyx School"},
    {"name": "ANCIENTPOWER", "location": "", "point": "", "method": ""},
    {"name": "AQUATAIL", "location": "Peridot Ward",
     "point": "Adrienn", "method": "Mosswater Market"},
    {"name": "BIND", "location": "Onyx Ward",
     "point": "Florina", "method": "Top Lower Room Onyx School"},
    {"name": "BLASTBURN", "location": "Peridot Ward",
     "point": "Saphira", "method": "Mosswater Market"},
    {"name": "BLOCK", "location": "Onyx Ward",
     "point": "Florina", "method": "Right Upper Room Onyx Ward"},
    {"name": "BOUNCE", "location": "7th Street",
     "point": "Subseven Sanctum", "method": "Red Tutor"},
    {"name": "BUGBITE", "location": "7th Street",
     "point": "Subseven Sanctum", "method": "Orange Tutor"},
    {"name": "COVET", "location": "7th Street",
     "point": "Subseven Sanctum", "method": "Doxy Tutor"},
    {"name": "DEFOG", "location": "7th Street",
     "point": "Subseven Sanctum", "method": "Magician Tutor"},
    {"name": "DRACOMETEOR", "location": "Peridot Ward",
     "point": "Saphira", "method": "Mosswater Market"},
    {"name": "DRAGONASCENT", "location": "", "point": "", "method": ""},
    {"name": "DRAGONPULSE", "location": "Peridot Ward",
     "point": "Titania", "method": "Mosswater Market"},
    {"name": "DRAINPUNCH", "location": "Peridot Ward",
     "point": "Adrienn", "method": "Mosswater Market"},
    {"name": "DRILLRUN", "location": "Agate Circus",
     "point": "Samson", "method": "Red Tutor"},
    {"name": "DUALCHOP", "location": "Agate Circus",
     "point": "Samson", "method": "Orange Tutor"},
    {"name": "EARTHPOWER", "location": "Peridot Ward",
     "point": "Amaria", "method": "Mosswater Market"},
    {"name": "ELECTROWEB", "location": "7th Street",
     "point": "Subseven Sanctum", "method": "Doxy Tutor"},
    {"name": "ENDEAVOR", "location": "Apophyll Academy",
     "point": "Kiki", "method": "Back Room Upper Floor"},
    {"name": "FIREPLEDGE", "location": "Lapis Ward",
     "point": "Shelly", "method": "Left of Shelly's Gym"},
    {"name": "FIREPUNCH", "location": "Agate Circus",
     "point": "Samson", "method": "Orange Tutor"},
    {"name": "FOCUSPUNCH", "location": "Agate Circus",
     "point": "Samson", "method": "Orange Tutor"},
    {"name": "FOULPLAY", "location": "Peridot Ward",
     "point": "Titania", "method": "Mosswater Market"},
    {"name": "FRENZYPLANT", "location": "Peridot Ward",
     "point": "Saphira", "method": "Mosswater Market"},
    {"name": "FURYCUTTER", "location": "", "point": "", "method": ""},
    {"name": "GASTROACID", "location": "Apophyll Academy",
     "point": "Kiki", "method": "Back Room Upper Floor"},
    {"name": "GIGADRAIN", "location": "7th Street",
     "point": "Adrienn", "method": "Lower Yellow Tutor"},
    {"name": "GRASSPLEDGE", "location": "Lapis Ward",
     "point": "Shelly", "method": "Left of Shelly's Gym"},
    {"name": "GRAVITY", "location": "Onyx Ward",
     "point": "Florina", "method": "Right Upper Room Onyx School"},
    {"name": "GUNKSHOT", "location": "Peridot Ward",
     "point": "Titania", "method": "Mosswater Market"},
    {"name": "HEADBUTT", "location": "7th Street",
        "point": "Subseven Sanctum", "method": "Red Tutor"},
    {"name": "HEALBELL", "location": "7th Street",
     "point": "Subseven Sanctum", "method": "Lower Yellow Tutor"},
    {"name": "HEATWAVE", "location": "Peridot Ward",
     "point": "Amaria", "method": "Mosswater Market"},
    {"name": "HELPINGHAND", "location": "Onyx Ward",
     "point": "Florina", "method": "Left Upper Room Onyx School"},
    {"name": "HYDROCANNON", "location": "Peridot Ward",
     "point": "Saphira", "method": "Mosswater Market"},
    {"name": "HYPERVOICE", "location": "Agate Circus",
     "point": "Samson", "method": "Orange Tutor"},
    {"name": "ICEPUNCH", "location": "7th Street",
     "point": "Samson", "method": "Orange Tutor"},
    {"name": "ICYWIND", "location": "Peridot Ward",
     "point": "Adrienn", "method": "Mosswater Market"},
    {"name": "IRONDEFENSE", "location": "Onyx Ward",
     "point": "Florina", "method": "Top Lower Room Onyx School"},
    {"name": "IRONHEAD", "location": "7th Street",
     "point": "Adrienn", "method": "Lower Yellow Tutor"},
    {"name": "IRONTAIL", "location": "Agate Circus",
     "point": "Samson", "method": "Orange Tutor"},
    {"name": "KNOCKOFF", "location": "7th Street",
     "point": "Adrienn", "method": "Lower Yellow Tutor"},
    {"name": "LASERFOCUS", "location": "7th Street",
     "point": "Subseven Sanctum", "method": "Magician Tutor"},
    {"name": "LASTRESORT", "location": "7th Street",
     "point": "Subseven Sanctum", "method": "Red Tutor"},
    {"name": "LIQUIDATION", "location": "7th Street",
     "point": "Adrienn", "method": "Lower Yellow Tutor"},
    {"name": "LOWKICK", "location": "Agate Circus",
     "point": "Samson", "method": "Orange Tutor"},
    {"name": "MAGICCOAT", "location": "Onyx Ward",
     "point": "Florina", "method": "Left Lower Room Onyx School"},
    {"name": "MAGICROOM", "location": "Onyx Ward",
     "point": "Florina", "method": "Left Lower Roon Onyx School"},
    {"name": "MAGNETRISE", "location": "Onyx Ward",
     "point": "Florina", "method": "Right Upper Room Onyx School"},
    {"name": "MUDSLAP", "location": "", "point": "", "method": ""},
    {"name": "OMINOUSWIND", "location": "", "point": "", "method": ""},
    {"name": "OUTRAGE", "location": "Peridot Ward",
     "point": "Amaria", "method": "Mosswater Market"},
    {"name": "PAINSPLIT", "location": "Apophyll Academy",
     "point": "Kiki", "method": "Back Room Upper Floor"},
    {"name": "RECYCLE", "location": "Apophyll Academy",
     "point": "Kiki", "method": "Back Room Upper Floor"},
    {"name": "RELICSONG", "location": "", "point": "", "method": ""},
    {"name": "ROLEPLAY", "location": "7th Street",
     "point": "Subseven Sanctum", "method": "Yellow Tutor"},
    {"name": "ROLLOUT", "location": "", "point": "", "method": ""},
    {"name": "SECRETSWORD", "location": "", "point": "", "method": ""},
    {"name": "SEEDBOMB", "location": "Peridot Ward",
     "point": "Titania", "method": "Mosswater Market"},
    {"name": "SHOCKWAVE", "location": "7th Street",
     "point": "Subseven Sanctum", "method": "Red Tutor"},
    {"name": "SIGNALBEAM", "location": "Peridot Ward",
     "point": "Adrienn", "method": "Mosswater Market"},
    {"name": "SKILLSWAP", "location": "7th Street",
     "point": "Subseven Sanctum", "method": "Yellow Tutor"},
    {"name": "SKYATTACK", "location": "7th Street",
     "point": "Subseven Sanctum", "method": "Yellow Tutor"},
    {"name": "SNATCH", "location": "Onyx Ward",
     "point": "Florina", "method": "Left Upper Room Onyx Ward"},
    {"name": "SNORE", "location": "Onyx Ward",
     "point": "Florina", "method": "Top Lower Room Onyx School"},
    {"name": "SPITE", "location": "Onyx Ward",
     "point": "Florina", "method": "Top Lower Room Onyx School"},
    {"name": "STEALTHROCK", "location": "Peridot Ward",
     "point": "Adrienn", "method": "Mosswater Market"},
    {"name": "STOMPINGTANTRUM", "location": "Agate Circus",
     "point": "Samson", "method": "Orange Tutor"},
    {"name": "STRINGSHOT", "location": "", "point": "", "method": ""},
    {"name": "SUCKERPUNCH", "location": "", "point": "", "method": ""},
    {"name": "SUPERFANG", "location": "7th Street",
     "point": "Subseven Sanctum", "method": "Yellow Tutor"},
    {"name": "SUPERPOWER", "location": "Peridot Ward",
     "point": "Amaria", "method": "Mosswater Market"},
    {"name": "SWIFT", "location": "", "point": "", "method": ""},
    {"name": "SYNTHESIS", "location": "Agate Circus",
     "point": "Samson", "method": "Orange Tutor"},
    {"name": "TAILWIND", "location": "Peridot Ward",
     "point": "Adrienn", "method": "Mosswater Market"},
    {"name": "TELEKINESIS", "location": "Onyx Ward",
     "point": "Florina", "method": "Left Lower Room Onyx School"},
    {"name": "THROATCHOP", "location": "Peridot Ward",
     "point": "Adrienn", "method": "Mosswater Market"},
    {"name": "THUNDERPUNCH", "location": "Agate Circus",
     "point": "Samson", "method": "Orange Tutor"},
    {"name": "TRICK", "location": "7th Street",
     "point": "Subseven Sanctum", "method": "Red Tutor"},
    {"name": "TWISTER", "location": "", "point": "", "method": ""},
    {"name": "UPROAR", "location": "Agate Circus",
     "point": "Samson", "method": "Red Tutor"},
    {"name": "VACUUMWAVE", "location": "", "point": "", "method": ""},
    {"name": "VOLTTACKLE", "location": "North Aventurine Woods",
     "point": "Radomus", "method": "NyuF"},
    {"name": "WATERPLEDGE", "location": "Lapis Ward",
     "point": "Shelly", "method": "Left of Shelly's Gym"},
    {"name": "WATERPULSE", "location": "7th Street",
     "point": "Subseven Sanctum", "method": "Red Tutor"},
    {"name": "WONDERROOM", "location": "Onyx Ward",
     "point": "Florina", "method": "Left Lower Room Onyx School"},
    {"name": "WORRYSEED", "location": "Onyx Ward",
     "point": "Florina", "method": "Right Upper Room Onyx School"},
    {"name": "ZENHEADBUTT", "location": "Peridot Ward", "point": "Adrienn", "method": "Mosswater Market"}]


points = [
    {"name": "Julia", "level": "20"},
    {"name": "ZEL/Pulse Tangrowth 1", "level": "25"},
    {"name": "Florina", "level": "25"},
    {"name": "Taka/Pulse Tangrowth 2", "level": "35"},
    {"name": "Taka/ZEL/Pulse Tangrowth 3", "level": "35"},
    {"name": "Corey", "level": "35"},
    {"name": "Shelly", "level": "35"},
    {"name": "Shade", "level": "40"},
    {"name": "Kiki", "level": "45"},
    {"name": "Aya", "level": "45"},
    {"name": "Serra", "level": "50"},
    {"name": "Noel", "level": "55"},
    {"name": "Radomus", "level": "60"},
    {"name": "Subseven Sanctum", "level": "65"},
    {"name": "Luna", "level": "65"},
    {"name": "Point of No Return", "level": "70"},
    {"name": "Samson", "level": "70"},
    {"name": "Charlotte", "level": "70"},
    {"name": "T3RR4", "level": "75"},
    {"name": "Ciel", "level": "75"},
    {"name": "Adrienn", "level": "80"},
    {"name": "Titania", "level": "85"},
    {"name": "Amaria", "level": "90"},
    {"name": "Hardy", "level": "90"},
    {"name": "Saphira", "level": "95"},
    {"name": "Elite 4/Champion", "level": "100"},
    {"name": "Post-Champion", "level": "120"}
]

methods = [
    {"name": "OldRod", "point": "Julia"},
    {"name": "RockSmash", "point": "Shade"},
    {"name": "GoodRod", "point": "Serra"},
    {"name": "Water", "point": "Charlotte"},
    {"name": "SuperRod", "point": "Adrienn"}
]

locations = [
    {"name": "Opal Ward", "point": "Julia"},
    {"name": "Lower Peridot Ward", "point": "Julia"},
    {"name": "Peridot Ward", "point": "Julia"},
    {"name": "North Peridot Alley", "point": "Julia"},
    {"name": "Lower Peridot Alley", "point": "Julia"},
    {"name": "Peridot Underground Railnet", "point": "Julia"},
    {"name": "Obsidia Slums", "point": "ZEL/Pulse Tangrowth 1"},
    {"name": "Coral Ward", "point": "ZEL/Pulse Tangrowth 1"},
    {"name": "Obsidia Alleyway", "point": "ZEL/Pulse Tangrowth 1"},
    {"name": "Obsidia Ward", "point": "ZEL/Pulse Tangrowth 1"},
    {"name": "Obsidia Underground Railnet", "point": "ZEL/Pulse Tangrowth 1"},
    {"name": "Onyx Ward", "point": "Florina"},
    {"name": "Jasper Ward", "point": "Taka/Pulse Tangrowth 2"},
    {"name": "Malchous Forest", "point": "Taka/Pulse Tangrowth 2"},
    {"name": "Beryl Ward", "point": "Taka/ZEL/Pulse Tangrowth 3"},
    {"name": "Rhodochrine Jungle", "point": "Taka/ZEL/Pulse Tangrowth 3"},
    {"name": "The Underroot", "point": "Corey"},
    {"name": "Beryl Cemetery", "point": "Corey"},
    {"name": "North Obsidia Alleyway", "point": "Shelly"},
    {"name": "Lapis Alleyway", "point": "Shelly"},
    {"name": "Grand Stairway", "point": "Shelly"},
    {"name": "Beryl Cave", "point": "Shade"},
    {"name": "Underground Railnet", "point": "Shade"},
    {"name": "Slums Playground", "point": "Shade"},
    {"name": "Yureyu Power Plant", "point": "Shade"},
    {"name": "Apophyll Beach", "point": "Kiki"},
    {"name": "Apophyll Academy", "point": "Kiki"},
    {"name": "Apophyll Cave", "point": "Kiki"},
    {"name": "Pyrous Mountain", "point": "Kiki"},
    {"name": "Azurine Island", "point": "Aya"},
    {"name": "Byxbysion Wasteland", "point": "Aya"},
    {"name": "Byxbysion Tunnels", "point": "Aya"},
    {"name": "Tanzan Mountain", "point": "Serra"},
    {"name": "Chrysolia Forest", "point": "Serra"},
    {"name": "Chrysolia Spring", "point": "Serra"},
    {"name": "Lost Railcave", "point": "Serra"},
    {"name": "Spinel Town", "point": "Serra"},
    {"name": "Tanzan Cove", "point": "Serra"},
    {"name": "Tanzan Depths", "point": "Noel"},
    {"name": "South Aventurine Woods", "point": "Radomus"},
    {"name": "Route 1", "point": "Radomus"},
    {"name": "North Aventurine Woods", "point": "Radomus"},
    {"name": "Vanhanen Labyrinth", "point": "Radomus"},
    {"name": "Celestinine Mountain", "point": "Radomus"},
    {"name": "Citae Astrae", "point": "Radomus"},
    {"name": "7th Street", "point": "Subseven Sanctum"},
    {"name": "Iolia Valley", "point": "Luna"},
    {"name": "Agate Circus", "point": "Samson"},
    {"name": "Route 2", "point": "Samson"},
    {"name": "Ametrine Mountain", "point": "Samson"},
    {"name": "Celestinine Cascade", "point": "Samson"},
    {"name": "Citrine Mountain", "point": "Samson"},
    {"name": "Route 3", "point": "Charlotte"},
    {"name": "Route 3 Caves", "point": "Charlotte"},
    {"name": "Route 4", "point": "Charlotte"},
    {"name": "Calcenon City", "point": "Charlotte"},
    {"name": "Ametrine City", "point": "T3RR4"},
    {"name": "Glitch World", "point": "T3RR4"},
    {"name": "Water Treatment Center", "point": "Ciel"},
    {"name": "South Peridot Alley", "point": "Adrienn"},
    {"name": "North Obsidia Ward", "point": "Adrienn"},
    {"name": "South Obsidia Ward", "point": "Adrienn"},
    {"name": "Malchous Forest Park", "point": "Adrienn"},
    {"name": "Lapis Ward", "point": "Adrienn"},
    {"name": "Azurine Lake", "point": "Adrienn"},
    {"name": "Azurine Cave", "point": "Adrienn"},
    {"name": "Coral Lighthouse", "point": "Adrienn"},
    {"name": "Tourmaline Desert", "point": "Titania"},
    {"name": "Mirage Tower", "point": "Titania"},
    {"name": "Sugiline Cave", "point": "Titania"},
    {"name": "Sugiline Ruin", "point": "Titania"},
    {"name": "Teknite Cave", "point": "Titania"},
    {"name": "1R253 Scrapyard", "point": "Titania"},
    {"name": "Desert Town", "point": "Titania"},
    {"name": "Once Upon a Somewhere/Waste of Time", "point": "Titania"},
    {"name": "Teknite Ridge", "point": "Hardy"},
    {"name": "Charous Mountain", "point": "Hardy"},
    {"name": "Agate City", "point": "Hardy"},
    {"name": "Charous Path", "point": "Elite 4/Champion"},
    {"name": "Victory Road", "point": "Elite 4/Champion"},
    {"name": "Aegir Cave Depths", "point": "Post-Champion"},
    {"name": "Aegir Cave", "point": "Post-Champion"},
    {"name": "Ametrine Core", "point": "Post-Champion"},
    {"name": "Cauldron of the Future", "point": "Post-Champion"},
    {"name": "Chrysolia Deepwoods", "point": "Post-Champion"},
    {"name": "Citae Prisma", "point": "Post-Champion"},
    {"name": "Endgame", "point": "Post-Champion"},
    {"name": "Idyll of Panaceance", "point": "Post-Champion"},
    {"name": "Idyll of Pestilence", "point": "Post-Champion"},
    {"name": "Rhodochrine Tree", "point": "Post-Champion"},
    {"name": "Manyworld Forest", "point": "Post-Champion"},
    {"name": "Manyworld Pool", "point": "Post-Champion"},
    {"name": "Mirage Tower?", "point": "Post-Champion"},
    {"name": "Neoteric Isle", "point": "Post-Champion"},
    {"name": "New World", "point": "Post-Champion"},
    {"name": "Splash Grounds", "point": "Post-Champion"},
    {"name": "Twilight Desert", "point": "Post-Champion"},
    {"name": "Unexplored Territory", "point": "Post-Champion"},
    {"name": "Vacant Past", "point": "Post-Champion"}
]

locationRemap = {
    "Obsidia Slums B1F": "Obsidia Slums",
    "Obsidia Slums 1F": "Obsidia Slums",
    "Obsidia Slums 2F": "Obsidia Slums",
    "Obsidia Park": "Obsidia Ward",
    "Lapis Water Grid": "Water Treatment Center",
    "Central Obsidia Water Grid": "Water Treatment Center",
    "North Obsidia Water Grid": "Water Treatment Center",
    "Onyx Water Grid": "Water Treatment Center",
    "Coral Water Grid": "Water Treatment Center",
    "Opal Water Grid": "Water Treatment Center",
    "Peridot Water Grid": "Water Treatment Center",
    "Jasper Water Grid": "Water Treatment Center",
    "Beryl Water Grid": "Water Treatment Center",
    "Apophyll Cave 2F": "Apophyll Cave",
    "Grand Stairway B1F": "Grand Stairway",
    "Grand Stairway B2F": "Grand Stairway",
    "Grand Stairway B3F": "Grand Stairway",
    "Mt Moon": "Glitch World",
    "Cerulean Cave": "Glitch World",
    "Byxbysion Grotto": "Byxbysion Tunnels",
    "Hidden Tunnel": "Byxbysion Tunnels",
    "Pyrous Mountain B1F": "Pyrous Mountain",
    "Pyrous Mountain 1F": "Pyrous Mountain",
    "Pyrous Mountain 2F": "Pyrous Mountain",
    "Pyrous Mountain 3F": "Pyrous Mountain",
    "Pyrous Mountain B2F - Sp.Atk EVs": "Pyrous Mountain",
    "Ruby Cave": "Route 3 Caves",
    "Sapphire Cave": "Route 3 Caves",
    "Emerald Cave": "Route 3 Caves",
    "Amethyst Cave": "Route 3 Caves",
    "Beryl Cave 1F": "Beryl Cave",
    "Beryl Cave B1F": "Beryl Cave",
    "Beryl Cave B2F": "Beryl Cave",
    "Chrysolia Spring 1F": "Chrysolia Spring",
    "Chrysolia Spring B1F": "Chrysolia Spring",
    "Chrysolia Spring Sauna": "Chrysolia Spring",
    "Teknite Cave 1F": "Teknite Cave",
    "Teknite Cave 2F": "Teknite Cave",
    "Teknite Cave 3F": "Teknite Cave",
    "Teknite Cave 4F": "Teknite Cave",
    "Teknite Cave 3-4F": "Teknite Cave",
    "Sugiline Cave B1F": "Sugiline Cave",
    "Sugiline Ruin B1F": "Sugiline Ruin",
    "Mirage Tower B1F": "Mirage Tower",
    "Ametrine Mountain B1F": "Ametrine Mountain",
    "Ametrine Mountain B2F": "Ametrine Mountain",
    "Ametrine Mountain B3F": "Ametrine Mountain",
    "Ametrine Mountain B4F": "Ametrine Mountain",
    "Ametrine Mountain 1F": "Ametrine Mountain",
    "Ametrine Mountain 2F": "Ametrine Mountain",
    "Ametrine Mountain 3F": "Ametrine Mountain",
    "Ametrine Mountain 4F": "Ametrine Mountain",
    "Ametrine Mountain 5F": "Ametrine Mountain",
    "Ametrine Mountain 6F": "Ametrine Mountain",
    "Ametrine Mountain 7F": "Ametrine Mountain",
    "Ametrine Mountain 8F": "Ametrine Mountain",
    "Celestinine Mountain B1F": "Celestinine Mountain",
    "Celestinine Mountain B2F": "Celestinine Mountain",
    "Celestinine Mountain B3F": "Celestinine Mountain",
    "Celestinine Mountain 1F": "Celestinine Mountain",
    "Celestinine Mountain 2F": "Celestinine Mountain",
    "Celestinine Mountain 3F": "Celestinine Mountain",
    "Celestinine Mountain 4F": "Celestinine Mountain",
    "Charous Mountain B1F": "Charous Mountain",
    "Charous Mountain B2F": "Charous Mountain",
    "Citrine Mountain 1F": "Citrine Mountain",
    "Citrine Mountain 2F": "Citrine Mountain",
    "Citrine Mountain 3F": "Citrine Mountain",
    "Once Upon a Somewhere": "Once Upon a Somewhere/Waste of Time",
    "Once Upon a Waste of Time": "Once Upon a Somewhere/Waste of Time",
    "Victory Road 2F": "Victory Road",
    "Victory Road B1F": "Victory Road",
    "Victory Road B2F": "Victory Road",
    "Victory Road B3F": "Victory Road",
    "Victory Road B4F": "Victory Road",
    "Victory Road B5F": "Victory Road",
    "New World - Regis": "New World",
    "New World - Victini": "New World",
    "New World Helix": "New World"
}

pointOfNoReturn = [
    "Agate Circus",
    "Route 2",
    "Ametrine Mountain",
    "Celestinine Cascade",
    "Route 3",
    "Route 3 Caves",
    "Route 4",
    "Calcenon City",
    "Ametrine City",
    "Glitch World",
    "Water Treatment Center"
]

locationNumRemap = {
    "041": "Peridot Underground Railnet",
    "103": "Obsidia Underground Railnet",
    "447": "Glitch World",
    "450": "Glitch World",
    "453": "Glitch World"
}

mapRepoint = {
    "151": "Corey",
    "228": "Serra",
    "229": "Serra",
    "281": "Adrienn",
    "371": "Adrienn",
    "379": "Hardy",
    "513": "Adrienn",
    "519": "Adrienn",
    "520": "Adrienn",
    "522": "Adrienn",
    "523": "Adrienn",
    "524": "Adrienn",
    "525": "Adrienn",
    "526": "Adrienn",
    "528": "Adrienn",
    "529": "Adrienn",
    "530": "Adrienn",
    "532": "Adrienn",
    "533": "Adrienn",
    "544": "Adrienn",
    "545": "Adrienn",
    "546": "Adrienn",
    "550": "Adrienn",
    "551": "Adrienn",
    "552": "Adrienn",
    "562": "Adrienn",
    "563": "Adrienn",
    "564": "Adrienn",
    "565": "Adrienn",
    "566": "Adrienn",
    "567": "Adrienn",
    "568": "Adrienn",
    "569": "Adrienn",
    "570": "Adrienn",
    "573": "Adrienn",
    "585": "Adrienn",
    "586": "Adrienn",
    "608": "Adrienn",
    "614": "Adrienn",
    "615": "Adrienn",
    "616": "Adrienn",
    "618": "Adrienn",
    "710": "Hardy",
    "711": "Hardy",
    "712": "Hardy",
    "713": "Hardy",
    "714": "Hardy",
    "715": "Hardy",
    "716": "Saphira",
    "717": "Hardy",
    "718": "Hardy",
    "719": "Hardy",
    "720": "Hardy",
    "721": "Hardy",
    "722": "Hardy",
    "723": "Hardy",
    "724": "Hardy",
    "725": "Hardy",
    "726": "Hardy",
    "727": "Hardy",
    "728": "Hardy",
    "729": "Hardy",
    "742": "Hardy",
    "760": "Adrienn",
    "792": "Elite 4/Champion"
}

alolanLocations = {
    "Rattata": [170, 524],
    "Raticate": [170, 524],
    "Sandshrew": [364, 366, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 390, 396, 430, 433, 434, 440, 441, 442],
    "Sandslash": [364, 366, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 390, 396, 430, 433, 434, 440, 441, 442, 749, 750],
    "Vulpix": [439],
    "Ninetales": [439, 721, 723, 725, 726, 727, 729],
    "Diglett": [33, 34, 35, 199, 201, 202, 203, 204],
    "Dugtrio": [33, 34, 35, 199, 201, 202, 203, 204],
    "Meowth": [170, 524],
    "Persian": [170, 524],
    "Geodude": [231, 247, 251, 258, 259, 260, 261, 262, 263, 264, 340, 341, 342, 343, 344, 346, 347, 348, 349, 371, 614, 615, 616, 618],
    "Graveler": [231, 247, 251, 258, 259, 260, 261, 262, 263, 264, 340, 341, 342, 343, 344, 346, 347, 348, 349, 371, 614, 615, 616, 618],
    "Golem": [231, 247, 251, 258, 259, 260, 261, 262, 263, 264, 340, 341, 342, 343, 344, 346, 347, 348, 349, 371, 614, 615, 616, 618],
    "Grimer": [467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505],
    "Muk": [467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505],
    "Marowak": [669]
}

tmTutorExclusions = {
    "Rattata": ["SLUDEGEBOMB", "TORMENT", "QUASH", "EMBARGO", "SHADOWCLAW", "SNARL", "DARKPULSE", "SNATCH"],
    "Rattata (Alolan)": ["WORKUP", "THUNDERBOLT", "THUNDER", "CHARGEBEAM", "THUNDERWAVE", "WILDCHARGE"],
    "Raticate": ["SLUDEGEBOMB", "TORMENT", "QUASH", "EMBARGO", "SHADOWCLAW", "SNARL", "DARKPULSE", "BULKUP", "VENOSHOCK", "SLUDGEWAVE", "SNATCH", "KNOCKOFF"],
    "Raticate (Alolan)": ["WORKUP", "THUNDERBOLT", "THUNDER", "CHARGEBEAM", "THUNDERWAVE", "WILDCHARGE"],
    "Raichu": ["PSYSHOCK", "CALMMIND", "SAFEGUARD", "PSYCHIC", "REFLECT", "MAGICCOAT", "MAGICROOM", "RECYCLE", "TELEKINESIS", "ALLYSWITCH"],
    "Sandshrew": ["WORKUP", "HAIL", "BLIZZARD", "LEECHLIFE", "FROSTBREATH", "IRONHEAD", "ICEPUNCH", "IRONDEFENSE", "ICYWIND", "AQUATAIL", "THROATCHOP"],
    "Sandshrew (Alolan)": ["SANDSTORM", "ROCKTOMB", "EARTHPOWER", "STOMPINGTANTRUM"],
    "Sandslash": ["WORKUP", "HAIL", "BLIZZARD", "LEECHLIFE", "AURORAVEIL", "FROSTBREATH", "IRONHEAD", "THROATCHOP", "ICEPUNCH", "IRONDEFENSE", "ICYWIND", "AQUATAIL"],
    "Sandslash (Alolan)": ["SANDSTORM", "ROCKTOMB", "STONEDGE", "EARTHPOWER", "STOMPINGTANTRUM"],
    "Vulpix": ["HAIL", "ICEBEAM", "BLIZZARD", "RAINDANCE", "AURORAVEIL", "FROSTBREATH", "ICYWIND", "AQUATAIL", "HEALBELL"],
    "Vulpix (Alolan)": ["SUNNYDAY", "FLAMETHROWER", "FIREBLAST", "FLAMECHARGE", "OVERHEAT", "ENERGYBALL", "WILLOWISP", "HEATWAVE"],
    "Ninetales": ["HAIL", "ICEBEAM", "BLIZZARD", "RAINDANCE", "AURORAVEIL", "FROSTBREATH", "DAZZLINGGLEAM", "ICYWIND", "AQUATAIL", "WONDERROOM", "HEALBELL"],
    "Ninetales (Alolan)": ["SUNNYDAY", "FLAMETHROWER", "FIREBLAST", "FLAMECHARGE", "OVERHEAT", "ENERGYBALL", "WILLOWISP", "SOLARBEAM", "HEATWAVE"],
    "Diglett": ["WORKUP", "FLASHCANNON", "IRONDEFENSE", "IRONHEAD"],
    "Dugtrio": ["WORKUP", "FLASHCANNON", "IRONDEFENSE", "IRONHEAD"],
    "Meowth": ["QUASH", "EMBARGO"],
    "Persian": ["QUASH", "SNARL"],
    "Geodude": ["THUNDERBOLT", "THUNDER", "CHARGEBEAM", "BRUTALSWING", "VOLTSWITCH", "MAGNETRISE", "ELECTROWEB"],
    "Graveler": ["THUNDERBOLT", "THUNDER", "CHARGEBEAM", "BRUTALSWING", "VOLTSWITCH", "MAGNETRISE", "ELECTROWEB", "SHOCKWAVE", "ALLYSWITCH"],
    "Golem": ["THUNDERBOLT", "THUNDER", "CHARGEBEAM", "BRUTALSWING", "VOLTSWITCH", "ECHOEDVOICE", "WILDCHARGE", "MAGNETRISE", "ELECTROWEB", "SHOCKWAVE", "ALLYSWITCH"],
    "Grimer": ["BRUTALSWING", "QUASH", "EMBARGO", "ROCKPOLISH", "STONEDGE", "SNARL", "KNOCKOFF", "GASTROACID", "SPITE"],
    "Grimer (Alolan)": ["THUNDERBOLT", "THUNDER"],
    "Muk": ["BRUTALSWING", "QUASH", "EMBARGO", "ROCKPOLISH", "STONEDGE", "SNARL", "KNOCKOFF", "GASTROACID", "SPITE", "RECYCLE"],
    "Muk (Alolan)": ["THUNDERBOLT", "THUNDER"],
    "Exeggutor": ["EARTHQUAKE", "BRICKBREAK", "FLAMETHROWER", "BRUTALSWING", "BULLDOZE", "DRAGONTAIL", "IRONHEAD", "SUPERPOWER", "DRAGONPULSE", "IRONTAIL", "KNOCKOFF", "OUTRAGE", "DRACOMETEOR"],
    "Marowak": ["RAINDANCE", "THUNDERBOLT", "THUNDER", "SHADOWBALL", "FLAMECHARGE", "WILLOWISP", "DREAMEATER", "DARKPULSE", "HEATWAVE", "PAINSPLIT", "SPITE", "ALLYSWITCH"],
    "Lycanroc": ["DUALCHOP", "UPROAR", "THUNDERPUNCH", "FIREPUNCH", "FOULPLAY", "FOCUSPUNCH", "THROATCHOP", "LASERFOCUS", "OUTRAGE"],
    "Lycanroc (Midnight Form)": ["DRILLRUN"],
    "Lycanroc (Dusk Form)": ["DUALCHOP", "UPROAR", "THUNDERPUNCH", "FIREPUNCH", "FOULPLAY", "FOCUSPUNCH", "THROATCHOP", "LASERFOCUS"]
}

pokemonRename = {
    "Nidoranma": "Nidoran♂",
    "Nidoranfe": "Nidoran♀",
    "Farfetchd": "Farfetch'd",
    "Mimejr": "Mime Jr.",
    "Mrmime": "Mr. Mime",
    "Typenull": "Type:Null",
    "Tapukoko": "Tapu Koko",
    "Tapulele": "Tapu Lele",
    "Tapubulu": "Tapu Bulu",
    "Tapufini": "Tapu Fini"
}

pokemonRenumber = {
    "Mega Venusaur": 10033,
    "Mega Charizard X": 10034,
    "Mega Charizard Y": 10035,
    "Mega Blastoise": 10036,
    "Mega Beedrill": 10090,
    "Mega Pidgeot": 10073,
    "Rattata (Alolan)": 10091,
    "Raticate (Alolan)": 10092,
    "Raichu (Alolan)": 10100,
    "Sandshrew (Alolan)": 10101,
    "Sandslash (Alolan)": 10102,
    "Vulpix (Alolan)": 10103,
    "Ninetales (Alolan)": 10104,
    "Diglett (Alolan)": 10105,
    "Dugtrio (Alolan)": 10106,
    "Meowth (Alolan)": 10107,
    "Meowth (Galarian)": 10158,
    "Persian (Alolan)": 10108,
    "Mega Alakazam": 10037,
    "Geodude (Alolan)": 10109,
    "Graveler (Alolan)": 10110,
    "Golem (Alolan)": 10111,
    "Ponyta (Galarian)": 10159,
    "Rapidash (Galarian)": 10160,
    "Slowpoke (Galarian)": 10161,
    "Mega Slowbro": 10071,
    "Farfetch’d (Galarian)": 10163,
    "Grimer (Alolan)": 10112,
    "Muk (Alolan)": 10113,
    "Mega Gengar": 10038,
    "Exeggutor (Alolan)": 10114,
    "Marowak (Alolan)": 10115,
    "Weezing (Galarian)": 10164,
    "Mega Kangaskhan": 10039,
    "Mr. Mime (Galarian)": 10165,
    "Mega Pinsir": 10040,
    "Mega Gyarados": 10041,
    "Mega Aerodactyl": 10042,
    "Mega Mewtwo X": 10043,
    "Mega Mewtwo Y": 10044,
    "Mega Ampharos": 10045,
    "Mega Steelix": 10072,
    "Mega Scizor": 10046,
    "Mega Heracross": 10047,
    "Corsola (Galarian)": 10170,
    "Mega Houndoom": 10048,
    "Mega Tyranitar": 10049,
    "Mega Sceptile": 10065,
    "Mega Blaziken": 10050,
    "Mega Swampert": 10064,
    "Zigzagoon (Galarian)": 10171,
    "Linoone (Galarian)": 10172,
    "Mega Gardevoir": 10051,
    "Mega Sableye": 10066,
    "Mega Mawile": 10052,
    "Mega Aggron": 10053,
    "Mega Medicham": 10054,
    "Mega Manectric": 10055,
    "Mega Sharpedo": 10070,
    "Mega Camerupt": 10087,
    "Mega Altaria": 10067,
    "Castform (Sunny Form)": 10013,
    "Castform (Rainy Form)": 10014,
    "Castform (Snowy Form)": 10015,
    "Mega Banette": 10056,
    "Mega Absol": 10057,
    "Mega Glalie": 10074,
    "Mega Salamence": 10089,
    "Mega Metagross": 10076,
    "Mega Latias": 10062,
    "Mega Latios": 10063,
    "Primal Kyogre": 10077,
    "Primal Groudon": 10078,
    "Mega Rayquaza": 10079,
    "Deoxys (Attack Forme)": 10001,
    "Deoxys (Defense Forme)": 10002,
    "Deoxys (Speed Forme)": 10003,
    "Burmy (Sandy Cloak)": 10027,
    "Burmy (Trash Cloak)": 10028,
    "Wormadam (Sandy Cloak)": 10004,
    "Wormadam (Trash Cloak)": 10005,
    "Mega Lopunny": 10088,
    "Mega Garchomp": 10058,
    "Mega Lucario": 10059,
    "Mega Abomasnow": 10060,
    "Mega Gallade": 10068,
    "Heat Rotom": 10008,
    "Wash Rotom": 10009,
    "Frost Rotom": 10010,
    "Fan Rotom": 10011,
    "Mow Rotom": 10012,
    "Giratina (Origin Forme)": 10007,
    "Shaymin (Sky Forme)": 10006,
    "Mega Audino": 10069,
    "Darumaka (Galarian)": 10173,
    "Darmanitan (Zen Mode)": 10017,
    "Darmanitan (Galarian)": 10174,
    "Yamask (Galarian)": 10176,
    "Stunfisk (Galarian)": 10177,
    "Tornadus (Therian Forme)": 10019,
    "Thundurus (Therian Forme)": 10020,
    "Landorus (Therian Forme)": 10021,
    "White Kyurem": 10023,
    "Black Kyurem": 10022,
    "Keldeo (Resolute Form)": 10024,
    "Meloetta (Pirouette Forme)": 10018,
    "Meowstic (Female)": 10025,
    "Aegislash (Blade Forme)": 10026,
    "Pumpkaboo (Super Size)": 710,
    "Gourgeist (Super Size)": 711,
    "Floette (Eternal Flower)": 10029,
    "Zygarde (10 Forme)": 10118,
    "Zygarde (Complete Forme)": 10120,
    "Mega Diancie": 10075,
    "Hoopa Unbound": 10086,
    "Oricorio (Pom-Pom Style)": 10123,
    "Oricorio (Pa'u Style)": 10124,
    "Oricorio (Sensu Style)": 10125,
    "Lycanroc (Midnight Form)": 10126,
    "Lycanroc (Dusk Form)": 10152,
    "Wishiwashi (School Form)": 10127,
    "Necrozma (Dusk Mane)": 10155,
    "Necrozma (Dawn Wings)": 10156,
    "Ultra Necrozma": 10157
}

bannedLocations = [
    "REMOVED",
    "Wasteland Wall"
]

bannedForms = [
    "Pichu (Spiky-Eared)",
    "Unown (B)",
    "Unown (C)",
    "Unown (D)",
    "Unown (E)",
    "Unown (F)",
    "Unown (G)",
    "Unown (H)",
    "Unown (I)",
    "Unown (J)",
    "Unown (K)",
    "Unown (L)",
    "Unown (M)",
    "Unown (N)",
    "Unown (O)",
    "Unown (P)",
    "Unown (Q)",
    "Unown (R)",
    "Unown (S)",
    "Unown (T)",
    "Unown (U)",
    "Unown (V)",
    "Unown (W)",
    "Unown (X)",
    "Unown (Y)",
    "Unown (Z)",
    "Unown (?)",
    "Unown (!)",
    "Sunshine Form",
    "East Sea",
    "Fighting Type",
    "Flying Type",
    "Poison Type",
    "Ground Type",
    "Rock Type",
    "Bug Type",
    "Ghost Type",
    "Steel Type",
    "Unknown Type",
    "Fire Type",
    "Water Type",
    "Grass Type",
    "Electric Type",
    "Psychic Type",
    "Ice Type",
    "Dragon Type",
    "Dark Type",
    "Fairy Type",
    "Basculin (Blue-Striped)",
    "Summer Form",
    "Autumn Form",
    "Winter Form",
    "Shock Drive",
    "Chill Drive",
    "Burn Drive",
    "Douse Drive",
    "Greninja (Ash-Greninja)",
    "Continental Pattern",
    "Elegant Pattern",
    "Garden Pattern",
    "High Plains Pattern",
    "Icy Snow Pattern",
    "Jungle Pattern",
    "Marine Pattern",
    "Meadow Pattern",
    "Modern Pattern",
    "Monsoon Pattern",
    "Ocean Pattern",
    "Polar Pattern",
    "River Pattern",
    "Sandstorm Pattern",
    "Savanna Pattern",
    "Sun Pattern",
    "Tundra Pattern",
    "Fancy Pattern",
    "Pok Ball Pattern",
    "Yellow Flower",
    "Orange Flower",
    "Blue Flower",
    "White Flower",
    "Heart Trim",
    "Star Trim",
    "Diamond Trim",
    "Debutante Trim",
    "Matron Trim",
    "Dandy Trim",
    "La Reine Trim",
    "Kabuki Trim",
    "Pharaoh Trim",
    "Pumpkaboo",
    "Gourgeist",
    "Average Size",
    "Large Size",
    "Active Mode",
    "Type: Fighting",
    "Type: Flying",
    "Type: Poison",
    "Type: Ground",
    "Type: Rock",
    "Type: Bug",
    "Type: Ghost",
    "Type: Steel",
    "Type: Unknown",
    "Type: Fire",
    "Type: Water",
    "Type: Grass",
    "Type: Electric",
    "Type: Psychic",
    "Type: Ice",
    "Type: Dragon",
    "Type: Dark",
    "Type: Fairy",
    "Red Core",
    "Orange Core",
    "Yellow Core",
    "Green Core",
    "Blue Core",
    "Indigo Core",
    "Violet Core",
    "Busted Form",
    "Original Color"
]

appendForms = [
    "Sunny Form",
    "Rainy Form",
    "Snowy Form",
    "Attack Forme",
    "Defense Forme",
    "Speed Forme",
    "Sandy Cloak",
    "Trash Cloak",
    "Origin Forme",
    "Sky Forme",
    "Zen Mode",
    "Therian Forme",
    "Resolute Form",
    "Pirouette Forme",
    "Blade Forme",
    "Super Size",
    "Eternal Flower",
    "10 Forme",
    "Complete Forme",
    "Pom-Pom Style",
    "Pa'u Style",
    "Sensu Style",
    "Midnight Form",
    "Dusk Form",
    "School Form",
    "Dusk Mane",
    "Dawn Wings"
]


def inListOfDict(dList, key, value):
    for d in dList:
        if d[key] == value:
            return True
    return False


def alolanExclusion(name, mapNo):
    return True if int(mapNo) in alolanLocations.get(name, []) else False


def getName(name, mapNo):
    return f"{name} (Alolan)" if alolanExclusion(
        name, mapNo) else name.capitalize()


def correctLocation(mapStr):
    mapNo = mapStr.split("#")[0].strip()
    loc = mapStr.split("#")[1].strip()
    correctLoc = locationRemap.get(loc, loc)
    if mapNo in locationNumRemap:
        correctLoc = locationNumRemap[mapNo]
    return (correctLoc, mapNo)


def getPoint(location, method, mapNo):
    locationPt = ""
    methodPt = ""
    if mapNo in mapRepoint:
        locationPt = mapRepoint[mapNo]
    else:
        for loc in locations:
            if loc["name"] == location:
                locationPt = loc["point"]
    for mth in methods:
        if mth["name"] == method:
            methodPt = mth["point"]
    if locationPt and not methodPt:
        return locationPt
    if methodPt and not locationPt:
        return methodPt
    if methodPt and locationPt:
        locationLv = "1"
        methodLv = "1"
        for pt in points:
            if pt["name"] == locationPt:
                locationLv = pt["level"]
            if pt["name"] == methodPt:
                methodLv = pt["level"]
        # Can't surf in areas outside of Point of No Return until Adrienn
        if method == "Water" and location not in pointOfNoReturn and int(locationLv) < int(methodLv):
            locationPt = "Adrienn"
            locationLv = "80"
        return locationPt if int(locationLv) > int(methodLv) else methodPt
    return ""


# Player can reach Citrine Mountain F2 at Shade, but no other floor or fishing
def handleMap382(locationsList, method):
    locationPt = ""
    if method == "Cave":
        locationPt = "Shade"
    elif method in ["OldRod", "GoodRod"]:
        locationPt = "Samson"
    elif method == "Water":
        locationPt = "Charlotte"
    elif method == "SuperRod":
        locationPt = "Adrienn"
    for loc in locationsList:
        if loc["location"] == "Citrine Mountain":
            locationLv = "1"
            ogLocationLv = "1"
            for pt in points:
                if pt["name"] == locationPt:
                    locationLv = pt["level"]
                if pt["name"] == loc["point"]:
                    ogLocationLv = pt["level"]
            loc["point"] = locationPt if locationLv < ogLocationLv else loc["point"]


class StrictConfigParser(ConfigParser):

    def __init__(self):
        super().__init__(allow_no_value=True)

    def _read(self, fp, fpname):
        cursect = None                        # None, or a dictionary
        optname = None
        lineno = 0
        e = None                              # None, or an exception
        while True:
            line = ''.join(char for char in fp.readline()
                           if char in printable).replace("%", '')
            if not line:
                break
            lineno = lineno + 1
            # comment or blank line?
            if line.strip() == '' or line[0] in '#;':
                continue
            if line.split(None, 1)[0].lower() == 'rem' and line[0] in "rR":
                # no leading whitespace
                continue
            # continuation line?
            if line[0].isspace() and cursect is not None and optname:
                value = line.strip()
                if value:
                    cursect[optname].append(value)
            # a section header or option header?
            else:
                # is it a section header?
                mo = self.SECTCRE.match(line)
                if mo:
                    sectname = mo.group('header')
                    if sectname == DEFAULTSECT:
                        cursect = self._defaults
                    else:
                        cursect = self._dict()
                        cursect['__name__'] = sectname
                        self._sections[sectname] = cursect
                    # So sections can't start with a continuation line
                    optname = None
                # no section header in the file?
                elif cursect is None:
                    raise MissingSectionHeaderError(fpname, lineno, line)
                # an option line?
                else:
                    try:
                        mo = self._optcre.match(line)   # 2.7
                    except AttributeError:
                        mo = self.OPTCRE.match(line)    # 2.6
                    if mo:
                        optname, vi, optval = mo.group('option', 'vi', 'value')
                        optname = self.optionxform(optname.rstrip())
                        # This check is fine because the OPTCRE cannot
                        # match if it would set optval to None
                        if optval is not None:
                            if vi in ('=', ':') and ';' in optval:
                                # ';' is a comment delimiter only if it follows
                                # a spacing character
                                pos = optval.find(';')
                                if pos != -1 and optval[pos - 1].isspace():
                                    optval = optval[:pos]
                            optval = optval.strip()
                            # allow empty values
                            if optval == '""':
                                optval = ''
                            cursect[optname] = [optval]
                        else:
                            # valueless option handling
                            cursect[optname] = optval
                    else:
                        # a non-fatal parsing error occurred.  set up the
                        # exception but keep going. the exception will be
                        # raised at the end of the file and will contain a
                        # list of all bogus lines
                        if not e:
                            e = ParsingError(fpname)
                        e.append(lineno, repr(line))
        # if any parsing errors occurred, raise an exception
        if e:
            raise e

        # join the multi-line values collected while reading
        all_sections = [self._defaults]
        all_sections.extend(self._sections.values())
        for options in all_sections:
            for name, val in options.items():
                if isinstance(val, list):
                    options[name] = '\n'.join(val)

    def dget(self, section, option, default=None, type=str):
        if not self.has_option(section, option):
            return default
        if type is str:
            return self.get(section, option)
        elif type is int:
            return self.getint(section, option)
        elif type is bool:
            return self.getboolean(section, option)
        else:
            raise NotImplementedError()


cfg = StrictConfigParser()
with open("pokemon.txt", encoding="utf-8") as f:
    cfg.read_file(f)


pokemonData = {}

for section in cfg.sections():
    pokemonData[section] = {}
    for name, value in cfg.items(section):
        pokemonData[section][name] = [x.strip() for x in value.split() if x]
        if len(pokemonData[section][name]) == 1:
            pokemonData[section][name] = pokemonData[section][name][0]
        elif len(pokemonData[section][name]) == 0:
            pokemonData[section][name] = ''

cfg2 = StrictConfigParser()
with open("pokemonforms.txt", encoding="utf-8") as f:
    cfg2.read_file(f)

pokemonForms = {}

for section in cfg2.sections():
    sectionName = section.split(",")[0].capitalize()
    if not pokemonForms.get(sectionName):
        pokemonForms[sectionName] = []
    formData = {}
    for name, value in cfg2.items(section):
        formData[name] = [x.strip()
                          for x in value.split() if x]
        if len(formData[name]) == 1:
            formData[name] = formData[name][0]
        elif len(formData[name]) == 0:
            formData[name] = ''
    pokemonForms[sectionName].append(formData)

cfg3 = StrictConfigParser()
with open("tm.txt", encoding="utf-8") as f:
    cfg3.read_file(f)

tmTutorData = {}

for section in cfg3.sections():
    for name, value in cfg3.items(section):
        vals = name.split(",")
        for val in vals:
            pkname = val.capitalize()
            if pkname in pokemonRename:
                pkname = pokemonRename[pkname.capitalize()]
            if not tmTutorData.get(pkname):
                tmTutorData[pkname] = []
            tmTutorData[pkname].append(section)


pokemonMap = {}
lastMethod = ""
lastLocation = ""
lastMapNo = ""
with open('encounters.txt') as f:
    for line in f:
        firstPart = line.split(",")[0]
        capFirstPart = firstPart.capitalize()
        if "#" in line:
            lastLocation, lastMapNo = correctLocation(line)
        elif "," in line and firstPart.isalpha():
            pkName = getName(capFirstPart, lastMapNo)
            if pkName in pokemonRename:
                pkName = pokemonRename[pkName]
            if pkName not in pokemonMap:
                pokemonMap[pkName] = {"locations": []}
            if lastMapNo == "382":
                handleMap382(pokemonMap[pkName]["locations"], lastMethod)
            elif not inListOfDict(pokemonMap[pkName]["locations"], "location", lastLocation) and \
                    lastLocation not in bannedLocations:
                # Add the location to the list
                pokemonMap[pkName]["locations"].append({"location": lastLocation, "point": getPoint(
                    lastLocation, lastMethod, lastMapNo), "method": lastMethod})
        elif "," not in line:
            lastMethod = line.strip()

for key, value in eventLocations.items():
    if not pokemonMap.get(key):
        pokemonMap[key] = {}
    if not pokemonMap[key].get("locations"):
        pokemonMap[key]["locations"] = []
    if isinstance(value, dict):
        pokemonMap[key]["locations"].append(value)
    else:
        pokemonMap[key]["locations"].extend(value)

contents = []
gen = 1
subgen = 0
for head, pk in pokemonData.items():
    if len(contents) > 74 or int(head) in [152, 252, 387, 494, 650, 722]:
        with open(f'gen{gen}_{subgen}.ts', 'w+') as f:
            f.write(f"import {{ Pokemon }} from '@/interfaces/pokemon_interfaces';\n \
                    export const pokemonData{gen}{subgen}: Pokemon[] = {json.dumps(contents)}")
            contents = []
        if int(head) in [152, 252, 387, 494, 650, 722]:
            subgen = 0
            gen += 1
        else:
            subgen += 1
    if pk["internalname"].capitalize() in pokemonRename:
        pk["name"] = pokemonRename[pk["internalname"].capitalize()]
    if pk["name"] not in bannedForms:
        try:
            locs = pokemonMap.get(pk["name"], {"locations": []})['locations']
        except Exception as e:
            raise ValueError(''.join(pk["name"]) +
                             " was unable to obtain locations")
        types = [pk["type1"].capitalize()]
        if pk.get("type2"):
            types.append(pk["type2"].capitalize())
        eggMoves = pk.get('eggmoves', '')
        eggMoves = eggMoves.split(',') if eggMoves else []
        lvMoves = {}
        it = iter(pk['moves'].split(","))
        for x in it:
            if not lvMoves.get(int(x)):
                lvMoves[int(x)] = []
            lvMoves[int(x)].append(next(it))
        contents.append({"no": int(head),
                        "name": pk['name'],
                         "types": types,
                         "stats": [int(stat) for stat in pk['basestats'].split(",")],
                         "levelUpMoves": lvMoves,
                         "eggMoves": eggMoves,
                         "tmTutorMoves": [mv for mv in tmTutorData.get(pk['name'], []) if mv not in tmTutorExclusions.get(pk['name'], [])],
                         "locations": locs
                         })

    # Check for forms
    for form in pokemonForms.get(pk["name"], []):
        if not form.get("formname"):
            continue
        formName = ' '.join(form['formname'])
        if isinstance(form["formname"], str):
            formName = f"{pk['name']} ({form['formname']})"
        if formName in bannedForms:
            continue
        if formName in appendForms:
            formName = f"{pk['name']} ({formName})"
        formTypes = [form.get("type1", pk["type1"]).capitalize()]
        try:
            formLocs = pokemonMap.get(formName, {"locations": []})[
                'locations']
        except Exception as e:
            raise ValueError(formName + " was unable to obtain locations")
        # Only append a 2nd type if the form declares a type 1 and has a type 2
        # OR the form DOES NOT declare a type 1 but the base form has a type 2
        if (form.get("type1") and form.get("type2")) or \
                (not form.get("type1") and pk.get("type2")):
            formTypes.append(
                form.get("type2", pk.get("type2")).capitalize())
        formEggMoves = form.get('eggmoves', '')
        formEggMoves = formEggMoves.split(',') if formEggMoves else []
        formLvMoves = {}
        it = iter(form.get('moves', pk['moves']).split(","))
        for x in it:
            if not formLvMoves.get(int(x)):
                formLvMoves[int(x)] = []
            formLvMoves[int(x)].append(next(it))
        contents.append({"no": pokemonRenumber.get(formName, "BADVAL"),
                         "name": formName,
                         "types": formTypes,
                         "stats": [int(stat) for stat in form.get('basestats', pk['basestats']).split(",")],
                         "levelUpMoves": formLvMoves,
                         "eggMoves": formEggMoves,
                         "tmTutorMoves": [mv for mv in tmTutorData.get(pk['name'], []) if mv not in tmTutorExclusions.get(formName, [])],
                         "locations": formLocs
                         })

with open(f'gen{gen}_{subgen}.ts', 'w+') as f:
    f.write(f"import {{ Pokemon }} from '@/interfaces/pokemon_interfaces';\n \
            export const pokemonData{gen}{subgen}: Pokemon[] = {json.dumps(contents)}")

# with open("json_encounters.json", 'w+') as fl:
#    (json.dump(pokemonMap, fl, ensure_ascii=False))

# with open("locations.txt") as f2:
#     with open("locations2.txt", 'w+') as fil:
#         pattern = re.compile(r'[\"\,\n]+')
#         for loc in f2:
#             fil.write(
#                 f"{{\"name\":\"{ pattern.sub('', loc ) }\", \"point\": \"\"}},\n")


with open("tm_locations.ts", 'w+') as f:
    f.write(f"export const tmLocations = {json.dumps(tmLocations)};")
    f.write(f"export const tutorLocations = {json.dumps(tutorLocations)};")
