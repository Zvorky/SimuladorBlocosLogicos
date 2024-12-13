#!/bin/python
# Simulador de formas de alocação de blocos lógicos

# Enzo Zavorski Delevatti - 199575@upf.br

# TDE Alocação de Arquivos
# Sistemas Operacionais II

# Dezembro 2024



import os, random, string



# ---[ Métodos de Alocação ]---

def ContiguaAdd(Disk : list, FAT : map, FileName : str, Length : int):
    if FileName in FAT.keys():
        return Disk, FAT, 2
    for I in range(0, len(Disk)):
        Null = True
        for L in range(I, I+Length):
            if not Disk[L] == "Null":
                Null = False
        if Null:
            FAT[FileName] = {
                "FileName" : FileName,
                "StartBlock" : I,
                "Length" : Length
            }
            for L in range(I, I+Length):
                Disk[L] = FileName
            return Disk, FAT, 0
    return Disk, FAT, 1 # Sem espaço contíguo

def ContiguaRem(Disk : list, FAT : map, FileName):
    FA = FAT[FileName]
    for I in range(FA["StartBlock"], FA["StartBlock"] + FA["Length"]):
        if Disk[I] == FileName:
            Disk[I] = "Null"
    FAT.pop(FileName)
    return Disk, FAT, 0


def EncadeadaAdd(Disk : list, FAT : map, FileName : str, Length : int):
    return Disk, FAT, 0

def EncadeadaRem(Disk : list, FAT : map, FileName):
    return Disk, FAT, 0


def IndexadaAdd(Disk : list, FAT : map, FileName : str, Length : int):
    return Disk, FAT, 0

def IndexadaRem(Disk : list, FAT : map, FileName):
    return Disk, FAT, 0


# ---[ Simulador ]---

def Simulation(Method : int, MethodName : str):
    Disk = MakeDisk()
    FAT = {}
    CharMap = {"Null" : " "}
    ErrorCode = 0

    Add = [
        ContiguaAdd,
        EncadeadaAdd,
        IndexadaAdd
    ]

    Rem = [
        ContiguaRem,
        EncadeadaRem,
        IndexadaRem
    ]

    Sel = -1
    while(Sel):
        Clear()
        print("Simulando Alocação {}.\n".format(MethodName))
        PrintDisk(Disk, CharMap)
        print("\nFile Allocation Table:")
        PrintFAT(FAT, CharMap)

        if ErrorCode:
            match Sel:
                case 1:
                    print("\nErro ao criar arquivo.")
                case 2:
                    print("\nErro ao remover arquivo.")

        Sel = IntInput("\n1 - Adicionar Arquivo\n2 - Remover Arquivo\n\n> ", "Opção Inválida")
        match Sel:
            case 0:
                pass
            case 1:
                Disk, FAT, ErrorCode = Add[Method-1](Disk, FAT, input("Nome do Arquivo: "), IntInput("Tamanho do Arquivo (Blocos): "))
            case 2:
                FileName = input("Nome do Arquivo: ")
                if (FileName in FAT.keys()):
                    Disk, FAT, ErrorCode = Rem[Method-1](Disk, FAT, FileName)
                else:
                    input("Arquivo não encontrado na Tabela de Alocação de Arquivos (FAT).")
            case _:
                input("Opção {} inválida.".format(Sel))
                Sel = -1

        for FileName in FAT.keys():
            if FileName not in CharMap.keys():
                CharMap[FileName] = NewChar(CharMap)

def MakeDisk():
    Disk = []
    Size = IntInput("Informe o tamanho do disco (Em Blocos): ")
    for I in range(0, Size):
        Disk.append("Null")
    return Disk


# ---[ Utilitário ]---

def Clear():
    if (os.getenv("OS")): # NT
        os.system("cls")
    else:
        os.system("clear")

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

def PrintDisk(Disk : list, CharMap : dict, Columns = 10):
    for I in range(0, len(Disk)):
        print("[{}]{}\t".format(CharMap[Disk[I]], I), end="") # CharMap serve apenas para distinguir pedaços de arquivos diferentes
        if not (I+1) % Columns:
            print() # Quebra de Linha

def PrintFAT(FAT : dict, CharMap : dict = {}):
    if len(FAT) and CharMap:
        print(end="    ")

    PrintedKeys = False
    for FA in FAT.values():
        if not PrintedKeys:
            for Key in FA.keys():
                print(Key, end="        ")
            print()
            PrintedKeys = True
        if CharMap:
            print(CharMap[FA["FileName"]], end="\t")
        for Value in FA.values():
            print(Value, end="\t\t")
        print()

def RandChar():
    Chars = string.ascii_letters + string.digits + string.punctuation
    return random.choice(Chars)

def NewChar(CharMap : dict):
    Char = RandChar()
    while Char in CharMap.values():
        Char = RandChar()
    return Char


# ---[ Menu Principal ]---

def Menu():
    Sel = -1
    while(Sel):
        Clear()
        print("Simulador Blocos Lógicos\nEnzo Zavorski Delevatti - 199575")
        Sel = IntInput("\nSelecione um Mecanismo de Alocação:\n1 - Contígua\n2 - Encadeada\n3 - Indexada\n\n0 - Sair\n\n> ", "Opção Inválida")

        match Sel:
            case 0:
                pass # Finaliza o While
            case 1:
                Simulation(Sel, "Contigua")
            case 2:
                Clear()
                input("Não Implementado.\n\n")
                # Simulation(Sel, "Encadeada")
            case 3:
                Clear()
                input("Não Implementado.\n\n")
                # Simulation(Sel, "Indexada")
            case _:
                input("Opção {} inválida.".format(Sel))

    Clear()
    print("Valeu!")

if __name__ == "__main__":
    Menu()