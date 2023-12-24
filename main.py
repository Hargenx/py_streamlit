from pathlib import Path
import json
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_extras.let_it_rain import rain

THIS_DIR = Path(__file__).parent
CSS_FILE = THIS_DIR / "style" / "style.css"
ASSETS = THIS_DIR / "assets"
LOTTIE_ANIMATION = ASSETS / "animation_natal.json"

def carregar_lottie_animation(file_path):
    with open(file_path, "r") as f:
        return json.load(f)

def animacao_queda():
    rain(emoji="❄️", font_size=20, falling_speed=5, animation_length="infinite")

def solicitar_nome():
    nome_container = st.empty()
    nome = nome_container.text_input("*Por favor, digite seu nome:*", key="nome_input")
    if nome:
        st.experimental_set_query_params(name=nome)
        nome_container.empty()
        return nome
    return "amigo"  # Valor padrão se nenhum nome for inserido

def main():
    st.set_page_config(page_title="Feliz natal!", page_icon="🎄")

    nome = solicitar_nome()
    st.header(f"Feliz Natal, {nome}! 🎄", anchor=False)

    if nome != "amigo":
        st.markdown("---")

        animacao_queda()
        with open(CSS_FILE) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

        lottie_animation = carregar_lottie_animation(LOTTIE_ANIMATION)
        st_lottie(lottie_animation, key="lottie-holiday", height=300)

        st.markdown(f":hibiscus: {nome}:balloon:, um Feliz Natal e um excelente Ano Novo! :snowflake: :star2:")

if __name__ == "__main__":
    main()
