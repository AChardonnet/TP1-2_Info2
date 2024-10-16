import model

def nourrir(animal_id):
    if model.verifie_disponibilite('mangeoire') == 'occupé':
        print(f"Impossible, la mangeoire est actuellement occupée par {model.cherche_occupant('mangeoire')[0]}")
    elif model.lit_etat(animal_id) != 'affamé':
        print(f"Désolé, {animal_id} n'a pas faim!")
    else: 
        model.change_lieu(animal_id, 'mangeoire')
        model.change_etat(animal_id, 'repus')

def divertir(animal_id):
    if model.verifie_disponibilite('roue') == 'occupé':
        print(f"Impossible, la roue est actuellement occupée par {model.cherche_occupant('roue')[0]}")
    elif model.lit_etat(animal_id) != 'repus':
        print(f"Désolé, {animal_id} n'est pas en état de faire du sport!")
    else:
        model.change_lieu(animal_id, 'roue')
        model.change_etat(animal_id, 'fatigué')

def coucher(animal_id):
    if model.verifie_disponibilite('nid') == 'occupé':
        print(f"Impossible, le nid est actuellement occupé par {model.cherche_occupant('nid')[0]}")
    elif model.lit_etat(animal_id) != 'fatigué':
        print(f"Désolé, {animal_id} n'est pas fatigué!")
    else:
        model.change_lieu(animal_id, 'nid')
        model.change_etat(animal_id, 'endormi')

def reveiller(animal_id):
    if model.lit_etat(animal_id) != 'endormi':
        print(f"Désolé, {animal_id} ne dort pas!")
    else:
        model.change_lieu(animal_id, 'litière')
        model.change_etat(animal_id, 'affamé')