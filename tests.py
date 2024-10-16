import model 
import controleur
import json

def test_reset():
    with open('orig/equipment.json','r', encoding='utf-8') as f:
        equipement = json.load(f)
    with open('orig/animal.json','r', encoding='utf-8') as f:
        animals = json.load(f)
    json.dump(animals, open("animal.json", "w"), indent=4)
    json.dump(equipement, open("equipment.json", "w"), indent=4)

def test_lit_etat():
    assert model.lit_etat('Tac') == 'affamé'
 
def test_lit_etat_nul():
    assert model.lit_etat('Bob') == None

def test_lit_lieu():
    assert model.lit_lieu('Tac') == 'litière'
 
def test_lit_lieu_nul():
    assert model.lit_lieu('Bob') == None

def test_verifie_disponibilite():
    assert model.verifie_disponibilite('litière') == 'libre'
    assert model.verifie_disponibilite('nid') == 'occupé'
    
def test_verifie_disponibilite_nul():
    assert model.verifie_disponibilite('nintendo') == None

def test_cherche_occupant():
    assert model.cherche_occupant('nid') == ['Pocahontas']
    assert 'Tac' in model.cherche_occupant('litière')
    assert 'Tac' not in model.cherche_occupant('mangeoire')

def test_cherche_occupant_nul():
    assert model.cherche_occupant('casino') == None

def test_change_etat():
    model.change_etat('Totoro', 'fatigué')
    assert model.lit_etat('Totoro') == 'fatigué'
    model.change_etat('Totoro', 'excité comme un pou')
    assert model.lit_etat('Totoro') == 'fatigué'
    model.change_etat('Bob', 'fatigué')
    assert model.lit_etat('Bob') == None

def test_change_lieu():
    model.change_lieu('Totoro', 'roue')
    assert model.lit_lieu('Totoro') == 'roue'
    assert model.verifie_disponibilite('litière') == 'libre'    
    assert model.verifie_disponibilite('roue') == 'occupé'

def test_change_lieu_occupé():
    model.change_lieu('Totoro', 'nid')
    assert model.lit_lieu('Totoro') == 'roue'

def test_change_lieu_nul_1():
    model.change_lieu('Totoro', 'casino')
    assert model.lit_lieu('Totoro') == 'roue'

def test_change_lieu_nul_2():
    model.change_lieu('Bob', 'litière')
    assert model.lit_lieu('Bob') == None


## Tests controleur
def test_nourrir():
    if model.verifie_disponibilite('mangeoire') == 'libre' and model.lit_etat('Tic') == 'affamé':
        controleur.nourrir('Tic')
    assert model.verifie_disponibilite('mangeoire') == 'occupé'
    assert model.lit_etat('Tic') == 'repus'
    assert model.lit_lieu('Tic') == 'mangeoire'
    controleur.nourrir('Tac')
    assert model.lit_etat('Tac') == 'affamé'
    assert model.lit_lieu('Tac') == 'litière'
    controleur.nourrir('Pocahontas')
    assert model.lit_etat('Pocahontas') == 'endormi'
    assert model.lit_lieu('Pocahontas') == 'nid'
    controleur.nourrir('Bob')
    assert model.lit_etat('Bob') == None
    assert model.lit_lieu('Bob') == None
    assert model.verifie_disponibilite('mangeoire') == 'occupé'

def test_divertir():
    test_reset()
    controleur.divertir('Totoro')
    assert model.lit_etat('Totoro') == 'fatigué'
    assert model.lit_lieu('Totoro') == 'roue'
    assert model.verifie_disponibilite('roue') == 'occupé'
    controleur.nourrir('Patrick')
    controleur.divertir('Patrick')
    assert model.lit_etat('Patrick') == 'repus'
    assert model.lit_lieu('Patrick') == 'mangeoire'
    controleur.divertir('Bob')
    assert model.lit_etat('Bob') == None
    assert model.lit_lieu('Bob') == None

def test_coucher():
    test_reset()
    controleur.reveiller('Pocahontas')
    controleur.divertir('Totoro')
    controleur.coucher('Totoro')
    assert model.lit_etat('Totoro') == 'endormi'
    assert model.lit_lieu('Totoro') == 'nid'
    assert model.verifie_disponibilite('nid') == 'occupé'
    controleur.nourrir('Patrick')
    controleur.divertir('Patrick')
    controleur.coucher('Patrick')
    assert model.lit_etat('Patrick') == 'fatigué'
    assert model.lit_lieu('Patrick') == 'roue'
    controleur.coucher('Tac')
    assert model.lit_etat('Tac') == 'affamé'
    assert model.lit_lieu('Tac') == 'litière'
    controleur.coucher('Bob')
    assert model.lit_etat('Bob') == None
    assert model.lit_lieu('Bob') == None

def test_reveiller():
    test_reset()
    controleur.reveiller('Totoro')
    assert model.lit_etat('Totoro') == 'repus'
    assert model.lit_lieu('Totoro') == 'mangeoire'
    controleur.reveiller('Pocahontas')
    assert model.lit_etat('Pocahontas') == 'affamé'
    assert model.lit_lieu('Pocahontas') == 'litière'
