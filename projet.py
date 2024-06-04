from datetime import datetime


class Membre:
    def __init__(self, nom, role):
        self.nom = nom
        self.role = role

    def __str__(self):
        return f"Membre(nom={self.nom}, role={self.role})"


class Tache:
    def __init__(self, nom, description, date_debut, date_fin, responsable, statut):
        self.nom = nom
        self.description = description
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.responsable = responsable
        self.statut = statut

    def __str__(self):
        return (
            f"Tache(nom={self.nom}, description={self.description}, "
            f"date_debut={self.date_debut}, date_fin={self.date_fin}, "
            f"responsable={self.responsable}, statut={self.statut})"
        )


class Risque:
    def __init__(self, nom, probabilite, impact):
        self.nom = nom
        self.probabilite = probabilite
        self.impact = impact

    def __str__(self):
        return f"Risque(nom={self.nom}, probabilite={self.probabilite}, impact={self.impact})"


class Equipe:
    def __init__(self):
        self.membres = []

    def ajouter_membre(self, membre):
        self.membres.append(membre)

    def obtenir_membres(self):
        return self.membres

    def __str__(self):
        return f"Equipe(membres={', '.join(str(membre) for membre in self.membres)})"


class Projet:
    def __init__(self, nom, description, date_debut, date_fin):
        self.nom = nom
        self.description = description
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.taches = []
        self.risques = []
        self.changements = []
        self.version = 1
        self.equipe = Equipe()

    def ajouter_tache(self, tache):
        self.taches.append(tache)

    def ajouter_membre_equipe(self, membre):
        self.equipe.ajouter_membre(membre)

    def ajouter_risque(self, risque):
        self.risques.append(risque)

    def enregistrer_changement(self, changement):
        self.changements.append(changement)
        self.version += 1

    def __str__(self):
        return (
            f"Projet(nom={self.nom}, description={self.description}, "
            f"date_debut={self.date_debut}, date_fin={self.date_fin}, "
            f"taches={self.taches}, risques={self.risques}, "
            f"changements={self.changements}, version={self.version}, "
            f"equipe={self.equipe})"
        )


def generer_rapport_performance(projet):
    rapport = f"Rapport de performance du projet {projet.nom}\n\n"

    rapport += "Tâches :\n"
    for tache in projet.taches:
        rapport += f"- {tache.nom}: {tache.statut}\n"

    rapport += "\nMembres de l'équipe :\n"
    for membre in projet.equipe.obtenir_membres():
        rapport += f"- {membre.nom} ({membre.role})\n"

    rapport += "\nRisques :\n"
    for risque in projet.risques:
        rapport += f"- {risque.nom}: Probabilité {risque.probabilite}, Impact {risque.impact}\n"

    rapport += "\nChangements enregistrés :\n"
    for changement in projet.changements:
        rapport += f"- {changement}\n"

    rapport += f"\nVersion du projet : {projet.version}\n"

    return rapport


def test_projet():
    membre1 = Membre("Modou", "Chef de projet")
    membre2 = Membre("Awa", "Développeur")
    tache1 = Tache(
        "Tache1",
        "Description1",
        datetime(2024, 6, 1),
        datetime(2024, 6, 10),
        membre1,
        "En cours",
    )
    tache2 = Tache(
        "Tache2",
        "Description2",
        datetime(2024, 6, 11),
        datetime(2024, 6, 20),
        membre2,
        "En attente",
    )
    projet = Projet(
        "Projet1", "Description du projet", datetime(2024, 6, 1), datetime(2024, 12, 31)
    )

    projet.ajouter_tache(tache1)
    projet.ajouter_membre_equipe(membre1)
    projet.ajouter_risque(Risque("Risque1", 0.5, "Haut"))

    projet.enregistrer_changement("Modification 1")

    print("Taches dans le projet:", [str(tache) for tache in projet.taches])
    print(
        "Membres de l'équipe:",
        [str(membre) for membre in projet.equipe.obtenir_membres()],
    )
    print("Risques dans le projet:", [str(risque) for risque in projet.risques])
    print("Changements enregistrés:", projet.changements)
    print("Version du projet:", projet.version)

    rapport_performance = generer_rapport_performance(projet)
    print("\nRapport de performance du projet :\n", rapport_performance)


if __name__ == "__main__":
    test_projet()
