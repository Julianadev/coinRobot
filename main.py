from selenium import webdriver as controle
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pyautogui as controleTempo
from datetime import datetime
import os
import xlsxwriter


xpath_moeda = '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]'
def cotacao_moeda(navegador, moeda):
    navegador.get('https://google.com.br')
    controleTempo.sleep(3)
    navegador.find_element(By.NAME, 'q').send_keys(f'{moeda} hoje')
    controleTempo.sleep(3)
    navegador.find_element(By.NAME, 'q').send_keys(Keys.RETURN)
    controleTempo.sleep(3)
    contacao = navegador.find_elements(By.XPATH, xpath_moeda)[0].text
    controleTempo.sleep(3)
    return contacao

controleTempo.sleep(3)

navegador = controle.Edge()

retornandoDolar = cotacao_moeda(navegador, 'dolar')
retornandoEuro = cotacao_moeda(navegador, 'Euro')

navegador.close()

print(f'Dólar: {retornandoDolar}')
print(f'Euro: {retornandoEuro}')

try:
    salvar_arquivo = input('Deseja salvar o arquivo? S/N ')
except ValueError as e:
    print('Ocorreu um erro: ', e)

opcoes = {'1': 'TXT', '2': 'XLSX'}

escolha_usuario = input('Qual formato de arquivo você deseja salvar?\n[1] - .txt\n[2] - .xlsx ')

if escolha_usuario in opcoes:
    if salvar_arquivo.upper() == 'S':
        if escolha_usuario == '1':
            nome_arquivo = input('Digite um nome para o arquivo: ')
            if nome_arquivo:
                hora_atual = datetime.now()
                data_hora = hora_atual.strftime('%d/%m/%Y %H:%M:%S')
                if not nome_arquivo.endswith('txt'):
                    nome_arquivo += '.txt'
                if os.path.exists(nome_arquivo):
                    modo = 'a'
                else:
                    modo = 'w'
                with open(nome_arquivo, modo, encoding='UTF-8') as arquivo:
                    arquivo.write(f'{hora_atual} | Dólar: {retornandoDolar}  Euro: {retornandoEuro}')
                    print(f'Arquivo {nome_arquivo}.txt salvo com sucesso!')
            else:
                print('Nome do arquivo não pode ser vazio')
        elif escolha_usuario == '2':
            caminho_arquivo = "C:\\Users\\jully\\OneDrive\\Área de Trabalho\\Extracao_dolar_euro_excel.xlsx"
            criando_planilha = xlsxwriter.Workbook(caminho_arquivo)
            planilha = criando_planilha.add_worksheet()

            planilha.write('A1', 'DATA/HORA')
            planilha.write('B1', 'Moeda')
            planilha.write('C1', 'Valor')

            hora_atual = datetime.now()
            data_hora = hora_atual.strftime('%d/%m/%Y %H:%M:%S')

            planilha.write('A2', data_hora)
            planilha.write('B2', 'Dálar')
            planilha.write('C2', retornandoDolar)

            planilha.write('A3', data_hora)
            planilha.write('B3', 'Euro')
            planilha.write('C3', retornandoEuro)

            criando_planilha.close()

            print(f'Arquivo salvo com sucesso em {caminho_arquivo}')
            os.startfile(caminho_arquivo)

    else:
        print('Encerrando o programa...')
else:
    print('Opção inválida')
