import random

taxa_aprendizado = 0.01

dados_treino = [
    {"x1": -0.6508, "x2": 0.1097, "x3": 4.0009, "d": -1.0000},
    {"x1": -1.4492, "x2": 0.8896, "x3": 4.4005, "d": -1.0000},
    {"x1": 2.0850,  "x2": 0.6876, "x3": 12.0710, "d": -1.0000},
    {"x1": 0.2626,  "x2": 1.1476, "x3": 7.7985, "d": 1.0000},
    {"x1": 0.6418,  "x2": 1.0234, "x3": 7.0427, "d": 1.0000},
    {"x1": 0.2569,  "x2": 0.6730, "x3": 8.3265, "d": -1.0000},
    {"x1": 1.1155,  "x2": 0.6043, "x3": 7.4446, "d": 1.0000},
    {"x1": 0.0914,  "x2": 0.3399, "x3": 7.0677, "d": -1.0000},
    {"x1": 0.0121,  "x2": 0.5256, "x3": 4.6316, "d": 1.0000},
    {"x1": -0.0429, "x2": 0.4660, "x3": 5.4323, "d": 1.0000},
    {"x1": 0.4340,  "x2": 0.6870, "x3": 8.2287, "d": -1.0000},
    {"x1": 0.2735,  "x2": 1.0287, "x3": 7.1934, "d": 1.0000},
    {"x1": 0.4839,  "x2": 0.4851, "x3": 7.4850, "d": -1.0000},
    {"x1": 0.4089,  "x2": -0.1267, "x3": 5.5019, "d": -1.0000},
    {"x1": 1.4391,  "x2": 0.1614, "x3": 8.5843, "d": -1.0000},
    {"x1": -0.9115, "x2": -0.1973, "x3": 2.1962, "d": -1.0000},
    {"x1": 0.3654,  "x2": 1.0475, "x3": 7.4858, "d": 1.0000},
    {"x1": 0.2144,  "x2": 0.7515, "x3": 7.1699, "d": 1.0000},
    {"x1": 0.2013,  "x2": 1.0014, "x3": 6.5489, "d": 1.0000},
    {"x1": 0.6483,  "x2": 0.2183, "x3": 5.8991, "d": 1.0000},
    {"x1": -0.1147, "x2": 0.2242, "x3": 7.2435, "d": -1.0000},
    {"x1": -0.7970, "x2": 0.8795, "x3": 3.8762, "d": 1.0000},
    {"x1": -1.0625, "x2": 0.6366, "x3": 2.4707, "d": 1.0000},
    {"x1": 0.5307,  "x2": 0.1285, "x3": 5.6883, "d": 1.0000},
    {"x1": -1.2200, "x2": 0.7777, "x3": 1.7252, "d": 1.0000},
    {"x1": 0.3957,  "x2": 0.1076, "x3": 5.6623, "d": -1.0000},
    {"x1": -0.1013, "x2": 0.5989, "x3": 7.1812, "d": -1.0000},
    {"x1": 2.4482,  "x2": 0.9455, "x3": 11.2095, "d": 1.0000},
    {"x1": 2.0149,  "x2": 0.6192, "x3": 10.9263, "d": -1.0000},
    {"x1": 0.2012,  "x2": 0.2611, "x3": 5.4631, "d": 1.0000}
]

amostras_teste = [
    {"id": 1,  "x1": -0.3665, "x2": 0.0620,  "x3": 5.9891},
    {"id": 2,  "x1": -0.7842, "x2": 1.1267,  "x3": 5.5912},
    {"id": 3,  "x1": 0.3012,  "x2": 0.5611,  "x3": 5.8234},
    {"id": 4,  "x1": 0.7757,  "x2": 1.0648,  "x3": 8.0677},
    {"id": 5,  "x1": 0.1570,  "x2": 0.8028,  "x3": 6.3040},
    {"id": 6,  "x1": -0.7014, "x2": 1.0316,  "x3": 3.6005},
    {"id": 7,  "x1": 0.3748,  "x2": 0.1536,  "x3": 6.1537},
    {"id": 8,  "x1": -0.6920, "x2": 0.9404,  "x3": 4.4058},
    {"id": 9,  "x1": -1.3970, "x2": 0.7141,  "x3": 4.9263},
    {"id": 10, "x1": -1.8842, "x2": -0.2805, "x3": 1.2548}
]

todos_os_pesos_finais = []

for rodada in range(1, 6):
    pesos = {
        'w1': random.uniform(0, 1),
        'w2': random.uniform(0, 1),
        'w3': random.uniform(0, 1),
        'w_limiar': random.uniform(0, 1)
    }
    
    pesos_iniciais = pesos.copy()
    epoca_atual = 0

    while True:
        epoca_atual += 1
        erros_epoca = 0

        for entradas in dados_treino:
            soma_produtos = (entradas['x1'] * pesos['w1']) + (entradas['x2'] * pesos['w2']) + (entradas['x3'] * pesos['w3']) + (-1 * pesos['w_limiar'])

            if soma_produtos >= 0:
                sinal_saida = 1
            else:
                sinal_saida = -1

            if sinal_saida != entradas['d']:
                erros_epoca += 1
                erro = entradas['d'] - sinal_saida
                pesos['w1'] = pesos['w1'] + (taxa_aprendizado * erro * entradas['x1'])
                pesos['w2'] = pesos['w2'] + (taxa_aprendizado * erro * entradas['x2'])
                pesos['w3'] = pesos['w3'] + (taxa_aprendizado * erro * entradas['x3'])
                pesos['w_limiar'] = pesos['w_limiar'] + (taxa_aprendizado * erro * -1)

        if erros_epoca == 0:
            break

    todos_os_pesos_finais.append(pesos.copy())

    print("\n" + "="*115)
    print(f"{f'RESULTADO DO TREINAMENTO ATUAL - RODADA T{rodada}':^115}")
    print("="*115)
    print(f"{'Vetor de pesos iniciais':^39} | {'Vetor de pesos finais':^39} | {'Número de':<11}")
    print(f"{'w_limiar':^8} {'w1':^8} {'w2':^8} {'w3':^8} | {'w0':^8} {'w1':^8} {'w2':^8} {'w3':^8} | {'épocas':<11}")
    print("-"*115)
    print(f"{pesos_iniciais['w_limiar']:8.4f} {pesos_iniciais['w1']:8.4f} {pesos_iniciais['w2']:8.4f} {pesos_iniciais['w3']:8.4f} | "
          f"{pesos['w_limiar']:8.4f} {pesos['w1']:8.4f} {pesos['w2']:8.4f} {pesos['w3']:8.4f} | "
          f"{epoca_atual:<11}")
    print("="*115)

    if rodada < 5:
        input(f"\nPressione ENTER para iniciar a rodada de treinamento T{rodada+1}...")
    else:
        print("\nFim das rodadas de treinamento!")
        input("\nExecutar o teste oficial com as 10 amostras...")

print("\n" + "=" * 85)
print(f"{'TABELA DE CLASSIFICAÇÃO AUTOMÁTICA DAS AMOSTRAS':^85}")
print("=" * 85)
print(f"{'Amostra':^9} | {'X1':^9} | {'X2':^9} | {'X3':^9} | {'y(T1)':^6} | {'y(T2)':^6} | {'y(T3)':^6} | {'y(T4)':^6} | {'y(T5)':^6}")
print("-" * 85)

for amostra in amostras_teste:
    respostas_rodadas = []
    
    for pesos_treinados in todos_os_pesos_finais:
        soma_produtos = (amostra['x1'] * pesos_treinados['w1']) + \
                        (amostra['x2'] * pesos_treinados['w2']) + \
                        (amostra['x3'] * pesos_treinados['w3']) + \
                        (-1 * pesos_treinados['w_limiar'])
        
        if soma_produtos >= 0:
            y = 1
        else:
            y = -1
        respostas_rodadas.append(y)
    
    print(f"{amostra['id']:^9} | "
          f"{amostra['x1']:9.4f} | "
          f"{amostra['x2']:9.4f} | "
          f"{amostra['x3']:9.4f} | "
          f"{respostas_rodadas[0]:^6} | "
          f"{respostas_rodadas[1]:^6} | "
          f"{respostas_rodadas[2]:^6} | "
          f"{respostas_rodadas[3]:^6} | "
          f"{respostas_rodadas[4]:^6}")

print("=" * 85)