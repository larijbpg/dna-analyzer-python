
# 🧬 Analisador de Sequências de DNA & Pipeline de Triagem (GC Content & Metagenômica)

Este repositório contém scripts em Python desenvolvidos para automação de controle de qualidade (QC), análise de sequências genéticas e triagem clínica. O projeto evoluiu da manipulação vetorial básica para pipelines modulares voltadas à bioinformática médica, diagnósticos moleculares e processamento de dados NGS.

---

## 🚀 Evolução & Arquitetura do Projeto

* **Versão Legada (`Analisador_basico.py`):**
  * **Tecnologias:** Python Nativo, NumPy e Pandas.
  * **Foco:** Manipulação básica de sequências tratadas como *strings* e cálculos numéricos vetoriais de métricas biológicas.

* **Pipeline Modular (`pipeline_biopython.py` + `bio_utils.py`):**
  * **Tecnologias:** Biopython (`Bio.Seq`, `Bio.SeqUtils`), Pandas e Módulo Customizado Python.
  * **Foco:** Manipulação de objetos biológicos nativos (`Seq`), cálculo automatizado de teor de GC com limite de corte (*cutoff*) personalizável e exportação de relatórios.

* **Análise de Arquivos FASTA (`estudo_fasta.py`):**
  * **Tecnologias:** Biopython (`SeqIO`), NumPy e Pandas.
  * **Foco:** Leitura em lote de arquivos biológicos `.fasta`, tradução genética de DNA para proteínas (com mapeamento de **códons de parada `*`**), estatística de lote via NumPy e exportação de relatórios em CSV.

* **Pipeline de Triagem Metagenômica & Metadados (`limpeza_dados_brutos.ipynb`):**
  * **Tecnologias:** Pandas, NumPy, RegEx (`re`), Matplotlib, Seaborn.
  * **Foco:** Simulação de pipeline de sequenciamento NGS (shotgun), higienização de sequências com expressões regulares, controle de qualidade (Q-Score/Teor GC), agrupamento estatístico por patógeno (`groupby`) e cruzamento relacional com metadados hospitalares (`pd.merge`). Visualização de dados com Matplotlib e Seaborn (boxplot de Q-Score por patógeno, scatterplot de correlação Teor GC x Q-Score).

---

## 📁 Estrutura de Arquivos

* `estudo_fasta.py`: Script para leitura de arquivos FASTA, tradução proteica, cálculo estatístico e geração de relatórios de QC.
* `bio_utils.py`: Módulo reutilizável com funções para cálculo de teor GC, contagem de bases e classificação de status de aprovação.
* `pipeline_biopython.py`: Script principal da pipeline modular que executa o processamento e gera as tabelas.
* `limpeza_dados_brutos.ipynb`: Script focado em filtragem rigorosa de dados biomédicos, validação por Regex e junção (`merge`) de metadados clínicos de pacientes.
* `Analisador_basico.py`: Script inicial focado em ciência de dados e lógica vetorial (NumPy/Pandas).
* `relatorio_qc_fasta.csv` / `amostras_aprovadas.csv`: Relatórios finais gerados contendo os dados processados na triagem.

---

## 🧠 Conceitos Biológicos e de Bioinformática Aplicados

* **Teor GC (%)**: Parâmetro essencial para o desenho de primers de PCR, estabilidade térmica de fitas e identificação taxonômica.
* **Códons de Parada (`*`)**: Caractere gerado na tradução proteica que representa um *Stop Codon* (ex: TAA, TAG, TGA), indicando o término da síntese da fita pelo ribossomo.
* **Metagenômica & Shotgun Sequencing**: Sequenciamento global da amostra sem primers específicos, permitindo a identificação cega de múltiplos patógenos.
* **Depleção do Hospedeiro (Host Depletion)**: Princípio bioinformático de remoção do DNA humano da amostra via alinhamento computacional contra um genoma de referência universal (ex: GRCh38), isolando o material genético de vírus e bactérias.
* **Phred Quality Score (Q-Score)**: Métrica logarítmica ($Q = -10 \log_{10} P$) que quantifica a probabilidade de erro na chamada de uma base nitrogenada pelo sequenciador NGS.
    * **Interpretação e Faixas de Valor:**
        * **`Q > 30`**: Alta precisão (Acurácia de $99,9\%$, taxa de erro de $1$ em $1.000$). Padrão ouro para diagnósticos e NGS.
        * **`Q < 20`**: Sinal de alerta no lote (Acurácia $< 99\%$). Se ocorrer em toda a corrida, indica degradação de enzimas, amostra degradada ou erro térmico do equipamento.
        * **`Q < 10`**: Biblioteca pobre / Artefatos (Acurácia $< 90\%$). Ocorre em amostras de baixa carga biomédica onde o equipamento lê apenas **dímeros de primers**, gerando leituras curtas e ruidosas.
        * **`Q = NaN`**: Ausência de dado/Sinal indisponível. Decorrente de ruído óptico severo, cluster sobreposto no *flowcell* ou corrupção no arquivo FASTQ/Parsing de dados.
    * **Distinção Biológica vs. Erro de Dados (`NaN` vs. Falha de Amplificação):**
        * *Falha de Amplificação / Baixa Carga (Bancada):* Se a amostra não amplificar na PCR/Preparo de Biblioteca, o resultado no NGS será a **ausência total de leituras** (0 *reads*) ou contagem residual de dímeros, e não um valor `NaN`.
        * *Presença de `NaN` (Dados/Sinal):* Indica falha técnica na leitura do sinal físico pelo equipamento (ex: ruído óptico/cluster sobreposto no *flowcell* que impediu o cálculo da matriz de qualidade) ou erro no parseamento/conversão de arquivos FASTQ corrompidos durante a etapa de software.

---

## 🛠️ Pré-requisitos

Certifique-se de ter instalado as bibliotecas necessárias:

```bash
pip install pandas numpy biopython



