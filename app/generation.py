from pokepy import V2Client

client = V2Client()

def gen_update():
    generations = {
        "Generation 1": [(i, client.get_pokemon(i).name.title()) for i in range(1, 152)],
        "Generation 2": [(i, client.get_pokemon(i).name.title()) for i in range(152, 252)],
        "Generation 3": [(i, client.get_pokemon(i).name.title()) for i in range(252, 387)],
        "Generation 4": [(i, client.get_pokemon(i).name.title()) for i in range(387, 494)],
        "Generation 5": [(i, client.get_pokemon(i).name.title()) for i in range(494, 650)],
        "Generation 6": [(i, client.get_pokemon(i).name.title()) for i in range(650, 722)],
        "Generation 7": [(i, client.get_pokemon(i).name.title()) for i in range(722, 808)]
    }

    with open('app/static/generations.csv', 'w') as File:
        for k in generations.keys():
            File.write(f"{format(k)}")
            for i in generations[k]:
                File.write(f";{format(i)}")
            File.write("\n")

def gen_read():
    import csv

    generations = {}
    with open('app/static/generations.csv', 'r') as File:
        reader = csv.reader(File, delimiter=';')

        for row in reader:
            pokemon = [eval(i) for i in row[1:]]
            generation = {row[0]: pokemon}
            generations.update(generation)
    
    return generations

def get_gen(dict):
    '''
    arr = []
    i = 1
    for k in dict.keys():
        arr.append((k, k))
        i += 1
    
    return arr
    '''
    return [i for i in dict.keys()]
