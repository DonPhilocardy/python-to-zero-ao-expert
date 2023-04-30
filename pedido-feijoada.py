print('*' * 50)

continuar = True
# Teste de condição
while continuar:
    # Entrada de Dados
    # Quantidade de feijoada
    quantidadeFeijoada = float(input('\nDigite a quantidade de feijoada (300ml a 5000ml): ').replace(',', '.'))
    # Comparação da quantidade de feijoada
    if quantidadeFeijoada < 300:
        print('ERRO: QUANTIDADE INVÁLIDA!')
        continue
    elif quantidadeFeijoada > 5000:
        print('ERRO: QUANTIDADE INVÁLIDA!')
        continue
    break

# declaração de variáveis
# Cálculo do preço
precoFeijoadaN = (quantidadeFeijoada * 5) / 100
precoFeijoadaG = (quantidadeFeijoada * 6) / 100
precoFeijoadaC = (quantidadeFeijoada * 6.5) / 100

print('*' * 50)

# Mostra na Tela
# Tipo de feijoada e o preço
print('\n- Normal (feijão + paio) = R$', precoFeijoadaN,
      '\n- Gourmet (feijão + paio + costelinha) = R$', precoFeijoadaG,
      '\n- Completa (feijão + paio + costelinha + Bacon + Pé + Orelha) = R$', precoFeijoadaC)

continuar2 = True
# declaração de variáveis
# Tipo de feijoada e o preço
n = 'N'
g = 'G'
c = 'C'

while continuar2:
    # Entrada de Dados
    # Tipo de feijoada
    tipoFeijoada = input('\n- N para Normal \n- G para Gourmet \n- C para Completa' +
                         '\n Informe o tipo de feijoada: ').upper().strip()
    if tipoFeijoada not in [n, g, c]:
        print('ERRO: TIPO INVÁLIDO!')
        continue
    break

# Armazenar
# Tipo de feijoada numa variável
if tipoFeijoada == n:
    classe1 = 'Normal'
    precoFeijoada = precoFeijoadaN
elif tipoFeijoada == g:
    classe1 = 'Gourmet'
    precoFeijoada = precoFeijoadaG
elif tipoFeijoada == c:
    classe1 = 'Completa'
    precoFeijoada = precoFeijoadaC

print('*' * 50)

# Mostra na Tela
# Tipo de Acompanhamento e o preço
print('\n- Farinha = R$ 2,00' + '\n- Laranja = R$ 1,00' + '\n- Banana = R$ 1,00' +
      '\n- Couve refogada com bacon = R$ 3,00')

continuar3 = True
# declaração de variáveis
# Tipo de Acompanhamento
f = 'F'
la = 'L'
b = 'B'
c = 'C'
n = '0'
# declaração de variáveis
# preço de Acompanhamento
precoF = 0
precoB = 0
precoL = 0
precoC = 0
# declaração de variáveis
# Contador de Acompanhamento
contF = 0
contL = 0
contB = 0
contC = 0

while continuar3 != n:
    # Entrada de Dados
    # ipo de Acompanhamento
    acompanhamento = input('\n- F para Farinha \n- L para Laranja \n- B para Banana' +
                           '\n- C para Couve refogada com bacon' + '\n- 0 para Não'
                           '\nInforme o tipo de acompanhamento: ').upper().strip()
    if acompanhamento not in [f, la, b, c, n]:
        print('ERRO: ACOMPANHAMENTO INVÁLIDO!')
    elif acompanhamento == f:
        print('\nAdicionado acompanhamento “Farinha”')
        # Incrementar o preço de farina em 2
        precoF = precoF + 2
        # Incrementar o contador de farina em 1
        contF += 1
    elif acompanhamento == la:
        print('\nAdicionado acompanhamento “Laranja”')
        # Incrementar o preço de laranja em 1
        precoL = precoL + 1
        # Incrementar o contador de laranja em 1
        contL = contL + 1
    elif acompanhamento == b:
        print('\nAdicionado acompanhamento “Banana”')
        # Incrementar o preço de banana em 1
        precoB = precoB + 1
        # Incrementar o contador de banana em 1
        contB = contB + 1
    elif acompanhamento == c:
        print('\nAdicionado acompanhamento “Couve refogada com bacon”')
        # Incrementar o preço de couve em 3
        precoC = precoC + 3
        # Incrementar o contador de Couve em 1
        contC = contC + 1
    elif acompanhamento == n:
        break
    continue
# declaração de variáveis
# Tipo de Acompanhamento com String vazio
Farina = ''
Banana = ''
Laranja = ''
Couve = ''
# Adicionar String
# Dentro Variáveis de Acompanhamento com String vazio
if contF > 0:
    Farina = '+ Farina'
if contL > 0:
    Laranja = '+ Laranja'
if contB > 0:
    Banana = '+ Banana'
if contC > 0:
    Couve = '+ Couve refogada com bacon'

print('*' * 50)

# Cálculo o preço Total
PrecoFinal = precoFeijoada + precoF + precoB + precoL + precoC

# Mostrar o preço Final
print('Pedido de feijoada:', quantidadeFeijoada,
      'ml de', classe1, Farina, Laranja, Banana, Couve, '= R$', PrecoFinal)
