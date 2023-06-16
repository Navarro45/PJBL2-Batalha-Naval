import time
import os
import random

contador=[1,5,5,1]
letra=["E","D","C","B","A"]
## Aqui estão os tabuleiros e as funções para imprimir.
tabuleiro1 = [
    [".",".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".",".","."]
]
tabuleiro2 = [
    [".",".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".",".","."]
]
tabuleiro3 = [
    [".",".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".",".","."]
]
tabuleiro4 = [
    [".",".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".",".","."]
]

def tabuleiroJogador():
    print(" | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 ")
    print("_|___|___|___|___|___|___|___|___|___|___|")
    print(f"1| {tabuleiro1[0][0]} | {tabuleiro1[0][1]} | {tabuleiro1[0][2]} | {tabuleiro1[0][3]} | {tabuleiro1[0][4]} | {tabuleiro1[0][5]} | {tabuleiro1[0][6]} | {tabuleiro1[0][7]} | {tabuleiro1[0][8]} | {tabuleiro1[0][9]} |")
    print("_|___|___|___|___|___|___|___|___|___|___|")
    print(f"2| {tabuleiro1[1][0]} | {tabuleiro1[1][1]} | {tabuleiro1[1][2]} | {tabuleiro1[1][3]} | {tabuleiro1[1][4]} | {tabuleiro1[1][5]} | {tabuleiro1[1][6]} | {tabuleiro1[1][7]} | {tabuleiro1[1][8]} | {tabuleiro1[1][9]} |")
    print("_|___|___|___|___|___|___|___|___|___|___|")
    print(f"3| {tabuleiro1[2][0]} | {tabuleiro1[2][1]} | {tabuleiro1[2][2]} | {tabuleiro1[2][3]} | {tabuleiro1[2][4]} | {tabuleiro1[2][5]} | {tabuleiro1[2][6]} | {tabuleiro1[2][7]} | {tabuleiro1[2][8]} | {tabuleiro1[2][9]} |")
    print("_|___|___|___|___|___|___|___|___|___|___|")
    print(f"4| {tabuleiro1[3][0]} | {tabuleiro1[3][1]} | {tabuleiro1[3][2]} | {tabuleiro1[3][3]} | {tabuleiro1[3][4]} | {tabuleiro1[3][5]} | {tabuleiro1[3][6]} | {tabuleiro1[3][7]} | {tabuleiro1[3][8]} | {tabuleiro1[3][9]} |")
    print("_|___|___|___|___|___|___|___|___|___|___|")
    print(f"5| {tabuleiro1[4][0]} | {tabuleiro1[4][1]} | {tabuleiro1[4][2]} | {tabuleiro1[4][3]} | {tabuleiro1[4][4]} | {tabuleiro1[4][5]} | {tabuleiro1[4][6]} | {tabuleiro1[4][7]} | {tabuleiro1[4][8]} | {tabuleiro1[4][9]} |")
    print("_|___|___|___|___|___|___|___|___|___|___|")
def tabuleiroJogadorTiro():
    print(" | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 ")
    print("_|___|___|___|___|___|___|___|___|___|___|")
    print(f"1| {tabuleiro3[0][0]} | {tabuleiro3[0][1]} | {tabuleiro3[0][2]} | {tabuleiro3[0][3]} | {tabuleiro3[0][4]} | {tabuleiro3[0][5]} | {tabuleiro3[0][6]} | {tabuleiro3[0][7]} | {tabuleiro3[0][8]} | {tabuleiro3[0][9]} |")
    print("_|___|___|___|___|___|___|___|___|___|___|")
    print(f"2| {tabuleiro3[1][0]} | {tabuleiro3[1][1]} | {tabuleiro3[1][2]} | {tabuleiro3[1][3]} | {tabuleiro3[1][4]} | {tabuleiro3[1][5]} | {tabuleiro3[1][6]} | {tabuleiro3[1][7]} | {tabuleiro3[1][8]} | {tabuleiro3[1][9]} |")
    print("_|___|___|___|___|___|___|___|___|___|___|")
    print(f"3| {tabuleiro3[2][0]} | {tabuleiro3[2][1]} | {tabuleiro3[2][2]} | {tabuleiro3[2][3]} | {tabuleiro3[2][4]} | {tabuleiro3[2][5]} | {tabuleiro3[2][6]} | {tabuleiro3[2][7]} | {tabuleiro3[2][8]} | {tabuleiro3[2][9]} |")
    print("_|___|___|___|___|___|___|___|___|___|___|")
    print(f"4| {tabuleiro3[3][0]} | {tabuleiro3[3][1]} | {tabuleiro3[3][2]} | {tabuleiro3[3][3]} | {tabuleiro3[3][4]} | {tabuleiro3[3][5]} | {tabuleiro3[3][6]} | {tabuleiro3[3][7]} | {tabuleiro3[3][8]} | {tabuleiro3[3][9]} |")
    print("_|___|___|___|___|___|___|___|___|___|___|")
    print(f"5| {tabuleiro3[4][0]} | {tabuleiro3[4][1]} | {tabuleiro3[4][2]} | {tabuleiro3[4][3]} | {tabuleiro3[4][4]} | {tabuleiro3[4][5]} | {tabuleiro3[4][6]} | {tabuleiro3[4][7]} | {tabuleiro3[4][8]} | {tabuleiro3[4][9]} |")
    print("_|___|___|___|___|___|___|___|___|___|___|")
def tabuleiroRoboTiro():
    print(" | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 ")
    print("_|___|___|___|___|___|___|___|___|___|___|")
    print(f"1| {tabuleiro4[0][0]} | {tabuleiro4[0][1]} | {tabuleiro4[0][2]} | {tabuleiro4[0][3]} | {tabuleiro4[0][4]} | {tabuleiro4[0][5]} | {tabuleiro4[0][6]} | {tabuleiro4[0][7]} | {tabuleiro4[0][8]} | {tabuleiro4[0][9]} |")
    print("_|___|___|___|___|___|___|___|___|___|___|")
    print(f"2| {tabuleiro4[1][0]} | {tabuleiro4[1][1]} | {tabuleiro4[1][2]} | {tabuleiro4[1][3]} | {tabuleiro4[1][4]} | {tabuleiro4[1][5]} | {tabuleiro4[1][6]} | {tabuleiro4[1][7]} | {tabuleiro4[1][8]} | {tabuleiro4[1][9]} |")
    print("_|___|___|___|___|___|___|___|___|___|___|")
    print(f"3| {tabuleiro4[2][0]} | {tabuleiro4[2][1]} | {tabuleiro4[2][2]} | {tabuleiro4[2][3]} | {tabuleiro4[2][4]} | {tabuleiro4[2][5]} | {tabuleiro4[2][6]} | {tabuleiro4[2][7]} | {tabuleiro4[2][8]} | {tabuleiro4[2][9]} |")
    print("_|___|___|___|___|___|___|___|___|___|___|")
    print(f"4| {tabuleiro4[3][0]} | {tabuleiro4[3][1]} | {tabuleiro4[3][2]} | {tabuleiro4[3][3]} | {tabuleiro4[3][4]} | {tabuleiro4[3][5]} | {tabuleiro4[3][6]} | {tabuleiro4[3][7]} | {tabuleiro4[3][8]} | {tabuleiro4[3][9]} |")
    print("_|___|___|___|___|___|___|___|___|___|___|")
    print(f"5| {tabuleiro4[4][0]} | {tabuleiro4[4][1]} | {tabuleiro4[4][2]} | {tabuleiro4[4][3]} | {tabuleiro4[4][4]} | {tabuleiro4[4][5]} | {tabuleiro4[4][6]} | {tabuleiro4[4][7]} | {tabuleiro4[4][8]} | {tabuleiro4[4][9]} |")
    print("_|___|___|___|___|___|___|___|___|___|___|")
def jogo():
    print("Computador")
    tabuleiroRoboTiro()
    print("\n========================================================================\n")
    print("Jogador")
    tabuleiroJogadorTiro()
def EscolhaInválida():
    os.system('cls')
    print("========================================================================")
    print("Escolha inválida\nEscolha novamente")
    print("========================================================================")
os.system('cls')

## Para criar um loop de jogo nós usamos um while com a variável temporizador
while contador[0]==1:
    ## Aqui nós resetamos o tabuleiro
    for i in range(10):
        for k in range(5):
            tabuleiro1[k][i]="."
    for i in range(10):
        for k in range(5):
            tabuleiro2[k][i]="."
    for i in range(10):
        for k in range(5):
            tabuleiro3[k][i]="."
    for i in range(10):
        for k in range(5):
            tabuleiro4[k][i]="."
    ##Aqui é o loop para o jogador colocar os barcos
    while contador[1] > 0:
        tabuleiroJogador()

        print("========================================================================")
        if letra.count("E")==1:
            print("Escolha 1 para escolher o Destroier, ele ocupa 1 espaço")
        if letra.count("D")==1:
            print("Escolha 2 para escolher o Submarino, ele ocupa 2 espaços")
        if letra.count("C")==1:
            print("Escolha 3 para escolher o Contra-torpedeiro, ele ocupa 3 espaços")
        if letra.count("B")==1:
            print("Escolha 4 para escolher o Navio-tanque, ele ocupa 4 espaços")
        if letra.count("A")==1:
            print("Escolha 5 para escolher o Porta aviões, ele ocupa 5 espaços")
        print("========================================================================")
        print("          4")
        print("          ^")
        print("1  <   Direções   >  3")
        print("          v")
        print("          2")
        print("========================================================================")

        letra2=[]
        tipo = int(input("Digite o barco desejado:"))
        ##Aqui ficam 
        if tipo<1 or tipo>5:
            EscolhaInválida()
            continue
        if letra[tipo-1]==".":
            EscolhaInválida()
            continue
        coluna1 = int(input("Digite a coluna desejada para o comeco do barco:"))
        if coluna1<1 or coluna1>10:
            EscolhaInválida()
            continue
        linha1 = int(input("Digite a linha desejada para o comeco do barco:"))
        if linha1<1 or linha1>5:
            EscolhaInválida()
            continue
        direção = int(input("Digite a direção desejada para o barco:"))

        if direção<1 or direção>4:
            EscolhaInválida()
            continue
        if direção==1 and coluna1-tipo<0:
            EscolhaInválida()
            continue
        elif direção==2 and linha1+tipo>6:
            EscolhaInválida()
            continue
        elif direção==3 and coluna1+tipo>11:
            EscolhaInválida()
            continue
        elif direção==4 and linha1-tipo<0:
            EscolhaInválida()
            continue
        linha1-=1

        if direção==1:
            for k in range(coluna1-tipo,coluna1):
                if tabuleiro1[linha1][k]==".":
                    letra2.append(tabuleiro1[linha1][k])
            if letra2.count(".")==tipo:
                for i in range(coluna1-tipo,coluna1):
                    tabuleiro1[linha1][i] = letra[tipo-1]
            else:
                EscolhaInválida()
                continue
        if direção==2:
            for k in range(linha1,linha1+tipo):
                if tabuleiro1[k][coluna1-1]==".":
                    letra2.append(tabuleiro1[k][coluna1-1])
            if letra2.count(".")==tipo:
                for i in range(linha1,linha1+tipo):
                    tabuleiro1[i][coluna1-1] = letra[tipo-1]
            else:
                EscolhaInválida()
                continue
        if direção==3:
            for k in range(coluna1-1,coluna1+tipo-1):
                if tabuleiro1[linha1][k]==".":
                    letra2.append(tabuleiro1[linha1][k])
            if letra2.count(".")==tipo:
                for i in range(coluna1-1,coluna1+tipo-1):
                    tabuleiro1[linha1][i] = letra[tipo-1]
            else:
                EscolhaInválida()
                continue
        if direção==4:
            for k in range(linha1-tipo,linha1):
                if tabuleiro1[k][coluna1-1]==".":
                    letra2.append(tabuleiro1[k][coluna1-1])
            if letra2.count(".")==tipo:
                for i in range(linha1-tipo+1,linha1+1):
                    tabuleiro1[i][coluna1-1] = letra[tipo-1]
            else:
                EscolhaInválida()
                continue
        contador[1]-= 1
        letra[tipo-1]="."
        os.system('cls')
    tabuleiroJogador()
    contador[1]=1
    time.sleep(1)
    while contador[2] > 0:
        letra=["E","D","C","B","A"]
        letra1=letra[contador[2]-1]
        letra2=[]
        coluna1 = random.randint(0,9)
        linha1 = random.randint(0,4)
        posição = random.randint(1,2)
        if posição==1 and coluna1+contador[2]>9:
            coluna1=10-contador[2]
        if posição==2 and linha1+contador[2]>4:
            linha1=5-contador[2]
        
        if posição==1:
            for k in range(coluna1,coluna1+contador[2]):
                if tabuleiro2[linha1][k]==".":
                    letra2.append(tabuleiro2[linha1][k])
            if letra2.count(".")==contador[2]:
                for i in range(coluna1,coluna1+contador[2]):
                    tabuleiro2[linha1][i] = letra1
            else:
                continue
        if posição==2:
            for k in range(linha1,linha1+contador[2]):
                if tabuleiro2[k][coluna1]==".":
                    letra2.append(tabuleiro2[k][coluna1])
            if letra2.count(".")==contador[2]:
                for i in range(linha1,linha1+contador[2]):
                    tabuleiro2[i][coluna1] = letra1
            else:
                continue
        contador[2] -= 1
    contador[2]=1










    NavioJogador=[0,0,0,0,0,0]
    NavioCPU=[0,0,0,0,0,0,5]
    Atirado=[
    [".",".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".",".","."]
    ]
    Condição=[0,0]
    Placar=[0,0]
    NavioJogadorCondição=[1,1,1,1,1]
    NavioCPUCondição=[1,1,1,1,1]
    for i in range(0,10):
        for k in range(0,5):
            if tabuleiro1[k][i]!=".":
                NavioJogador[0]+=1
    for i in range(0,10):
        for k in range(0,5):
            if tabuleiro2[k][i]!=".":
                NavioCPU[0]+=1
    os.system('cls')
    while NavioJogador[0]>0 and NavioCPU[0]>0:
        jogo()
        if Condição[0]==1:
            print("========================================================================")
            print("Você acertou")
            print("========================================================================")
        if Condição[0]==2:
            print("========================================================================")
            print("Você errou")
            print("========================================================================")
        if Condição[1]==1:
            print("O computador acertou")
            print("========================================================================")
        if Condição[1]==2:
            print("O computador errou")
            print("========================================================================")
        for i in range(1,5):
            NavioJogador[i]=0
            NavioCPU[i]=0
        for i in range(0,5):
            for k in range(0,10):
                if tabuleiro1[i][k]=="A":
                    NavioJogador[1]+=1
                if tabuleiro2[i][k]=="A":
                    NavioCPU[1]+=1
                if tabuleiro1[i][k]=="B":
                    NavioJogador[2]+=1
                if tabuleiro2[i][k]=="B":
                    NavioCPU[2]+=1
                if tabuleiro1[i][k]=="C":
                    NavioJogador[3]+=1
                if tabuleiro2[i][k]=="C":
                    NavioCPU[3]+=1
                if tabuleiro1[i][k]=="D":
                    NavioJogador[4]+=1
                if tabuleiro2[i][k]=="D":
                    NavioCPU[4]+=1
                if tabuleiro1[i][k]=="E":
                    NavioJogador[5]+=1
                if tabuleiro2[i][k]=="E":
                    NavioCPU[5]+=1
        if NavioCPU[1]==0 and NavioCPUCondição[0]==1:
            print("Você destruiu o Porta-aviões inimigo!")
            NavioCPUCondição[0]-=1
            NavioCPU[6]-=1
        if NavioCPU[2]==0 and NavioCPUCondição[1]==1:
            print("Você destruiu o Navio-Tanque inimigo!")
            NavioCPUCondição[1]-=1
            NavioCPU[6]-=1
        if NavioCPU[3]==0 and NavioCPUCondição[2]==1:
            print("Você destruiu o Contra-Torpedeiro inimigo!")
            NavioCPUCondição[2]-=1
            NavioCPU[6]-=1
        if NavioCPU[4]==0 and NavioCPUCondição[3]==1:
            print("Você destruiu o Submarino inimigo!")
            NavioCPUCondição[3]-=1
            NavioCPU[6]-=1
        if NavioCPU[5]==0 and NavioCPUCondição[4]==1:
            print("Você destruiu o Destroier inimigo!")
            NavioCPUCondição[4]-=1
            NavioCPU[6]-=1
        if NavioJogador[1]==0 and NavioJogadorCondição[0]==1:
            print("Você perdeu seu Porta-aviões!")
            NavioJogadorCondição[0]-=1
        if NavioJogador[2]==0 and NavioJogadorCondição[1]==1:
            print("Você perdeu seu Navio-Tanque!")
            NavioJogadorCondição[1]-=1
        if NavioJogador[3]==0 and NavioJogadorCondição[2]==1:
            print("Você perdeu seu Contra-Torpedeiro!")
            NavioJogadorCondição[2]-=1
        if NavioJogador[4]==0 and NavioJogadorCondição[3]==1:
            print("Você perdeu seu Submarino!")
            NavioJogadorCondição[3]-=1
        if NavioJogador[5]==0 and NavioJogadorCondição[4]==1:
            print("Você perdeu seu Destroier!")
            NavioJogadorCondição[4]-=1
        print(f"Navios inimigos restantes:{NavioCPU[6]}")
        print("========================================================================")
        tiroColunaJ=int(input("Escolha a coluna para atirar:"))
        if tiroColunaJ>10 or tiroColunaJ<1:
            EscolhaInválida()
            continue
        tiroColunaJ-=1
        tiroLinhaJ=int(input("Escolha a linha para atirar:"))
        if tiroLinhaJ>5 or tiroLinhaJ<1:
            EscolhaInválida()
            continue
        tiroLinhaJ-=1
        contador[3]=1
        while contador[3]>0:
            tiroColunaCPU=random.randint(0,9)
            tiroLinhaCPU=random.randint(0,4)
            if Atirado[tiroLinhaCPU][tiroColunaCPU]!=".":
                continue
            Atirado[tiroLinhaCPU][tiroColunaCPU]="0"
            contador[3]=0
        if tabuleiro2[tiroLinhaJ][tiroColunaJ]!=".":
            tabuleiro3[tiroLinhaJ][tiroColunaJ]="X"
            tabuleiro2[tiroLinhaJ][tiroColunaJ]="."
            Condição[0]=1
            NavioCPU[0]-=1
        elif tabuleiro2[tiroLinhaJ][tiroColunaJ]==".":
            tabuleiro3[tiroLinhaJ][tiroColunaJ]="o"
            Condição[0]=2
        else:
            os.system('cls')
            print("========================================================================")
            print("Você já escolheu esse espaço")
            print("========================================================================")
            continue
        if tabuleiro1[tiroLinhaCPU][tiroColunaCPU]!=".":
            tabuleiro4[tiroLinhaCPU][tiroColunaCPU]="X"
            tabuleiro1[tiroLinhaCPU][tiroColunaCPU]="."
            Condição[1]=1
            NavioJogador[0]-=1
        else:
            tabuleiro4[tiroLinhaCPU][tiroColunaCPU]="o"
            Condição[1]=2
        os.system('cls')
    if NavioCPU[0]==0:
        print("========================================================================")
        print("Parabéns!!! Você venceu!")
        Placar[0]+=1
    if NavioJogador[0]==0:
        print("========================================================================")
        print("Parabéns!!! Você perdeu!")
        Placar[1]+=1
    print("\n========================================================================")
    print("O placar é:")
    print(f"Seu placar é {Placar[0]}")
    print(f"O placar do computador é {Placar[1]}")
    print("\n========================================================================")
    contador[0]=int(input("Se você deseja continuar digite 1 e você deseja sair digite qualquer outro valor: "))
print("Obrigado por Jogar!!!")