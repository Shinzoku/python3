from vehicule import Vehicule

class Voiture(Vehicule):
    """
    Cette classe représente une voiture.
    C'est une classe concrête qui etend (ou hérite de) la classe Vehicule.
    Cette classe estdestinée à être instanciée.
    """


    # les vartiables déclarées directement dans la classe sont "des variables de classe"
    # le underscore permet d'indiquer que la variable est privée
    # attention car elle reste tout de même accessible depuis l'exterieur
    # redéfenir une variable de classe dans une classe s'appelle "surcharger une variable de classe"
    _acceleration = 20

    # redéfinir une méthode (fonction) d'une classe mère dans une classe enfant s'appelle "surcharger une méthode"
    def __init__(self, marque: str, modele: str, carburant: str, vitesse: int, type_carrosserie: str):
        super().__init__(marque, modele, carburant, vitesse)
        self._type_carrosserie = type_carrosserie

    # redéfinir une méthode (fonction) d'une classe mère dans une classe enfant s'appelle "surcharger une méthode"
    def __str__(self) -> str:
        return super().__str__() + f" {self._type_carrosserie}"

    def get_type_carrosserie(self) -> str:
        return self._type_carrosserie