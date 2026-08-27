import pandas as pd
import numpy as np
from Bio.Seq import Seq
from Bio.SeqUtils import gc_fraction

def porcentagem_gc(dna_seq):
    """Calcula o teor de GC (%) arredondado para 2 casas decimais"""
    return round(gc_fraction(dna_seq) * 100, 2)

def classificar_status(teor_gc, corte=50.0):
    """
    Retorna 'Aprovado' se o teor de GC for >= limite de corte, senão 'Reprovado'.
    Muito usado para questões de Controle de Qualidade da sequencia: 
        desenho de primers(para uma Tm equilibrada = 40% a 60% de %GC), 
        triagem para sequenciamento(NGS) => Viés de GC (GC bias)  
        checagem de Integridade de Montagem => Indicação de contaminação
        """
    return "Aprovado" if teor_gc >= corte else "Reprovado"

def processar_amostras(lista_dnas, corte = 50.0):
    """Processa uma lista de sequências e retorna um DataFrame estruturado"""
    dados = []
    for i, dna in enumerate(lista_dnas):
        qtde_a = dna.count("A")
        qtde_t = dna.count("T")
        qtde_c = dna.count("C")
        qtde_g = dna.count("G")

        gc = porcentagem_gc(dna)
        status = classificar_status(gc, corte = corte)

        dados.append({
            "Amostra": f"Amostra_{i+1}",
            "DNA": str(dna),
            "Qtde_A": qtde_a,
            "Qtde_T": qtde_t,
            "Qtde_C": qtde_c,
            "Qtde_G": qtde_g,
            "Teor_GC_%": gc,
            "Corte": corte,
            "Status": status
        })
    return pd.DataFrame(dados)

        