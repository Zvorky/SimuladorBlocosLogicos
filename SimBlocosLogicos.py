#!/bin/python
# Simulador de formas de alocação de blocos lógicos

# Enzo Zavorski Delevatti - 199575@upf.br

# TDE Alocação de Arquivos
# Sistemas Operacionais II

# Dezembro 2024


import os


def Clear():
    if (os.getenv("OS")): # NT
        os.system("cls")
    else:
        os.system("clear")

def Contigua():
    FAT = [["FileName", "StartBlock", "Length"]]
    Disk = []
    Size = IntInput("Simulando Alocação Contigua\n\nInforme o tamanho do disco (em kB): ")

    for I in range(0, Size):
        Disk.append(0)
    PrintDisk(Disk, [" "])
    input()

def Encadeada():
    Size = IntInput("Simulando Alocação Encadeada\n\nInforme o tamanho do disco (em kB): ")

def Indexada():
    Size = IntInput("Simulando Alocação Indexada\n\nInforme o tamanho do disco (em kB): ")

def IntInput(Message : str, InvalidMessage : str = "Valor precisa ser Inteiro."):
    MustBeInt = None
    while(MustBeInt == None):
        MustBeInt = input(Message)
        try:
            MustBeInt = int(MustBeInt)
        except:
            Clear()
            print("\"{}\" - {}".format(MustBeInt, InvalidMessage))
            MustBeInt = None
    return MustBeInt

def PrintDisk(Disk : list, CharTable : list, Columns = 10):
    for I in range(0, len(Disk)):
        print("[{}]{}\t".format(CharTable[Disk[I]], I), end="") # CharTable serve apenas para distinguir pedaços de arquivos diferentes
        if not (I+1) % Columns:
            print() # Quebra de Linha

if __name__ == "__main__":
    Sel = -1
    while(Sel):
        Clear()
        print("Simulador Blocos Lógicos\nEnzo Zavorski Delevatti - 199575")
        Sel = IntInput("\nSelecione um Mecanismo de Alocação:\n1 - Contígua\n2 - Encadeada\n3 - Indexada\n\n0 - Sair\n\n> ", "Opção Inválida")

        match Sel:
            case 0:
                pass # Finaliza o While
            case 1:
                Contigua()
            case 2:
                Encadeada()
            case 3:
                Indexada()
            case _:
                input("Opção {} inválida.".format(Sel))
