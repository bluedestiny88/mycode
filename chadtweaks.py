#!/usr/bin/python3

# The following code contains the endpoints using Flask

from flask import Flask, redirect, url_for
import requests

app = Flask(__name__)
pokemon = "https://pokeapi.co/api/v2/pokemon/"

# Would this also technically fulfill the requirement for mini-project 1 if I decide to
# make a new project for mini-project 2?
@app.route("/starterpoke", methods= ["POST"])
def choose():
    # input won't work in flask, unfortunately.
    # grabs value from postmaker.html
    color= request.form.get("nm")

    if color == "red":
        starter = "charmander"
    elif color == "green":
        starter == "bulbasaur"
    elif color == "blue":
        starter == "squirtle"
    elif color == "yellow":
        starter == "pikachu"
    else:
        starter= "muk"
    
    ## Return statement needed for else?
    getthatpokemon  = requests.get(pokemon + starter)
    pokemondata = getthatpokemon.json()
    attack = pokemondata["abilities"][0]["ability"]["name"]
    return f"Hello! Your starting Pokemon is {starter}! \n {starter.capitalize()} used {attack.capitalize()}! It's super effective!"

@app.route("/start/")
def start():
    # take postmaker.html from an earlier lab. Have it ask to choose one of the following colors: red, green, blue, or yellow.
    # change the POST address to /starterpoke
    return render_template("choice.html")

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 2224)
