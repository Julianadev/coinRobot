from selenium import webdriver as controle
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
from datetime import datetime
import os
import traceback
import logging


xpath_moeda = '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]'
def cotacao_moeda(navegador, moeda):
    navegador.get('https://google.com.br')

    try:
        WebDriverWait(navegador, 10).until(EC.visibility_of_element_located((By.NAME, 'q')))
        navegador.find_element(By.NAME, 'q').send_keys(f'{moeda} hoje')
        navegador.find_element(By.NAME, 'q').send_keys(Keys.RETURN)
        WebDriverWait(navegador, 10).until(EC.visibility_of_element_located((By.NAME, 'q')))
        cotacao = navegador.find_elements(By.XPATH, xpath_moeda)[0].text
        return cotacao
    except Exception as e:
        traceback.print_exc()
        logging.exception('Mensagem de erro: ', e)
        return None

def salvar_arquivo_txt(data_hora, retornandoDolar, retornandoEuro):
    nome_arquivo = input('Digite um nome para o arquivo: ')
    if nome_arquivo.lower():
        if not nome_arquivo.endswith('txt'):
            nome_arquivo += '.txt'
        modo = 'a' if os.path.exists(nome_arquivo) else 'w'
        with open(nome_arquivo, modo, encoding='UTF-8') as arquivo:
            arquivo.write(f'{data_hora} | Dólar: {retornandoDolar}  Euro: {retornandoEuro}\n')
            print(f'Arquivo {nome_arquivo} salvo com sucesso!')
    else:
        print('Nome do arquivo não pode ser vazio')

def salvar_arquivo_xlsx(caminho_arquivo, data_hora, retornandoDolar, retornandoEuro):
    try:
        if caminho_arquivo.lower().endswith(('.xls', '.xlsx', '.csv')):
            caminho_arquivo = os.path.abspath(caminho_arquivo)
            df = pd.DataFrame(columns=['HORA/DATA', 'MOEDA', 'VALOR'])

            df_leitura = pd.read_excel(caminho_arquivo)

            df.loc[len(df.index)] = data_hora, 'Dólar', retornandoDolar
            df.loc[len(df.index)] = data_hora, 'Euro', retornandoEuro

            df.to_excel(caminho_arquivo, index=False)

            print(f'Arquivo salvo com sucesso em {caminho_arquivo}')
            os.startfile(caminho_arquivo)
        else:
            print('Extensão de arquivo inválida. Encerrando o programa...')
    except FileNotFoundError as e:
        print(f'Caminho inválido: {e}')


options = controle.EdgeOptions()
options.add_argument('--headless=new')
navegador = controle.Edge(options=options)
print('Coletando os dados...Aguarde')

retornandoDolar = cotacao_moeda(navegador, 'dolar')
retornandoEuro = cotacao_moeda(navegador, 'Euro')

navegador.close()

print(f'Dólar: {retornandoDolar}')
print(f'Euro: {retornandoEuro}')

def main():
    try:
        salvar_arquivo = input('Deseja salvar o arquivo? S/N ')
        opcoes = {'1': 'TXT', '2': 'XLSX'}
        escolha_usuario = input('Qual formato de arquivo você deseja salvar?\n[1] - .txt\n[2] - .xlsx\n ').lower()
    except Exception as e:
        print('Ocorreu um erro: ', e)
        return

    if escolha_usuario in opcoes:
        if salvar_arquivo.upper() == 'S':
            if escolha_usuario == '1':
                hora_atual = datetime.now()
                data_hora = hora_atual.strftime('%d/%m/%Y %H:%M:%S')
                salvar_arquivo_txt(data_hora, retornandoDolar, retornandoEuro)
            elif escolha_usuario == '2':
                caminho_arquivo = input('Digite o caminho do arquivo: ').strip('"')
                hora_atual = datetime.now()
                data_hora = hora_atual.strftime('%d/%m/%Y %H:%M:%S')
                salvar_arquivo_xlsx(caminho_arquivo, data_hora, retornandoDolar, retornandoEuro )
            else:
                print('Opção inválida. Escolha 1(.TXT) ou 2(.XLSX)')
        else:
            print('Encerrando o programa...')
    else:
        print('Opção inválida.')

if __name__ == "__main__":
    main()



