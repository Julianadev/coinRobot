from selenium import webdriver as controle
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pyautogui as controleTempo
import os
from datetime import datetime



xpath_moeda = '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]'

def buscar_cotacao(navegador, moeda):
    navegador.get('https://google.com.br')
    navegador.find_element(By.NAME, 'q').send_keys(f'{moeda} hoje')
    controleTempo.sleep(3)
    navegador.find_element(By.NAME, 'q').send_keys(Keys.RETURN)
    controleTempo.sleep(3)
    cotacao = navegador.find_elements(By.XPATH, xpath_moeda)[0].text
    controleTempo.sleep(3)
    return cotacao

controleTempo.sleep(3)

# Abre navegador
navegador = controle.Edge()

# Dólar
retornandoDolar = buscar_cotacao(navegador, 'dolar')

# Euro
retornandoEuro = buscar_cotacao(navegador, 'euro')

navegador.close()

# Imprime no console o retorno dos valores
print(f'Dólar: {retornandoDolar}')
print(f'Euro: {retornandoEuro}')

# Salva os resultado em um arquivo .txt
try:
    salvar_resultado = input('Deseja salvar o resultado? S/N ')
except ValueError as e:
    print('Ocorreu um erro: ', e)

if salvar_resultado.upper() == 'S':
    nome_arquivo = input('Digite o nome do arquivo: ')
    if nome_arquivo:
        agora = datetime.now()
        data_hora = agora.strftime('%d/%m/%Y %H:%M:%S')
        if nome_arquivo.endswith('txt'):
            nome_arquivo += '.txt'
        if os.path.exists(nome_arquivo):
            modo = 'a'
        else:
            modo = 'w'
        with open(nome_arquivo, modo, encoding='UTF-8') as arquivo:
            arquivo.write(f'{data_hora} | Dólar {retornandoDolar}  Euro: {retornandoEuro}\n')
            print(f'Arquivo {nome_arquivo}.txt salvo com sucesso!')
    else:
        print('Nome do arquivo não pode ser vazio')
else:
    print('Encerrando o programa')








