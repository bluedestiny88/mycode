#!/usr/bin/python3

# The following code contains the endpoints using Flask

from flask import Flask, redirect, url_for
import requests

app = Flask(__name__)
pokemon = "https://pokeapi.co/api/v2/pokemon/"

# Would this also technically fulfill the requirement for mini-project 1 if I decide to
# make a new project for mini-project 2?
@app.route("/starterpoke/<character>")
def choose(character):
    print(f"Hello {character}! \n")
    # input won't work in flask, unfortunately.

    color = input("Pick a color: red, green, blue, yellow \n")
    starter = ""
    if color == "red":
        starter = "charmander"
    elif color == "green":
        starter == "bulbasaur"
    elif color == "blue":
        starter == "squirtle"
    elif color == "yellow":
        starter == "pikachu"
    ## Return statement needed for else?
    getthatpokemon  = requests.get(pokemon + starter)
    pokemondata = getthatpokemon.json()
    attack = pokemondata["abilities"][0]["ability"]["name"]
    return f"{starter.capitalize()} used {attack.capitalize()}! It's super effective!"

@app.route("/start/")
def start():
    player = input("Please enter your name: ")
    return redirect(url_for("choose", character = player))

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 2224)
