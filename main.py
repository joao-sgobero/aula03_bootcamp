# ==============================================================================
# EXERCÍCIOS: ESTRUTURAS CONDICIONAIS (IF, ELIF, ELSE)
# ==============================================================================

# Exercício 1: Verificação de Qualidade de Dados
# Você está analisando um conjunto de dados de vendas e precisa garantir que todos 
# os registros tenham valores positivos para quantidade e preço. Escreva um 
# programa que verifique esses campos e imprima "Dados válidos" se ambos forem 
# positivos ou "Dados inválidos" caso contrário.
#

# try:
#     quantidade = int(input("Digite uma quantidade: "))
#     preco = float(input("Digite um valor: "))
    
#     if quantidade > 0 and preco > 0:
#         print("Dados válidos")
#     else: 
#         print("Dados inválidos")

# except ValueError:
#     print("Digite apenas números")

# Exercício 2: Classificação de Dados de Sensor
# Imagine que você está trabalhando com dados de sensores IoT. Os dados incluem 
# medições de temperatura. Você precisa classificar cada leitura como 'Baixa', 
# 'Normal' ou 'Alta'. Considerando que:
# - Temperatura < 18°C é 'Baixa'
# - Temperatura >= 18°C e <= 26°C é 'Normal'
# - Temperatura > 26°C é 'Alta'
#
# temperatura = 22

# try:
#     temperatura = float(input("Digite o valor da temperatura no sensor em Cº: "))
    
#     if temperatura < 18:
#         print("Temperatura baixa, Avise um técnico!")
#     elif temperatura >= 18 and temperatura <= 26:
#         print("A temperatura está normal.")
#     else:
#         print("A temperatura está alta. Chame um técnico urgente.")

# except ValueError:
#     print("Digite um valor válido!")

# Exercício 3: Filtragem de Logs por Severidade
# Você está analisando logs de uma aplicação e precisa filtrar mensagens com 
# severidade 'ERROR'. Dado um registro de log em formato de dicionário como 
# log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}, 
# escreva um programa que imprima a mensagem se a severidade for 'ERROR'.

# log = {
#     'timestamp': '2021-06-23 10:00:00', 
#     'level': 'ERROR', 
#     'message': 'Falha na conexão'
# }

# try: 
#     #tenta acessar e checar o nível de severidade
#     if log['level'] == 'ERROR':
#         print(log['message'])
# except KeyError:
#     print("Erro: O log fornecido não possui os campos necessários para análise.")


# Exercício 4: Validação de Dados de Entrada
# Antes de processar os dados de usuários em um sistema de recomendação, você 
# precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha 
# fornecido um email válido. Escreva um programa que valide essas condições e 
# imprima "Dados de usuário válidos" ou o erro específico encontrado.
#
# idade = 25
# email = "usuario@exemplo.com"

# try:
#     idade = 18
#     email = "usuario@exemplo.com"

#     dados_validos = True
    
#     # Validando se a idade é negativa
#     if idade < 0:
#         raise ValueError

#     # Validando idade entre 18 e 65
#     elif not (18 <= idade <= 65):
#         print("Erro encontrado: A idade deve estar entre 18 e 65 anos.")
#         dados_validos = False
    
#     # Validação básica de e-mail
#     if '@' not in email or '.' not in email:
#         print('Erro encontrado: O e-mail é invalido!')
#         dados_validos = False
    
#     # Se tudo estiver correto
#     if dados_validos:
#         print('Os dados de usuário são válidos.')
        
# except ValueError:
#     print('Sua idade não pode ser negativa.')

# Exercício 5: Detecção de Anomalias em Dados de Transações
# Você está trabalhando em um sistema de detecção de fraude e precisa identificar 
# transações suspeitas. Uma transação é considerada suspeita se o valor for 
# superior a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou 
# depois das 18h). Dada uma transação como transacao = {'valor': 12000, 'hora': 20}, 
# verifique se ela é suspeita.

# transacao = {'valor': 12000, 'hora': 20}

# try:
#     # Isolamos os valores em variaveis para ficarem mais legiveis.
#     valor = transacao['valor']
#     hora = transacao['hora']
    
#     # Verificando a lógica de transação suspeita
#     if valor > 10000 or (hora < 9 or hora > 18):
#         print("Alerta: Esta transação é suspeita!")
#     else:
#         print("Essa transação é normalizada e segura.")

# except KeyError:
#     print("Erro: O arquivo de transação está incompleto ou com chaves inválidas.")

# ==============================================================================
# EXERCÍCIOS: ESTRUTURAS DE REPETIÇÃO (FOR) & DICIONÁRIOS
# ==============================================================================

# Exercício 6: Contagem de Palavras em Textos
# Objetivo: Dado um texto, contar quantas vezes cada palavra única aparece nele.
#
# texto = "a raposa marrom salta sobre o cachorro preguiçoso"

# #Separando as palavras do texto
# palavras = texto.split()

# #Criando dicionario vazio para receber a contagem
# contagem_palavras = {}

# #Percorrendo as palavras
# for p in palavras:
#     if p in palavras:
#         contagem_palavras[p] =+ 1
#     else:
#         contagem_palavras[p] = 1
# print(contagem_palavras)


# Exercício 7: Normalização de Dados
# Objetivo: Normalizar uma lista de números para que fiquem na escala de 0 a 1.
#
# numeros = [10, 20, 30, 40, 50]

# #Descobrir o maior e menor valor
# minimo = min(numeros)
# maximo = max(numeros)

# #Criando uma lista que vai receber os novos valores normalizados
# numeros_normalizados = []

# #Percorrendo os números e normalizando
# for num in numeros:
#     #Aplicando a formula
#     num_normalizado = (num - minimo) / (maximo - minimo)
#     #Guardando os numeros
#     numeros_normalizados.append(num_normalizado)
    
# print(numeros_normalizados)

# Exercício 8: Filtragem de Dados Faltantes
# Objetivo: Dada uma lista de dicionários representando dados de usuários, 
# filtrar aqueles que têm um campo específico faltando (vazio).

# usuarios = [
#     {"nome": "Alice", "email": "alice@example.com"},
#     {"nome": "Bob", "email": ""},
#     {"nome": "Carol", "email": "carol@example.com"}
# ]

# usuarios_vazios = []

# for user in usuarios:
#     nome = user.get("nome")
#     email = user.get("email")
    
#     novo_usuario = {}
    
#     if not nome or not email:
#         novo_usuario["nome"] = nome
#         novo_usuario["email"] = email
#         usuarios_vazios.append(novo_usuario)
    
# print(usuarios_vazios)

# Exercício 9: Extração de Subconjuntos de Dados
# Objetivo: Dada uma lista de números, extrair apenas aqueles que são pares.
#
# numeros = range(1, 11)
# num_pares = []

# for n in numeros:
#     if n % 2 == 0:
#         num_pares.append(n)

# print(num_pares)

# Exercício 10: Agregação de Dados por Categoria
# Objetivo: Dado um conjunto de registros de vendas, calcular o total de 
# vendas por categoria.
#
# vendas = [
#     {"categoria": "eletrônicos", "valor": 1200},
#     {"categoria": "livros", "valor": 200},
#     {"categoria": "eletrônicos", "valor": 800}
# ]

# # Criando dicionario para armazenar os valors totais
# totais = {}

# for v in vendas:
#     # Pegando os dados atuais
#     categoria = v["categoria"]
#     valor = v["valor"]
    
#     # Lógica para calculo de valor
#     if categoria in totais:
#         totais[categoria] += valor
#     else:
#         totais[categoria] = valor

# print(totais)

# ==============================================================================
# EXERCÍCIOS: ESTRUTURAS DE REPETIÇÃO (WHILE) & TRATAMENTO DE ERROS
# ==============================================================================

# Exercício 11: Leitura de Dados até Flag
# Objetivo: Ler dados de entrada do usuário até que uma palavra-chave 
# específica ("sair") seja fornecida.

while True:
    palavra_chave = input("Digite uma palavra chave: ").strip().lower()
    
    if palavra_chave == "sair":
        print("Parabéns, você fugiu do loop")
        break

# Exercício 12: Validação de Entrada
# Objetivo: Solicitar ao usuário um número dentro de um intervalo específico 
# (entre 1 e 10) repetidamente até que a entrada seja válida.


# Exercício 13: Consumo de API Simulado
# Objetivo: Simular o consumo de uma API paginada, onde cada "página" de dados 
# é processada em loop até que não haja mais páginas.
#
# pagina_atual = 1
# paginas_totais = 5


# Exercício 14: Tentativas de Conexão
# Objetivo: Simular tentativas de reconexão a um serviço com um limite 
# máximo de 5 tentativas. Se falhar em todas, avisar sobre o erro.
#
# tentativas_maximas = 5
# tentativa = 1

# Exercício 15: Processamento de Dados com Condição de Parada
# Objetivo: Processar itens de uma lista um a um até encontrar um valor 
# específico ("parar") que indica a interrupção.
#
# itens = [1, 2, 3, "parar", 4, 5]


# Exercício Bônus: Validação Completa de Formulário com Controle de Fluxo
# Objetivo: Integre um fluxo de `while` com tratamento de exceções (`try-except`) 
# que repita as perguntas de entrada de dados (Nome, Salário e Bônus) até que o 
# usuário insira