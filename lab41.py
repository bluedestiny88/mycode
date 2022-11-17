chosen_char = input("Which character do you want to know about? (Starlord, Mystique, Hulk)")
chosen_stat = input("What statistic do you want to know about? (real name, powers, archenemy")

marvelchars= {
"Starlord":
  {"real name": "peter quill",
  "powers": "dance moves",
  "archenemy": "Thanos"},

"Mystique":
  {"real name": "raven darkholme",
  "powers": "shape shifter",
  "archenemy": "Professor X"},

"Hulk":
  {"real name": "bruce banner",
  "powers": "super strength",
  "archenemy": "adrenaline"}
             }


char_name = marvelchars.get(chosen_char)
char_stat = marvelchars[char_name].get(chosen_stat)

print(f"{char_name}'s {char_stat} is {value}")
