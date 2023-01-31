from tkinter import *  
from tkinter import messagebox

# hoved class Materiale 
class Materiale():
    def __init__(self, idnr, titel, antal, antaludlaan, aarstal):
        self.idnr = int(idnr)
        self.titel = titel
        self.antal = int(antal)
        self.antaludlaan = int(antaludlaan)
        self.aarstal = aarstal
        self.forfatter = ""
        self.kunstner = ""
        self.instruktor = ""

    # toString metode der returnerer formateret oplysninger om materialet
    def toString(self):
        return (f"ID nummer: {self.idnr}  bog   title: {self.titel}  "
            f"antal: {self.antal}  antaludlaan: {self.antaludlaan}  "
            f"aarstal: {self.aarstal} ")    
    
    # metode der returner idnumret for materialet. Bruges til udlån og aflever 
    def return_id(self):
        return self.idnr

    # metode der låner materiale ud
    def udlaan_materiale(self):
        # tjekker om der er ledige kopier af materialet
        if self.antal - self.antaludlaan > 0:
            # hvis der er ledig kopi, bliver antallet af udlån materialer + 1 stk.
            self.antaludlaan = int(self.antaludlaan) + 1 
            # og der vises kvittering på udlån
            messagebox.showinfo("Udlån af materiale", 
                f"Du har nu lånet {self.titel}")
        else:
            # ellers vises info besked
            return messagebox.showinfo("info", 
                "Der er ikke flere ledige kopier af materialet")
    
    # metode der afleverer materiale
    def aflever_materiale(self):
        # tjekker om materialet er lånet ud
        if self.antaludlaan != 0:
            # hvis ja, så får man lov til at aflevere. Antaludlån bliver - 1 stk.
            self.antaludlaan = int(self.antaludlaan) - 1
            # og der vises kvittering
            messagebox.showinfo("Udlån af materiale", 
                f"Du har nu afleverer {self.titel}")
        else:
            # info besked der fortæller at materialet er ikke lånet ud og kan 
            # derfor ikke afleveres
            return messagebox.showinfo("info", 
                "Materialet er ikke lånet ud og kan derfor ikke afleveres")     

    # metode der returnerer objektets parametre, som vi vil kunne søge i 
    def search_in_object(self):
        return (f"{self.idnr}, {self.titel}, {self.aarstal},"
        f"{self.forfatter}, {self.kunstner}, {self.instruktor}")

# child class der arver fra Materiale klassen
class Bog(Materiale):

    def __init__(self, idnr, titel, antal, antaludlaan, aarstal, antalsider, 
        forfatter):
        super().__init__(idnr, titel, antal, antaludlaan, aarstal)
        self.antalsider = antalsider
        self.forfatter = forfatter

    # metode der erstatter metoden fra Materiale. Tilpasset formattering  
    def toString(self):
        return (f"ID nummer: {self.idnr}  bog       titel: {self.titel:<25}  "
            f"forfatter:   {self.forfatter:<25} antal: {self.antal:<3} "
            f"antaludlaan: {self.antaludlaan:<3} aarstal: {self.aarstal} "
            f"antalsider:  {self.antalsider}")



# child class der arver fra Materiale klassen
class Film(Materiale):
    def __init__(self, idnr, titel, antal, antaludlaan, aarstal, instruktor,
        laengde):
        super().__init__(idnr, titel, antal, antaludlaan, aarstal)
        self.instruktor = instruktor
        self.laengde = laengde

    # metode der erstatter metoden fra Materiale. Tilpasset formattering
    def toString(self):
        return (f"ID nummer: {self.idnr}  film      titel: {self.titel:<25} "
            f" instruktor:  {self.instruktor:<25} antal: {self.antal:<3} "
            f"antaludlaan: {self.antaludlaan:<3} aarstal: {self.aarstal} "
            f"laengde:     {self.laengde}")

# child class der arver fra Materiale klassen
class MusikDVD(Materiale):
    def __init__(self, idnr, titel, antal, antaludlaan, aarstal, kunstner):
        super().__init__(idnr, titel, antal, antaludlaan, aarstal)
        self.kunstner = kunstner
        
    # metode der erstatter metoden fra Materiale. Tilpasset formattering
    def toString(self):
        return (f"ID nummer: {self.idnr}  MusikDVD  titel: {self.titel:<25}  "
            f"kunstner:    {self.kunstner:<25} antal: {self.antal:<3} "
            f"antaludlaan: {self.antaludlaan:<3} aarstal: {self.aarstal}")