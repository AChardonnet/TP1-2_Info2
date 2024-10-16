from appJar import gui
import model
import controleur

def initGui():
    model.reset()
    app.addLabel("en-tête", "Bienvenue à l'animalerie!")
    app.setLabelBg("en-tête", "salmon")
    app.setLabelFg("en-tête", "white")

    app.addLabel("tableau de bord", "Tableau de bord")
    app.setLabelBg("tableau de bord", "gray")

    for animal in animals:
        app.addLabel(animal, f"{animal} : {model.lit_etat(animal)}, {model.lit_lieu(animal)}")

    app.addLabel("actions", "Actions")
    app.setLabelBg("actions", "gray")

    app.addLabel("animal", "Animal")
    app.setLabelBg("animal", "lightgray")

    for animal in animals:
        app.addRadioButton("id_animal", animal)

    app.addLabel("action", "Action")
    app.setLabelBg("action", "lightgray")

    for etat in etats:
        app.addRadioButton("etat", etat)

    app.addButton("go",  press)

    app.go()

def updateGui():
    for animal in animals:
        app.setLabel(animal, f"{animal} : {model.lit_etat(animal)}, {model.lit_lieu(animal)}")

def press(act):
    action = app.getRadioButton("etat")
    animal = app.getRadioButton("id_animal")
    result = None
    match action:
        case 'nourrir':
            result = controleur.nourrir(animal)
        case 'divertir':
            result = controleur.divertir(animal)
        case 'coucher':
            result = controleur.coucher(animal)
        case 'reveiller':
            result = controleur.reveiller(animal)
    updateGui()
    if result != True:
        app.warningBox("Erreur !", result)

animals = ['Tic', 'Tac', 'Totoro', 'Patrick', 'Pocahontas']
etats = ['nourrir', 'divertir', 'coucher', 'reveiller']
app=gui()

initGui()