import pyautogui
import time

pyautogui.PAUSE = 0.8

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

pyautogui.hotkey("ctrl", "l")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press ("enter")

time.sleep(1)

pyautogui.PAUSE = 0.5

pyautogui.click(x=801, y=371)
pyautogui.write("cauabap@gmail.com")
pyautogui.click(x=717, y=471)
pyautogui.write("Caua13bap")

pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(1)

import pandas

tabela = pandas.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index:
    pyautogui.click(x=826, y=259)
    codigo =  tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)

    pyautogui.press("tab")
    marca =  tabela.loc[linha, "marca"]
    pyautogui.write(marca)

    pyautogui.press("tab")
    tipo =  tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)

    pyautogui.press("tab")
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)

    pyautogui.press("tab")
    preco_unitario = str (tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)

    pyautogui.press("tab")
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)

    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]

    if obs != "nan":
        pyautogui.write(obs)

    pyautogui.write("obs")
    pyautogui.press("enter")

