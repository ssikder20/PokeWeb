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

def gen_update():
    from pokepy import V2Client

    client = V2Client()
    generations = {
        "Generation 1": [(i, name_hash.get(i, client.get_pokemon(i).name.title())) for i in range(1, 152)],
        "Generation 2": [(i, name_hash.get(i, client.get_pokemon(i).name.title())) for i in range(152, 252)],
        "Generation 3": [(i, name_hash.get(i, client.get_pokemon(i).name.title())) for i in range(252, 387)],
        "Generation 4": [(i, name_hash.get(i, client.get_pokemon(i).name.title())) for i in range(387, 494)],
        "Generation 5": [(i, name_hash.get(i, client.get_pokemon(i).name.title())) for i in range(494, 650)],
        "Generation 6": [(i, name_hash.get(i, client.get_pokemon(i).name.title())) for i in range(650, 722)],
        "Generation 7": [(i, name_hash.get(i, client.get_pokemon(i).name.title())) for i in range(722, 808)]
    }

    with open('app/static/generations.csv', 'w', encoding='utf-8') as File:
        for k in generations.keys():
            File.write(f"{format(k)}")
            for i in generations[k]:
                File.write(f";{format(i)}")
            File.write("\n")

def gen_read():
    import csv

    generations = {}
    with open('app/static/generations.csv', 'r', encoding='utf-8') as File:
        reader = csv.reader(File, delimiter=';')

        for row in reader:
            pokemon = [eval(i) for i in row[1:]]
            generation = {row[0]: pokemon}
            generations.update(generation)
    
    return generations

def get_gen(dict):
    return [i for i in dict.keys()]