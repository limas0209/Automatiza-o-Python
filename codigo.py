# AUTOMATIZANDO TAREFAS EM PYTHON

#imports
import pyautogui
import time
import pandas as pd
import keyboard

#PASSO 1: ENTRANDO NO SISTEMA DA EMPRESA https://dlp.hashtagtreinamentos.com/python/intensivao/login


#pyautogui.write -> escrever texto
#pyautogui.click -> clicar com o mouse
#pyautogui.press -> apertar uma tecla
#pyautogui.hotkey -> apertar um atalho de teclado (Ctrl, C)

#Colocar uma pausa
pyautogui.PAUSE = 0.5


#abrir o navegador
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")




#Entrando no link
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")

pyautogui.press("enter")

#Dando uma pausa para carregar a página
time.sleep(2.5)
pyautogui.click(x=-1216, y=413)
pyautogui.write("riquelima00@gmail.com")
pyautogui.press("tab")
pyautogui.write("Rique009")                         
pyautogui.press("tab")
pyautogui.click(x=-918, y=582)

#Passo 2: Importar a base de dados

tabela = pd.read_csv("produtos.csv")
print(tabela)




#Passo 3: Cadastrando um produto


for linha in tabela.index:
    #Selecionando 1 campo 
    pyautogui.click(x=-1076, y=295)
    
    #Código
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    #Marca
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    #Tipo
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    #Categoria
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    #Preço unitário
    preço_unitario = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preço_unitario))
    pyautogui.press("tab")

    #Custo
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    #Obs
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(obs))
    pyautogui.press("tab")

    #Enviando
    pyautogui.press("enter")


    #Voltando ao topo
    pyautogui.press("home")


