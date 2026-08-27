
# 🧬 Analisador de Sequências de DNA & Pipeline de Triagem (GC Content)

Este repositório contém scripts em Python desenvolvidos para automação de controle de qualidade (QC) e análise de sequências genéticas. O projeto evoluiu da manipulação vetorial básica para pipelines modulares voltadas à bioinformática médica, diagnósticos e triagem laboratorial.

---

## 🧬 Evolução & Arquitetura do Projeto

* **Versão Legada (`Analisador_basico.py`):**
  * **Tecnologias:** Python Nativo, NumPy e Pandas.
  * **Foco:** Manipulação básica de sequências tratadas como *strings* e cálculos numéricos vetoriais de métricas biológicas.

* **Pipeline Modular (`pipeline_biopython.py` + `bio_utils.py`):**
  * **Tecnologias:** Biopython (`Bio.Seq`, `Bio.SeqUtils`), Pandas e Módulo Customizado Python.
  * **Foco:** Manipulação de objetos biológicos nativos (`Seq`), cálculo automatizado de teor de GC com limite de corte (*cutoff*) personalizável e exportação de relatórios.

* **Análise de Arquivos FASTA (`estudo_fasta.py`):**
  * **Tecnologias:** Biopython (`SeqIO`), NumPy e Pandas.
  * **Foco:** Leitura em lote de arquivos biológicos `.fasta`, tradução genética de DNA para proteínas (com mapeamento de **códons de parada `*`**), estatística de lote via NumPy e exportação de relatórios em CSV.

---

## 📁 Estrutura de Arquivos

* `estudo_fasta.py`: Script para leitura de arquivos FASTA, tradução proteica, cálculo estatístico e geração de relatórios de QC.
* `bio_utils.py`: Módulo reutilizável com funções para cálculo de teor GC, contagem de bases e classificação de status de aprovação.
* `pipeline_biopython.py`: Script principal da pipeline modular que executa o processamento e gera as tabelas.
* `Analisador_basico.py`: Script inicial focado em ciência de dados e lógica vetorial (NumPy/Pandas).
* `relatorio_qc_fasta.csv` / `amostras_aprovadas.csv`: Relatórios finais gerados contendo os dados processados na triagem.

---

## 🧠 Conceitos Biológicos Aplicados

* **Teor GC (%)**: Parâmetro essencial para o desenho de primers de PCR e identificação taxonômica.
* **Códons de Parada (`*`)**: Caractere gerado na tradução proteica que representa um *Stop Codon* (ex: TAA, TAG, TGA), indicando o término da síntese da fita pelo ribossomo.

---

## 📋 Pré-requisitos

Certifique-se de ter instalado as bibliotecas necessárias:

```bash
pip install biopython pandas numpy




