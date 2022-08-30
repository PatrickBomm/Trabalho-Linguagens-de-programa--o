from tkinter import *

i = 0
alfabeto = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
palavra = ""
validar = "0123456789+-*/()<>=:abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
auxiliarPrint = ""


def isNumber(x):
    if x in numbers:
        return True
    else:
        return False


def getNonAlphanumeric(x):
    global auxiliarPrint

    if x == "+":
        print("(" + x + ", ADDOP, 5)")
        auxiliarPrint += "(" + x + ", ADDOP, 5)"
        return 1
    if x == "-":
        print("(" + x + ", SUBOP, 6)")
        auxiliarPrint += "(" + x + ", SUBOP, 6)"
        return 1
    if x == "*":
        print("(" + x + ", MULOP, 7)")
        auxiliarPrint += "(" + x + ", MULOP, 7)"
        return 1
    if x == "/":
        print("(" + x + ", DIVOP, 8)")
        auxiliarPrint += "(" + x + ", DIVOP, 8)"
        return 1
    if x == "(":
        print("(" + x + ", LPAREN, 3)")
        auxiliarPrint += "(" + x + ", LPAREN, 3)"
        return 1
    if x == ")":
        print("(" + x + ", RPAREN, 4)")
        auxiliarPrint += "(" + x + ", RPAREN, 4)"
        return 1
    if x == "<":
        print("(" + x + ", STOP, 9)")
        auxiliarPrint += "(" + x + ", STOP, 9)"
        return 1
    if x == ">":
        print("(" + x + ", LTOP, 10)")
        auxiliarPrint += "(" + x + ", LTOP, 10)"
        return 1
    else:
        return 0 

def analiser():
    global i
    global palavra
    global numbers
    global validar
    global auxiliarPrint
    
    while i < len(palavra):
        
        if palavra[i] not in validar:
            i += 1
            break
        if i >= len(palavra):
            break
        
        if palavra[i] == " " or palavra[i] == "\n":
            i += 1
            analiser()
            break
        
        auxiliarPrint += "\n"
        
        
        
        # Verifica se tem letras solo ou consecutivas
        palavraAux = ""
        if palavra[i] in alfabeto:
            
                while (palavra[i] in alfabeto and i < len(palavra) or palavra[i] in numbers and i < len(palavra)): 
                    palavraAux += palavra[i]
                    i +=1
                    if i+1 > len(palavra):
                        break
            
                if len(palavraAux) >= 1:
            
                    print("(" + palavraAux + ", VAR, 1)")
                    auxiliarPrint += "(" + palavraAux + ", VAR, 1)"
                    analiser()
                    break

        # verifica se é "==" ou ":="
        if i+1 < len(palavra):
            equals = palavra[i] + palavra[i+1]
            if equals == "==":
                print("(" + palavra[i] + palavra[i+1] + ", EQOP, 11)")
                auxiliarPrint += "(" + palavra[i] + palavra[i+1] + ", EQOP, 11)"
                i += 2
                analiser()
                break
            if equals == ":=":
                print("(" + palavra[i] + palavra[i+1] + ", ASSIGNOP, 12)")
                auxiliarPrint += "(" + palavra[i] + palavra[i+1] + ", ASSIGNOP, 12)"
                i += 2
                analiser()
                break
        
        # verifica se é um non-alphanumeric
        if getNonAlphanumeric(palavra[i]) == 1:
            i += 1
            analiser()
            break
        
        # verifica se é um numero ou mais
        numerosAux = ""
        if(palavra[i] in numbers):
            while(palavra[i] in numbers):
                numerosAux += palavra[i]
                i += 1
                if i+1 > len(palavra):
                    break
        
            if len(numerosAux) >= 1:
                print("(" + numerosAux + ", NUM, 2)")
                auxiliarPrint += "(" + numerosAux + ", NUM, 2)"
                analiser()
                break
    
   
               


class Application:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 100
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()

        self.titulo = Label(self.primeiroContainer, text="Analisador Léxico")
        self.titulo["font"] = ("Arial", "15", "bold")
        self.titulo.pack()

        self.palavraLabel = Label(self.segundoContainer,text="Palavra: ", font=self.fontePadrao)
        self.palavraLabel.pack(side=LEFT)

        self.palavra = Entry(self.segundoContainer)
        self.palavra["width"] = 30
        self.palavra["font"] = self.fontePadrao
        self.palavra.pack(side=LEFT)
        
        self.autenticar = Button(self.quartoContainer)
        self.autenticar["text"] = "Analisar"
        self.autenticar["font"] = ("Calibri", "12")
        self.autenticar["width"] = 15
        self.autenticar["command"] = self.mandaPalavra
        self.autenticar.pack()
        
        self.mensagem = Label(self.quartoContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()
        
    def mandaPalavra(self):
        global palavra
        global numbers
        
        h = 0
        
        stringaux = self.palavra.get()

        while h < len(stringaux):
            if stringaux[h] == " " or stringaux[h] == "\n":
                h += 1
            palavra += stringaux[h] 
            h+=1

        if len(palavra) <= 0:
            self.mensagem["text"] =("Erro: Palavra vazia")
        if palavra[0] in numbers:
            self.mensagem["text"] =("Erro: Primeiro caracter não pode ser numero")
        else:
            analiser()
            self.mensagem["text"] = auxiliarPrint



root = Tk()
Application(root)
root.mainloop()