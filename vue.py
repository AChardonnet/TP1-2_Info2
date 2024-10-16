from appJar import gui
import model

animals = ['Tic', 'Tac', 'Totoro', 'Patrick', 'Pocahontas']
etats = ['affamé', 'fatigué', 'repus', 'endormi']
app=gui()

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








app.go()