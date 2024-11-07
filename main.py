import streamlit as st
from scholarly import scholarly
import time

def buscar_dados_google_academico(nome_pesquisador):
    try:
        # Busca o perfil do pesquisador pelo nome
        search_query = scholarly.search_author(nome_pesquisador)
        autor = next(search_query)  # Pega o primeiro resultado

        # Carrega o perfil completo do autor
        autor = scholarly.fill(autor)

        # Coleta as informações desejadas
        citacoes = autor.get("citedby", "Informação não disponível")
        indice_h = autor.get("hindex", "Informação não disponível")
        indice_i10 = autor.get("i10index", "Informação não disponível")
        
        return citacoes, indice_h, indice_i10
    except StopIteration:
        return "Perfil não encontrado no Google Acadêmico.", "-", "-"
    except Exception as e:
        return f"Erro ao buscar dados: {e}", "-", "-"

# Interface Streamlit
st.title("Busca de Dados no Google Acadêmico")

# Entrada de múltiplos nomes de pesquisadores separados por vírgulas
nomes_pesquisadores = st.text_input("Digite os nomes dos pesquisadores no Google Acadêmico, separados por vírgulas:")

if st.button("Buscar"):
    if nomes_pesquisadores:
        with st.spinner("Buscando..."):
            # Divide a lista de nomes e remove espaços extras
            nomes_lista = [nome.strip() for nome in nomes_pesquisadores.split(",")]
            for nome in nomes_lista:
                st.subheader(f"Dados para: {nome}")
                citacoes, indice_h, indice_i10 = buscar_dados_google_academico(nome)
                st.write(f"Citações: {citacoes}")
                st.write(f"Índice h: {indice_h}")
                st.write(f"Índice i10: {indice_i10}")
                # Adiciona um intervalo de 2 segundos entre as buscas
                time.sleep(2)
    else:
        st.warning("Por favor, insira pelo menos um nome de pesquisador.")
