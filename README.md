# Projeto de Busca de Cotação de Moedas

Este projeto usa Selenium e Python para buscar cotações de moedas automaticamente.

## Dependências

O projeto depende das seguintes bibliotecas Python:

- Selenium
- pandas
- os
- datetime
- traceback
- logging

## Como usar

1. Certifique-se de que todas as dependências estão instaladas.
2. Execute o script Python principal.

O script irá buscar as cotações do Dólar e do Euro, e perguntará se você deseja salvar essas informações em um arquivo. Você pode escolher entre salvar em um arquivo .txt ou .xlsx.

## Detalhes do Script

O script contém várias funções:

- `cotacao_moeda()`: Esta função busca a cotação de uma moeda no Google.
- `salvar_arquivo_txt()`: Esta função salva as cotações em um arquivo .txt.
- `salvar_arquivo_xlsx()`: Esta função salva as cotações em um arquivo .xlsx.
- `main()`: Esta é a função principal que chama as outras funções e controla o fluxo do programa.

## Contribuindo

Contribuições para este projeto são bem-vindas. Por favor, abra uma issue ou um pull request se você quiser contribuir.

## Licença

Este projeto é licenciado sob os termos da licença MIT.
