from appJar import gui

app=gui()

app.addLabel("en-tête", "Bienvenue à l'animalerie!")
app.setLabelBg("en-tête", "salmon")
app.setLabelFg("en-tête", "white")

app.addLabel("tableau de bord", "Tableau de bord")
app.setLabelBg("tableau de bord", "gray")
app.go()