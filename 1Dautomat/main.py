import tkinter as tk

class CellAutomaton1D:
    def __init__(self, rule):
        self.rule = rule
        self.width = 101  # fiksna velikost širine
        self.height = 101  # fiksna velikost višine
        self.grid = [[0] * self.width for _ in range(self.height)]
        self.grid[0][self.width//2] = 1 #postavi 1 celico v sredini, v sredini prve vrstice aktivno celico

    def apply_rule(self, a, b, c):
        return self.rule[7 - (a << 2 | b << 1 | c)] #se uporablja za določanje naslednjega stanja celice na podlagi njenega trenutnega stanja in stanj njenih sosednjih celic, levo, desno, center

    def generate(self): #Za vsako vrstico (razen prve) in vsako celico v njej se izračunajo stanja sosednjih celic (a, b, c) in nato se pravilo uporabi za določanje naslednjega stanja celice.
        for y in range(1, self.height): #razen prve vrstice
            for x in range(self.width):
                a = self.grid[y-1][(x-1)%self.width]
                b = self.grid[y-1][x]
                c = self.grid[y-1][(x+1)%self.width]
                self.grid[y][x] = self.apply_rule(a, b, c)

class GUI:
    def __init__(self, master):
        self.master = master
        self.rule = tk.StringVar()
        self.rule.set("30")  # privzeto pravilo
        self.canvas = tk.Canvas(self.master, width=1100, height=200, bg="white") #barvo ozadja na belo
        self.rule_entry = tk.Entry(self.master, textvariable=self.rule) #vnosno polje za vnos pravila ki bo se preneslo na self.rule
        self.start_button = tk.Button(self.master, text="Start", command=self.start) #klice se funkcija start
        #self.reset_button = tk.Button(self.master, text="Reset", command=self.reset)
        self.quit_button = tk.Button(self.master, text="Quit", command=self.quit) #klice se funkcija quit
        self.canvas.pack() #prikazuje platno v aplikacije
        tk.Label(self.master, text="Rule (decimal)").pack()
        self.rule_entry.pack() #vnosno polje
        self.start_button.pack(side=tk.LEFT)
        #self.reset_button.pack(side=tk.LEFT)
        self.quit_button.pack(side=tk.LEFT)

    def start(self):
        self.canvas.delete("all")
        rule = int(self.rule.get()) #prebere vrednost
        automaton = CellAutomaton1D([int(x) for x in bin(rule)[2:].zfill(8)]) #pretvori v binarno obliko stevila rule
        cell_size = 12 # velikost celice, piksle
        #dve gnezdeni zanki za izrisovanje pravokotnikov na platnu, ki predstavljajo celice 1D
        for y in range(automaton.height): #vsako vrstico
            #najprej izrise samo za tiste celice, ki imajo v matriki automation.grid vrednost 1, t.j. ustvari samo prvu vrsticu celic in je prikaze na platnu
            for x in range(automaton.width): #vsako celico v vsako vrstico
                if automaton.grid[y][x]: #ce je vrednost celice 1, ustvari pravokotnik na platnu, ki predstavlja to celico
                    self.canvas.create_rectangle(x*cell_size, y*cell_size, (x+1)*cell_size, (y+1)*cell_size, fill="black")
                    #Ta ukaz ustvari pravokotnik na platnu s širino in višino cell_size, ki predstavlja trenutno celico
        for _ in range(100): #generira se metoda ki izrise na platnu nasljedno stanje 1D automata
            automaton.generate()
            for y in range(automaton.height):
                for x in range(automaton.width):
                    if automaton.grid[y][x]:
                        self.canvas.create_rectangle(x * cell_size, y * cell_size, (x + 1) * cell_size,(y + 1) * cell_size, fill="black")
            #Za vsako celico v trenutni mreži 1D avtomata ustvari pravokotnik na platnu, ki predstavlja to celico, če ima vrednost 1. Vse ustvarjene pravokotnike doda na platno.
            #self.canvas.update()

    #def reset(self):
     #   self.canvas.delete("all")
      #  self.start()

    def quit(self):
        self.master.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    root.title("1D Cellular Automaton")
    gui = GUI(root)
    root.mainloop()
