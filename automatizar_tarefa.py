# AUTOMATIZAÇÃO DE CADASTRO DE PRODUTOS

# Código Python para cadastro automático de mais de 300 produtos com apenas 1 clique no código.
# Pode ser utilizado em todas as tarefas diárias que queira automatizar e melhorar sua produtividade.
# Atentar à pequenas variações do código que possa ocorrer em diferentes tamanhos de telas (monitores/notebooks) e local de disposição dos arquivos.


# SOBRE AS BIBLIOTECAS

# Pyautogui -> para operações com mouse e teclado
    # pyautogui.click -> para clicar
    # pyautogui.write -> para escrever
    # pyautogui.press -> para pressionar uma tecla
    # pyautogui.hotkey -> para usar atalho no teclado
# Time -> para adicionar tempo do código
# Pandas -> para criar e visualizar uma tabela com a base de dados


# INSTRUÇÕES FINAIS

# Quando aparecer (x=000, y=000) no código, pegar a posição do cursor do mouse com o arquivo auxiliar 'pegar_posição.py' disponibilizado juntamente com este arquivo.
# Necessário adaptar o link, e-mail, senha e posições x,y às suas configurações.
# Lembrar de salvar base de dados (arquivo csv) na mesma pasta do código.

# Importar bibliotecas
import pyautogui
import time
import pandas

# Pausa no código (em função da velocidade da conexão)
pyautogui.PAUSE = 0.5

# Variáveis
link = 'https://forms.gle/i3ySAwUYvJQR11vK9'
tabela = pandas.read_csv('produtos.csv')

# Abrir navegador e entrar na planilha para cadastrar os produtos
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
pyautogui.write(link)
pyautogui.press('enter')
time.sleep(3)

# Fazer login no sistema (se necessário)
pyautogui.click(x=000, y=000)
pyautogui.write('email')
pyautogui.press('tab')
pyautogui.white('senha')
pyautogui.press('tab')
pyautogui.press('enter')
time.sleep(3)

# Cadastrar 1 produtos (preencher campos) e repetir o processo de cadastro até acabar os produtos (para cada linha da tabela)
for linha in tabela.index:    
    pyautogui.click(x=000, y=000)
    
    codigo = tabela.loc[linha, 'codigo']
    pyautogui.write(codigo)
    pyautogui.press('tab')

    pyautogui.write(tabela.loc[linha, 'marca'])
    pyautogui.press('tab')

    pyautogui.write(tabela.loc[linha, 'tipo'])
    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha, 'categoria']))
    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha, 'preco_unitario']))
    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha, 'custo']))
    pyautogui.press('tab')

    obs = tabela.loc[linha, 'obs']
    if not pandas.isna(obs):
        pyautogui.write(tabela.loc[linha, 'obs'])
    pyautogui.press('tab')
        
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.press('tab')
    pyautogui.press('enter')