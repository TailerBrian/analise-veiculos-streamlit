# 🚗 Análise de Anúncios de Veículos - Web App Interativa

https://project-sprint-5-5j6o.onrender.com/

Este projeto consiste no desenvolvimento de uma aplicação web interativa para a análise exploratória de dados (EDA) de anúncios de veículos, simulando um cenário real de análise de mercado.

## 🛠️ Tecnologias e Ferramentas
* **Linguagem:** Python
* **Interface Web:** Streamlit
* **Processamento de Dados:** Pandas
* **Visualização Interativa:** Plotly Express
* **Alojamento:** Render

## ⚙️ Funcionalidades da Aplicação
* **Visualização de Dados:** Exibição do conjunto de dados estruturado (`vehicles.csv`).
* **Análise de Quilometragem:** Gráfico interativo (Histograma) dinâmico acionado pelo utilizador.
* **Análise de Preços:** Gráfico de dispersão (Preço vs. Quilometragem) para identificar correlações de mercado.
* **Filtros Dinâmicos:** Caixas de seleção inteligentes (`st.checkbox`) para customizar a visualização.

## 📊 Insights Práticos do Projeto
* **Depreciação Visual:** É possível identificar de forma clara como o preço dos veículos decresce de forma acentuada e previsível à medida que a quilometragem (`odometer`) aumenta.
* **Dispersão de Outliers:** A análise visual permitiu isolar valores discrepantes de veículos antigos com preços anormalmente altos (potenciais carros clássicos ou erros de inserção de dados).

## 🚀 Como Executar Localmente
1. Clonar este repositório.
2. Criar e ativar o ambiente virtual:
   ```bash
   python -m venv vehicles_env
   # No Windows (Terminal):
   vehicles_env\Scripts\activate
   ```
3. Instalar as dependências necessárias:
   ```bash
   pip install -r requisitos.txt
   ```
4. Executar a aplicação:
   ```bash
   streamlit run app.py
   ```
