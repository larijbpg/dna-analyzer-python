from Bio.Seq import Seq
from bio_utils import *

#Primeiro vou passar as sequencias de DNA que vou analisar
lista_dnas = [
    Seq("ATGCGATCGATCGAT"),
    Seq("ATGGCCATTGTAACG"),
    Seq("ATGCTAGCTAGCAAT"),
    Seq("ATGCGGCGGCCGTTT")
]

# Executar as funções 

df_resultado = processar_amostras(lista_dnas) 
# chama a função passando a lista de seq como parametro. Ela faz todas as contagens de A,T,C,G e Status e retorna o resultado em formato de tabela na variavel df_resultado
df_aprovados = df_resultado[df_resultado["Status"] == "Aprovado"]
# aplica um filtro condicional na tabela df_resultado. Olha a coluna status e seleciona apenas os aprovados e guarda essa nova tabela filtrada na variavel df_aprovados
df_aprovados.to_csv("amostras_aprovadas.csv", index=False)
# pega o df filtrado e exporta pra um arquivo fisico no computador. O parametro index=false garante que a coluna de numeração automatica(índice) do Pandas nao seja salva junto
print(df_aprovados)
