from tkinter import *
from tkinter import messagebox
from klasser import Film, Bog, MusikDVD

# liste hvor alle materialler bliver samlet
listMaterialer = []

# opretter 3 boger
bog1 = Bog(idnr = 4545, titel = "Great Expectations", antal= 12, \
    antaludlaan = 11, aarstal = 1861, antalsider = 544, \
    forfatter = "Charles Dickens")
bog2 = Bog(idnr = 3465, titel = "Moby Dick", antal= 7, antaludlaan = 6, 
    aarstal = 1851, antalsider =585, forfatter ="Herman Melville")
bog3 = Bog(idnr = 6535, titel = "War and Peace", antal= 1, antaludlaan = 1, 
    aarstal = 1225, antalsider = 1456, forfatter = "Lev Tolstoy")

# og tilføjer dem på listen
listMaterialer.append(bog1)
listMaterialer.append(bog2)
listMaterialer.append(bog3)


# opretter 3 film
film1 = Film(idnr = 1925, titel = "Godfather", antal= 3, antaludlaan = 0, 
    aarstal = 1972, laengde = 175, instruktor = "Francis Ford Coppola")
film2 = Film(idnr = 6853, titel = "The Shawshank Redemption", antal= 5, 
    antaludlaan = 5, aarstal = 1995, laengde = 142, \
    instruktor = "Frank Darabont")
film3 = Film(idnr = 8929, titel = "Schindlers liste", antal= 2, antaludlaan = 0, 
    aarstal = 1993, laengde = 195, instruktor = "Steven Spielberg")

# og tilføjer dem på listen
listMaterialer.append(film1)
listMaterialer.append(film2)
listMaterialer.append(film3)

# opretter 3 musik DVD'er
musik1 = MusikDVD(idnr = 8194, titel = "The bends", antal = 3, antaludlaan = 3, \
    aarstal = 1995, kunstner = "Radiohead")
musik2 = MusikDVD(idnr = 3195, titel = "Showbiz", antal = 1, antaludlaan = 0, \
    aarstal = 1999, kunstner = "Muse")
musik3 = MusikDVD(idnr = 1162, titel = "Nevermind", antal = 5, antaludlaan = 2, \
    aarstal = 1991, kunstner = "Nirvana")

# og tilføjer dem på listen
listMaterialer.append(musik1)
listMaterialer.append(musik2)
listMaterialer.append(musik3)


# grafisk interfacet begynder her
class Application(Frame):

    # udlån metode
    def udlaan(self):
        # får input fra brugeren
        idnr = self.id_entry.get()
        print("id der skal lånes: " + idnr)
        # opretter flag, status skifter hvis materialet bliver fundet
        not_in_list = True
        for x in listMaterialer:
            # returnerer idnummer for materialet
            y = x.return_id()
            # tjekker hvis bruger input er lige med idnummer 
            if int(idnr) == y:
                #hvis ja - skifter flag
                not_in_list = False
                # og kører udlån metoden defineret i klassen
                x.udlaan_materiale()
        if not_in_list:
            # hvis flag er stadig True, er der ikke fundet noget materiale
            # så man får info besked om det
            print(messagebox.showinfo("info", 
            "Der findes ingen materiale med dette ID nummer!"))
    # aflever metode          
    def aflever(self):
        # får input fra brugeren
        idnr = self.aflever_entry.get()
        print("id der skal afleveres: " + idnr)
        # opretter flag, status skifter hvis materialet bliver fundet
        not_in_list = True
        for x in listMaterialer:
            # returnerer idnummer for materialet
            y = x.return_id()
            # tjekker hvis bruger input er lige med idnummer 
            if int(idnr) == y:
                #hvis ja - skifter flag
                not_in_list = False
                # og kører aflever metoden defineret i klassen
                x.aflever_materiale()
        if not_in_list:
            # hvis flag er stadig True, er der ikke fundet noget materiale
            # så man får info besked om det
            print(messagebox.showinfo("info", 
            "Der findes ingen materiale med dette ID nummer!"))

    # søg metode
    def sog_i_listen(self):
        # får input fra brugeren
        search_text = self.entry.get()
        print("søge tekst: "+search_text)
        # sletter listen der er vist på skærmen
        self.listGui.delete('1.0', END)
        
        # opretter flag, status skifter hvis materialet bliver fundet
        not_in_list = True
        for materiale in listMaterialer:
            # kalder på search_in_object der returnerer objektets parametre, 
            # som vi vil kunne søge i
            y = materiale.search_in_object()
            # tjekker hvis bruger input findes i materialet
            if str(search_text.lower()) in str(y.lower()):
                # hvis ja - lister materialet
                self.listGui.insert(INSERT, materiale.toString()+"\n")
                # og skifter flaget
                not_in_list = False

        # hvis flag er stadig True, er der ikke fundet noget materiale
        # så man får info besked om det
        if not_in_list:
            print(messagebox.showinfo("info", 
            f"Der findes ingen materiale der indeholder {search_text}!"))

    # funktionen nedunder kan også søge.  
    # def sog_i_listen(self):
    #     search_text = self.entry.get()
    #     print("søge tekst: "+search_text)
    #     self.listGui.delete('1.0', END)
    #     not_in_list = True
    #     for materiale in listMaterialer:
    #         if search_text.lower() in materiale.titel.lower() or \
    #         search_text.lower() in str(materiale.aarstal):
    #             self.listGui.insert(INSERT, materiale.toString()+"\n")
    #             not_in_list = False
    #         elif 'forfatter' in materiale.__dict__:
    #             if search_text.lower() in materiale.forfatter.lower():
    #                 self.listGui.insert(INSERT, materiale.toString()+"\n")
    #                 not_in_list = False
    #         elif 'instruktor' in materiale.__dict__:
    #             if search_text.lower() in materiale.instruktor.lower():
    #                 self.listGui.insert(INSERT, materiale.toString()+"\n")
    #                 not_in_list = False
    #         elif 'kunstner' in materiale.__dict__:
    #             if search_text.lower() in materiale.kunstner.lower():
    #                 self.listGui.insert(INSERT, materiale.toString()+"\n")
    #                 not_in_list = False
    #     if not_in_list:
    #         print(messagebox.showinfo("info", 
    #         f"Der findes ingen materiale der indeholder {search_text}!"))


    # vis hele listen metode        
    def vis_hele_listen(self):
        print("Vis hele listen")
        # begynder med at slette listen
        self.listGui.delete('1.0', END)
        for materiale in listMaterialer:
            # og så tilføjer alle materialer på listen
            self.listGui.insert(INSERT, materiale.toString()+"\n")
        

    def create_widgets(self):
        frame = Frame(self)
        self.winfo_toplevel().title("Biblioteks databasen")

        # definition af quit-knap
        self.QUIT = Button(frame, text="QUIT")
        self.QUIT["fg"] = "red"
        self.QUIT["command"] = self.quit
        self.QUIT.pack({"side": "left"})

        # definition og mapping af vis hele listen knappen
        self.visListe = Button(frame,text="Vis hele listen")
        self.visListe["command"] = self.vis_hele_listen
        self.visListe.pack({"side": "left"})

        # definition af input-søgefeltet.
        self.L1 = Label(frame, text="Søgestreng")
        self.L1.pack(side=LEFT)
        self.entry = Entry(frame, bd=5)
        self.entry.pack(side=LEFT)

        # definition og mapping af søgeknappen.
        self.sogKnap = Button(frame, text="Søg i listen")
        self.sogKnap["command"] = self.sog_i_listen
        self.sogKnap.pack({"side": "left"})

        # definition af ID inputfeltet til udlån
        self.L1 = Label(frame, text="ID for udlån")
        self.L1.pack(side=LEFT)
        self.id_entry = Entry(frame, bd=5)
        self.id_entry.pack(side=LEFT)

        # definition af udlånsknappen og mapping til
        # en funktion.
        self.udlaanKnap = Button(frame, text="Udlån")
        self.udlaanKnap["command"] = self.udlaan
        self.udlaanKnap.pack({"side": "left"})

        # inputfelt til aflevering.
        self.L1 = Label(frame, text="ID for aflevering:")
        self.L1.pack(side=LEFT)
        self.aflever_entry = Entry(frame, bd=5)
        self.aflever_entry.pack(side=LEFT)

        # definition og mapping af afleveringsknap
        self.afleverKnap = Button(frame, text="Aflever")
        self.afleverKnap["command"] = self.aflever
        self.afleverKnap.pack({"side": "left"})

        
        

        # Her definerer vi en Text-widget - dvs
        # den kan indeholde multiple linjer.
        # Idéen er så at hver linje indeholder et styk materiale.
        # Nedenunder kan du se, hvordan listen af materiale løbes
        # igennem og toString-metoden bliver kaldt, så der bliver
        # indsat en ny linje i Text-widgeten
        self.listGui = Text(self, width=160)
        for materiale in listMaterialer:
            self.listGui.insert(INSERT, materiale.toString()+"\n")
        frame.pack()
        self.listGui.pack()

    # Denne constructor køres når programmet starter
    # og sørger for at alle vores widgets bliver lavet.
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.create_widgets()


root = Tk()
app = Application(master=root)
app.mainloop()
