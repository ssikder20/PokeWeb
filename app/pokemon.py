def get_type_effectiveness(arr):
    type_effectiveness = {
        'Normal': [1, 2, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'Fighting': [1, 1, 2, 1, 1, 0.5, 0.5, 1, 1, 1, 1, 1, 1, 2, 1, 1, 0.5, 2],
        'Flying': [1, 0.5, 1, 1, 0, 2, 0.5, 1, 1, 1, 1, 0.5, 2, 1, 2, 1, 1, 1],
        'Poison': [1, 0.5, 1, 0.5, 2, 1, 0.5, 1, 1, 1, 1, 0.5, 1, 2, 1, 1, 1, 0.5],
        'Ground': [1, 1, 1, 0.5, 1, 0.5, 1, 1, 1, 1, 2, 2, 0, 1, 2, 1, 1, 1],
        'Rock': [0.5, 2, 0.5, 0.5, 2, 1, 1, 1, 2, 0.5, 2, 2, 1, 1, 1, 1, 1, 1],
        'Bug': [1, 0.5, 2, 1, 0.5, 2, 1, 1, 1, 2, 1, 0.5, 1, 1, 1, 1, 1, 1],
        'Ghost': [0, 0, 1, 0.5, 1, 1, 0.5, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1],
        'Steel': [0.5, 2, 0.5, 0, 2, 0.5, 0.5, 1, 0.5, 2, 1, 0.5, 1, 0.5, 0.5, 0.5, 1, 0.5],
        'Fire': [1, 1, 1, 1, 2, 2, 0.5, 1, 0.5, 0.5, 2, 0.5, 1, 1, 0.5, 1, 1, 0.5],
        'Water': [1, 1, 1, 1, 1, 1, 1, 1, 0.5, 0.5, 0.5, 2, 2, 1, 0.5, 1, 1, 1],
        'Grass': [1, 1, 2, 2, 0.5, 1, 2, 1, 1, 2, 0.5, 0.5, 0.5, 1, 2, 1, 1, 1],
        'Electric': [1, 1, 0.5, 1, 2, 1, 1, 1, 0.5, 1, 1, 1, 0.5, 1, 1, 1, 1, 1],
        'Psychic': [1, 0.5, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 0.5, 1, 1, 2, 1],
        'Ice': [1, 2, 1, 1, 1, 2, 1, 1, 2, 2, 1, 1, 1, 1, 0.5, 1, 1, 1],
        'Dragon': [1, 1, 1, 1, 1, 1, 1, 1, 1, 0.5, 0.5, 0.5, 0.5, 1, 2, 2, 1, 2],
        'Dark': [1, 2, 1, 1, 1, 1, 2, 0.5, 1, 1, 1, 1, 1, 0, 1, 1, 0.5, 2],
        'Fairy': [1, 0.5, 1, 2, 1, 1, 0.5, 1, 2, 1, 1, 1, 1, 1, 1, 0, 0.5, 1]
    }

    type_num = {
        0: 'Normal',
        1: 'Fighting',
        2: 'Flying',
        3: 'Poison',
        4: 'Ground',
        5: 'Rock',
        6: 'Bug',
        7: 'Ghost',
        8: 'Steel',
        9: 'Fire',
        10: 'Water',
        11: 'Grass',
        12: 'Electric',
        13: 'Psychic',
        14: 'Ice',
        15: 'Dragon',
        16: 'Dark',
        17: 'Fairy'
    }

    effectiveness = []

    def find_type_effectiveness(n):
        arr = [type_num[i] for i in range(len(effectiveness)) if effectiveness[i] == n]
        return arr

    if len(arr) == 1:
        effectiveness = type_effectiveness[arr[0]]
    else:
        arr_of_types = [type_effectiveness[type] for type in arr]
        effectiveness = list(map(lambda type1, type2: type1 * type2, arr_of_types[0], arr_of_types[1]))
    
    type_effective = {
        "Neutral (1x)": find_type_effectiveness(1),
        "Weak (2x)": find_type_effectiveness(2),
        "Very Weak (4x)": find_type_effectiveness(4),
        "Resistant (0.5x)": find_type_effectiveness(0.5),
        "Very Resistant (0.25x)": find_type_effectiveness(0.25),
        "Immune (0x)": find_type_effectiveness(0)
    }

    return type_effective

def pokemon_image(nat_dex):
    name_hash = {
        772: 'Type: Null',
        112: 'Mr. Mime',
        439: 'Mime Jr.',
        29: 'Nidoran♀',
        32: 'Nidoran♂',
        784: 'Kommo-o',
        783: 'Hakamo-o',
        83: 'Farfetch\'d',
        386: 'Deoxys',
        413: 'Wormadam',
        487: 'Giratina',
        492: 'Shaymin',
        550: 'Basculin',
        555: 'Darmanitan',
        641: 'Tornadus',
        642: 'Thundurus',
        645: 'Landorus',
        647: 'Keldeo',
        648: 'Meloetta',
        669: 'Flabébé',
        670: 'Floette',
        671: 'Florges',
        678: 'Meowstic',
        681: 'Aegislash',
        710: 'Pumpkaboo',
        711: 'Gourgeist',
        741: 'Oricorio',
        745: 'Lycanroc',
        746: 'Wishiwashi',
        774: 'Minior',
        778: 'Mimikyu',
        782: 'Jangmo-o',
        785: 'Tapu Koko',
        786: 'Tapu Lele',
        787: 'Tapu Bulu',
        788: 'Tapu Fini',
    }

    from pokepy import V2Client
    import requests
    from bs4 import BeautifulSoup

    client = V2Client()
    name = name_hash.get(int(nat_dex), client.get_pokemon(nat_dex).name.title())

    wiki = requests.get(f"https://bulbapedia.bulbagarden.net/wiki/{name}_(Pok%C3%A9mon)")
    soup = BeautifulSoup(wiki.content, 'html.parser')

    image = soup.find('img', {'alt': name})
    
    print(nat_dex)
    print(name)
    return(f"https://{image.get('src')[2:]}")

def pokemon_data(nat_dex):
    from pokepy import V2Client

    name_hash = {
        772: 'Type: Null',
        112: 'Mr. Mime',
        439: 'Mime Jr.',
        29: 'Nidoran♀',
        32: 'Nidoran♂',
        784: 'Kommo-o',
        783: 'Hakamo-o',
        83: 'Farfetch\'d',
        386: 'Deoxys',
        413: 'Wormadam',
        487: 'Giratina',
        492: 'Shaymin',
        550: 'Basculin',
        555: 'Darmanitan',
        641: 'Tornadus',
        642: 'Thundurus',
        645: 'Landorus',
        647: 'Keldeo',
        648: 'Meloetta',
        669: 'Flabébé',
        670: 'Floette',
        671: 'Florges',
        678: 'Meowstic',
        681: 'Aegislash',
        710: 'Pumpkaboo',
        711: 'Gourgeist',
        741: 'Oricorio',
        745: 'Lycanroc',
        746: 'Wishiwashi',
        774: 'Minior',
        778: 'Mimikyu',
        782: 'Jangmo-o',
        785: 'Tapu Koko',
        786: 'Tapu Lele',
        787: 'Tapu Bulu',
        788: 'Tapu Fini',
    }
    client = V2Client()
    pokemon = client.get_pokemon(nat_dex)
    stats = [i.base_stat for i in pokemon.stats]
    
    pokeObj = {
        'id': nat_dex,
        'name': name_hash.get(nat_dex, client.get_pokemon(nat_dex).name.title()),
        'height': pokemon.height,
        'weight': pokemon.weight,
        'abilities': [(i.ability.name.title(), i.is_hidden) for i in pokemon.abilities], # parsing for descriptions would be very complex so just the name is fine for now
        'types': [i.type.name.title() for i in pokemon.types],
        'type effectiveness': {},
        'stats': {'HP': stats[0], 'Attack': stats[1], 'Defense': stats[2], 'Special Attack': stats[3], 'Special Defense': stats[4], 'Speed': stats[5]}
    }

    pokeObj['type effectiveness'] = get_type_effectiveness(pokeObj['types'])

    return pokeObj