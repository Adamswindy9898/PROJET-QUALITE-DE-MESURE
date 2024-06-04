import unittest
from datetime import datetime
from projet import (
    Membre,
    Tache,
    Risque,
    Projet
)

class TestProjet(unittest.TestCase):
    def setUp(self):
        self.membre1 = Membre("Alice", "Manager")
        self.membre2 = Membre("Bob", "Développeur")
        self.tache1 = Tache("Tache1", "Description1", datetime(2024, 6, 1), datetime(2024, 6, 10), self.membre1, "En cours")
        self.tache2 = Tache("Tache2", "Description2", datetime(2024, 6, 11), datetime(2024, 6, 20), self.membre2, "En attente")
        self.projet = Projet("Projet1", "Description du projet", datetime(2024, 6, 1), datetime(2024, 12, 31))

    def test_ajout_tache(self):
        self.projet.ajouter_tache(self.tache1)
        self.assertIn(self.tache1, self.projet.taches)

    def test_ajout_membre(self):
        self.projet.ajouter_membre_equipe(self.membre1)
        self.assertIn(self.membre1, self.projet.equipe.obtenir_membres())

    def test_ajout_risque(self):
        risque = Risque("Risque1", 0.5, "Haut")
        self.projet.ajouter_risque(risque)
        self.assertIn(risque, self.projet.risques)

    def test_enregistrer_changement(self):
        self.projet.enregistrer_changement("Modification 1")
        self.assertEqual(self.projet.version, 2)
        self.assertEqual(len(self.projet.changements), 1)

if __name__ == '__main__':
    unittest.main()
