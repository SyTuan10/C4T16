anime = {
    "Pikachu" : "All Pikachu in Alola will evolve into this form regardless of their origin",
    "Raichu" : "It has a regional variant that is Electric/Psychic"
}

while True:
    n = str.upper(input("Enter Pokemon Name : "))
    if n == "PIKACHU":
        print(anime["Pikachu"])
    if n == "RAICHU":
        print(anime["Raichu"])