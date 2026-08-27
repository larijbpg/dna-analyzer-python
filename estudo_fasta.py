import numpy as np
import pandas as pd
from Bio import SeqIO
from Bio.SeqUtils import gc_fraction

# Passo 1: crio listas vazias para guardar as informações das sequencias
ids = []
tamanhos = []
teores_gc = []
proteinas = []

# Passo 2: ler o arquivo fasta e extrair as informações

for registro in SeqIO.parse("dna_amostra.fasta", "fasta"): # pegar um arquivo no formato fasta chamado "dna_amostra.fasta" e abrir e ler. Para cada registro nesse arquivo:
    ids.append(registro.id) #pegar o id de cada registro e adicionar na lista ids
    tamanhos.append(len(registro.seq)) # vou pegar o comprimento total (qtde de bases) da sequencia de cada registro e adicionar na lista tamanhos
    teores_gc.append(round(gc_fraction(registro.seq) * 100, 2)) 
    # quero a quantidade de gc da seq no registro, transformar em porcentagem (*100) e arredondar 2 casas decimais (round() .., 2) e adicionar na lista de teores_gc

    proteinas.append(str(registro.seq.translate()))
    # traduzindo o DNA em proteina e adicionando na lista de proteinas
    # ou seja, traduz a seq do registro e adiciona como string na lista de proteinas

array_gc = np.array(teores_gc) # transformo a lista de teores_gc em um array do numpy para conseguir fazer calculos matematicos com alta performance
media_gc = np.mean(array_gc) # calculo a media aritmetica de todos os valores de teor GC contidos no array_gc
desvio_padrao = np.std(array_gc) # calculo o desvio padrao dos teores de GC para ver a variacao/dispersao dos dados em relacao a media

print(f"Média do Teor GC do lote: {media_gc:.2f}%")
print(f"Desvio Padrão: {desvio_padrao:.2f}")

# Passo 3: criar a planilha do relátorio final
# DataFrame = df
df = pd.DataFrame({
    "ID_Amostra": ids,
    "Tamanho_bp": tamanhos,
    "Teor_GC_%": teores_gc,
    "Sequencia_Proteica": proteinas
})

# Passo 4: numpy ajudando a classificar com base na média
df["Status_QC"] = np.where(df["Teor_GC_%"] >= media_gc, "Aprovado", "Reprovado")

print("\nRelatório Final Gerado:")
print(df)

# Passo 5: exportando o relatório para .csv
df.to_csv("relatorio_qc_fasta.csv", index=False)
print("\nArquivo 'relatorio_qc_fasta.csv' gerado com sucesso!")