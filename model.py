import json

def lit_etat(animal_id):
    with open('animal.json', "r", encoding='utf-8') as f:
        animals = json.load(f)
    if animal_id in animals :
        return animals[animal_id]['ETAT']
    else:
        print(f"Désolé, {animal_id} n'est pas un animal connu")
        return None

def lit_lieu(animal_id):
    with open('animal.json','r', encoding='utf-8') as f:
        animals = json.load(f)
    if animal_id in animals:
        return animals[animal_id]['LIEU']
    else:
        print(f"Désolé, {animal_id} n'est pas un animal connu")
        return None
    
def verifie_disponibilite(equipement_id):
    with open('equipment.json','r', encoding='utf-8') as f:
        equipement = json.load(f)
    if equipement_id in equipement:
        return equipement[equipement_id]['DISPONIBILITÉ']
    else:
        print(f"Désolé, {equipement_id} n'est pas un équipement connu")
        return None

def cherche_occupant(lieu):
    with open('equipment.json','r', encoding='utf-8') as f:
        equipement = json.load(f)
    if not(lieu in equipement) :
        print(f"Désolé, {lieu} n'est pas un équipement connu")
        return None
    with open('animal.json','r', encoding='utf-8') as f:
        animals = json.load(f)
    occupants = []
    for animal in animals.keys():
        if animals[animal]['LIEU'] == lieu :
            occupants.append(animal)
    return occupants

def change_etat(animal_id, etat):
    etats_autorisés = ['affamé', 'fatigué', 'repus', 'endormi']
    with open('animal.json','r', encoding='utf-8') as f:
        animals = json.load(f)
    if etat in etats_autorisés:
        if animal_id in animals:
            animals[animal_id]['ETAT'] = etat
    json.dump(animals, open("animal.json", "w"), indent=4)

def change_lieu(animal_id, lieu):
    with open('equipment.json','r', encoding='utf-8') as f:
        equipement = json.load(f)
    if lieu in equipement:
        if equipement[lieu]['DISPONIBILITÉ'] == 'occupé':
            print(f"Désolé, le lieu {lieu} est déjà occupé")
        else:
            with open('animal.json','r', encoding='utf-8') as f:
                animals = json.load(f)
            if animal_id in animals:
                if animals[animal_id]['LIEU'] != 'litière': #on libère l'ancien lieu
                    equipement[animals[animal_id]['LIEU']]['DISPONIBILITÉ'] = 'libre'
                if lieu != 'litière': #on occupe le nouveau lieu
                    equipement[lieu]['DISPONIBILITÉ'] = 'occupé'
                animals[animal_id]['LIEU'] = lieu
                json.dump(animals, open("animal.json", "w"), indent=4)
                json.dump(equipement, open("equipment.json", "w"), indent=4)
