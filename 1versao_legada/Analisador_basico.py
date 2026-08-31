"""
Quero criar um código que analisa uma sequencia de DNA e me passe as seguintes informações:
- quantas base nitrogenadas tem a sequencia
- quantidade de GC
- Primeira trinca de nucleotídeos
- mostre sequencias repetidas que eu quero 
- crie uma sequencia complementar 
- Tm: Temperatura de Melting
        Par A-T valem 2ºC no total para a Tm (Possui 2 pontes de H)
        Par G-C valem 4ºC no total para a Tm (Possui 3 pontes de H)
"""
# Tamanho da sequencia: =============================================================================================================

dna = 'ATGCGTACCTGAACTGGTACGATCGTACG'
bn = len(dna)
print(f'A sequencia de DNA possui {bn} bases nitrogenadas')

# Quantidade de nucleotídeos GC ======================================================================================================

g = dna.count('G')
c = dna.count('C')
cg = c + g
print(f'A sequencia possui ao todo {cg} CG, sendo {g} Guaninas e {c} Citosinas')

# Calculo de CG em relação a fita total
pct_cg = cg/ len(dna) * 100
print(f'A sequencia de DNA possui {pct_cg:.2f}% de GC')

# Qual é a primeira trinca de nucleotídeos: ============================================================================================================
primeiro_codon = dna[0:3]
print(f'A primeira trinca da sequencia de DNA é: {primeiro_codon}')

# Sequencia repetida: ================================================================================================================
repeticao = dna.count('AT')
print(f'A sequencia AT aparece {repeticao} vezes na sequencia de DNA')

# Sequencia complementar: ==============================================================================================================

# A sequencia complementar será a mudança de A <-> T e de C <-> G

    # complementar = ''
    # for base in dna:
    #     if base == 'A':
    #         complementar += 'T' # += vai juntando as letras
    #     elif base == 'T':
    #         complementar += 'A'
    #     elif base == 'C':
    #         complementar += 'G'
    #     elif base == 'G':
    #         complementar += 'C'
    # print(complementar)

#======================================== FUNÇÃO PRONTA ====================================================================================

# 1. Criamos a regra de mapeamento
regra = str.maketrans("ATCG", "TAGC")
# Acesse a função interna da classe de textos (str) para criar uma regra de tradução"
# str.maketrans("DE_QUEM", "PARA_QUEM")

# 2. Aplicamos a regra na fita de DNA
fita_complementar = dna.translate(regra) # uso o translate para aplicar a regra

print(f"Original:     {dna}")
print(f"Complementar: {fita_complementar}")

# Não é recomendado usar .replace() em uma linha para fazer a complementaridade do DNA porque as substituições acontecem em sequência. 
# Assim, quando eu troco A por T, os T que já existiam e os T que foram criados também podem ser trocados por A, alterando o resultado.

# ============================================================================================================================================
# Quero calcular a Tm dessa sequencia:
    # Tm: Temperatura de Melting -> temperatura em que 50% da dupla fita de DNA está em fita simples 
    # Vale ressaltar que a Tm está diretmente ligada a %GC, quanto maior a %, maior a Tm necessária. 
    # Além disso, para sequencias curtas(oligonucleotideos), usamos a Regra de Wallace:
        # Tm = (2 * (A + T)) + (4 * (C + G))

a = dna.count('A')
t = dna.count('T')
c = dna.count('C')
g = dna.count('G')

Tm = (2 * (a + t)) + (4 * (c + g))
print(f'A Tm da sequencia é {Tm}ºC')

# Ou seja, eu preciso de uma temperatura de 88ºC para conseguir separar 50% da fita dupla

# =============================================================================================================================================

# Alerta biológico baseado no tamanho da fita:
tamanho_fita = len(dna)

if tamanho_fita > 20:
    print("Aviso: Para sequências com mais de 20 bases, a Regra de Wallace pode superestimar a Tm.")
        # Sabe-se que Tm altas(acima de 70ºC pode influenciar no funcionamento da reação, pois exige Ta alta. 
        # Teria usar outras ferramentas para ajustar esses parametros)
else:
    print(f"Temperatura de Anelamento (Ta) sugerida para PCR: {Tm - 5}°C")
    # Em reações de PCR é importante saber a Temperatura de Anelamento (Ta), que seria a temperatura em que os primers se anelam a fita
    # A Ta precisa ser alta o bastante para garantir a especificidade (evitando ligações inespecíficas e dímeros), 
    # mas baixa o suficiente em relação à Tm para permitir que os primers se anelem com eficiência.
