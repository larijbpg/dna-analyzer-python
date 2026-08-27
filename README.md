
# 🧬 Analisador de Sequências de DNA & Pipeline de Triagem (GC Content)

Este repositório contém scripts em Python desenvolvidos para automação de controle de qualidade (QC) e análise de sequências genéticas. O projeto evoluiu de uma análise vetorial básica para uma pipeline modular reutilizável voltada à bioinformática médica e diagnóstica.

---

## 🚀 Evolução & Arquitetura do Projeto

* **Versão Legada (`Analisador_basico.py`):**
  - **Tecnologias:** Python Nativo, NumPy e Pandas.
  - **Foco:** Manipulação básica de sequências tratadas como *strings* e cálculos numéricos vetoriais de métricas biológicas.

* **Versão Atual / Pipeline Modular (`pipeline_biopython.py` + `bio_utils.py`):**
  - **Tecnologias:** Biopython (`Bio.Seq`, `Bio.SeqUtils`), Pandas e Módulo Customizado Python.
  - **Foco:** Manipulação de objetos biológicos nativos (`Seq`), cálculo automatizado de teor de GC com limite de corte (*cutoff*) personalizável e exportação de relatórios para triagem laboratorial.

---

## 📂 Estrutura de Arquivos

* `bio_utils.py`: Módulo reutilizável com funções para cálculo de teor GC, contagem de bases e classificação de status de aprovação.
* `pipeline_biopython.py`: Script principal da pipeline modular que executa o processamento e gera as tabelas.
* `Analisador_basico.py`: Script inicial focado em ciência de dados e lógica vetorial (NumPy/Pandas).
* `amostras_aprovadas.csv`: Relatório final gerado contendo apenas as amostras aprovadas na triagem.

---

## 📋 Pré-requisitos

Certifique-se de ter instalado as bibliotecas necessárias:

```bash
pip install biopython pandas numpy




