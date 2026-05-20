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
 <img width="1142" height="517" alt="image" src="https://github.com/user-attachments/assets/c227fd4b-6835-45c1-ac7a-15f16bd86a2b" />
 
* **Análise de Quilometragem:** Gráfico interativo (Histograma) dinâmico acionado pelo utilizador.
 <img width="759" height="408" alt="image" src="https://github.com/user-attachments/assets/bdaab1a6-02f7-47b6-b1ce-257ffaac9fb4" />
 
* **Análise de Preços:** Gráfico de dispersão (Preço vs. Quilometragem) para identificar correlações de mercado.
 <img width="773" height="416" alt="image" src="https://github.com/user-attachments/assets/cbbc5f94-11f6-4a42-ad0d-55ab8423316b" />
 
* **Filtros Dinâmicos:** Caixas de seleção inteligentes (`st.checkbox`) para customizar a visualização.
 <img width="669" height="549" alt="image" src="https://github.com/user-attachments/assets/b795cb4c-40b1-48b1-8c1d-62a2e16eae6b" />
 

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
