#!/usr/bin/python3

# The following code contains the endpoints using Flask

from flask import Flask, redirect, url_for, render_template
import requests

app = Flask(__name__)
pokemon = "https://pokeapi.co/api/v2/pokemon/"

@app.route("/")
def start():
    # go to lab 100 and borrow the postmaker.html, render that here. Ask for the player to choose red, green, blue, or yellow
    return render_template()

# this can count as mini project 1 as well, sure!
@app.route("/starterpoke", methods= ["POST"])
def choose():
    color = request.form.get("nm")
    if color == "red":
        starter= "charmander"
    elif color == "green":
        starter= "bulbasaur"
    elif color == "blue":
        starter= "squirtle"
    elif color == "yellow":
        starter= "pikachu"
    else:
        starter= "muk"
    
    getthatpokemon  = requests.get(pokemon + starter.lower())
    pokemondata = getthatpokemon.json()
    attack = pokemondata["abilities"][0]["ability"]["name"]

    # you could return this string as jinja2 html quite easily! that'd finish off the project real quick!
    return f"Your starter {starter.capitalize()} used {attack.capitalize()}! It's super effective!"


if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 2224)
