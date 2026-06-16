import streamlit as st
from cryptography.fernet import Fernet
from PIL import Image
from io import BytesIO
from pathlib import Path


st.set_page_config(page_title="Escape", page_icon="🔐")

st.title("🔐 Escape")
st.write("Digite a senha para desbloquear a imagem.")

senha_correta = "1234"

senha = st.text_input("Senha:", type="password")

if st.button("Entrar"):
    if senha == senha_correta:
        st.success("Senha correta!")

        pasta = Path(__file__).parent

        caminho_chave = pasta / "chave.key"
        caminho_foto = pasta / "foto.enc"

        chave = caminho_chave.read_bytes()
        dados_criptografados = caminho_foto.read_bytes()

        fernet = Fernet(chave)
        dados_descriptografados = fernet.decrypt(dados_criptografados)

        imagem = Image.open(BytesIO(dados_descriptografados))

        st.image(imagem, caption="Imagem desbloqueada")

    else:
        st.error("Senha incorreta. Tente novamente.")