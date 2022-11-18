

print("Pokemon Starter Personality Quiz")
player_name = input("Please enter your name: ")

starters = {"Charmander", "Squirtle", "Balbasaur", "Pikachu"}
fav_snack = input("What your favorite after school snack? Fruit/Cookies/Potato Chips/Granola Bars").lower()
fav_movie = input("Pick a Disney movie: Inside Out/Moana/Zooptopia/Wreck-it Ralph").capitalize()
fav_sprpwr = input("Pick a superpower: Flying/Mind reading/Super speed/Super strength").lower()
fav_drink = input("What's your favorite drink: Milk/Smoothie/Water/Sode").lower()
wknd_act = input("Pick a weekend activity: A day in the pool/hiking through a forest/hanging out at the park/baking a cake").lower()

if wknd_act == "a day in the pool":
    print(f"{player_name}, your starter Pokemon is {starters[1]}");