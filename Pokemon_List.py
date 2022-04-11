# Algorithm that generates sequence of Pokemon names

pokemon_list = ['audino', 'bagon', 'baltoy', 'banette', 'bidoof', 'braviary', 'bronzor', 'carracosta', 'charmeleon',
                'cresselia', 'croagunk', 'darmanitan', 'deino', 'emboar', 'emolga', 'exeggcute', 'gabite', 'girafarig',
                'gulpin', 'haxorus', 'heatmor', 'heatran', 'ivysaur', 'jellicent', 'jumpluff', 'kangaskhan',
                'kricketune', 'landorus', 'ledyba', 'loudred', 'lumineon', 'lunatone', 'machamp', 'magnezone',
                'mamoswine', 'nosepass', 'petilil', 'pidgeotto', 'pikachu', 'pinsir', 'poliwrath', 'poochyena',
                'porygon2', 'porygonz', 'registeel', 'relicanth', 'remoraid', 'rufflet', 'sableye', 'scolipede',
                'scrafty', 'seaking', 'sealeo', 'silcoon', 'simisear', 'snivy', 'snorlax', 'spoink', 'starly',
                'tirtouga', 'trapinch', 'treecko', 'tyrogue', 'vigoroth', 'vulpix', 'wailord', 'wartortle', 'whismur',
                'wingull', 'yamask']
pokemon_order = []
pokemon_last = pokemon_list[-1]


def fill_list(pokemon):
    """
    Add the pokemon name to the list

    Args:
        pokemon: pokemon name.

    Returns:
        Pokemon name list
    """
    pokemon_order.append(pokemon)
    return [pokemon_order]


def search_pokemon(letter, list_1, list_2):
    """
    Search pokemon name in the lists

    Args:
        letter: letter with which to search for the name of the pokemon
        list_1: list containing pokemon names
        list_2: list containing the names of the ordered pokemons

    Returns:
        name of the pokemon that begins with the letter you are looking for
    """
    for pokemon in list_1:
        if letter == pokemon[0]:
            if pokemon in list_2:
                continue
            else:
                return pokemon


def last_letter(list_1):
    """
    Last letter of pokemon name

    Args:
        list_1: list of pokemon names ordered

    Returns:
        Final letter of the last pokemon on the list
    """
    pokemon = list_1[-1]
    return pokemon[-1]


fill_list(pokemon_last)

while pokemon_order[-1] is not None:
    fill_list(search_pokemon(last_letter(pokemon_order), pokemon_list, pokemon_order))

if pokemon_order[-1] is None:
    pokemon_order[-1] = pokemon_order[-2]

print(pokemon_order)
