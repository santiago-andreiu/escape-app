import streamlit as st
from cryptography.fernet import Fernet
from PIL import Image
from io import BytesIO
from pathlib import Path


st.set_page_config(
    page_title="Escape",
    page_icon="🔐",
    layout="centered"
)


st.markdown("""
<style>
    .stApp {
        background: radial-gradient(circle at top, #172554 0%, #020617 45%, #020617 100%);
        color: white;
    }

    section.main > div {
        max-width: 760px;
        padding-top: 70px;
    }

    .hero {
        text-align: center;
        margin-bottom: 35px;
    }

    .hero-icon {
        font-size: 70px;
        margin-bottom: 10px;
    }

    .hero-title {
        font-size: 54px;
        font-weight: 900;
        color: white;
        margin-bottom: 8px;
    }

    .hero-subtitle {
        font-size: 18px;
        color: #cbd5e1;
    }

    .info-card {
        background: rgba(15, 23, 42, 0.85);
        border: 1px solid rgba(148, 163, 184, 0.25);
        border-radius: 18px;
        padding: 22px;
        margin-bottom: 25px;
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.35);
    }

    .info-title {
        font-size: 20px;
        font-weight: 700;
        margin-bottom: 8px;
        color: #f8fafc;
    }

    .info-text {
        font-size: 15px;
        color: #cbd5e1;
        line-height: 1.6;
    }

    div.stTextInput > div > div > input {
        border-radius: 12px;
        height: 48px;
    }

    div.stButton > button {
        width: 100%;
        height: 50px;
        border-radius: 14px;
        font-size: 17px;
        font-weight: 700;
        color: white;
        border: none;
        background: linear-gradient(90deg, #2563eb, #7c3aed);
        transition: 0.2s;
    }

    div.stButton > button:hover {
        transform: scale(1.01);
        color: white;
        background: linear-gradient(90deg, #1d4ed8, #6d28d9);
    }

    .footer {
        text-align: center;
        color: #64748b;
        font-size: 13px;
        margin-top: 35px;
    }
</style>
""", unsafe_allow_html=True)


st.markdown("""
<div class="hero">
    <div class="hero-icon">🔐</div>
    <div class="hero-title">Escape</div>
    <div class="hero-subtitle">Sistema de desbloqueio de imagem criptografada</div>
</div>
""", unsafe_allow_html=True)


st.markdown("""
<div class="info-card">
    <div class="info-title">Área protegida</div>
    <div class="info-text">
        Digite a senha correta para liberar o acesso à imagem criptografada.
        Caso a senha esteja incorreta, o conteúdo continuará bloqueado.
    </div>
</div>
""", unsafe_allow_html=True)


senha_correta = st.secrets.get("SENHA_APP", "478593")

senha = st.text_input(
    "Senha:",
    type="password",
    placeholder="Digite a senha de acesso"
)

if st.button("Desbloquear imagem"):
    if senha == senha_correta:
        st.success("Acesso liberado com sucesso!")

        try:
            pasta = Path(__file__).parent

            caminho_chave = pasta / "chave.key"
            caminho_foto = pasta / "foto.enc"

            chave = caminho_chave.read_bytes()
            dados_criptografados = caminho_foto.read_bytes()

            fernet = Fernet(chave)
            dados_descriptografados = fernet.decrypt(dados_criptografados)

            imagem = Image.open(BytesIO(dados_descriptografados))

            st.image(
                imagem,
                caption="Imagem desbloqueada",
                use_container_width=True
            )

        except FileNotFoundError:
            st.error("Erro: os arquivos chave.key ou foto.enc não foram encontrados.")

        except Exception as erro:
            st.error("Erro ao desbloquear a imagem.")
            st.write(erro)

    else:
        st.error("Senha incorreta. Tente novamente.")


st.markdown("""
<div class="footer">
    Projeto desenvolvido em Python com Streamlit
</div>
""", unsafe_allow_html=True)
