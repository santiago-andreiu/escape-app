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
        background: linear-gradient(135deg, #0f172a 0%, #020617 100%);
        color: white;
    }

    .main-card {
        background: rgba(255, 255, 255, 0.08);
        padding: 35px;
        border-radius: 22px;
        border: 1px solid rgba(255, 255, 255, 0.15);
        box-shadow: 0 0 35px rgba(0, 0, 0, 0.35);
        margin-top: 40px;
    }

    .title {
        font-size: 48px;
        font-weight: 800;
        margin-bottom: 5px;
    }

    .subtitle {
        font-size: 18px;
        color: #cbd5e1;
        margin-bottom: 25px;
    }

    .info-box {
        background: rgba(59, 130, 246, 0.12);
        border-left: 4px solid #3b82f6;
        padding: 14px;
        border-radius: 10px;
        margin-bottom: 25px;
        color: #dbeafe;
    }

    .footer {
        text-align: center;
        color: #64748b;
        font-size: 13px;
        margin-top: 30px;
    }

    div.stButton > button {
        width: 100%;
        height: 48px;
        border-radius: 12px;
        font-size: 17px;
        font-weight: 600;
        background: linear-gradient(90deg, #2563eb, #7c3aed);
        color: white;
        border: none;
    }

    div.stButton > button:hover {
        background: linear-gradient(90deg, #1d4ed8, #6d28d9);
        color: white;
        border: none;
    }
</style>
""", unsafe_allow_html=True)


st.markdown('<div class="main-card">', unsafe_allow_html=True)

st.markdown('<div class="title">🔐 Escape</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Sistema de desbloqueio de imagem criptografada.</div>',
    unsafe_allow_html=True
)

st.markdown("""
<div class="info-box">
Digite a senha correta para acessar o conteúdo protegido.
</div>
""", unsafe_allow_html=True)


# Melhor forma: senha escondida nos Secrets do Streamlit
senha_correta = st.secrets.get("SENHA_APP", "1234")

senha = st.text_input("Digite a senha:", type="password", placeholder="Insira a senha aqui")

botao = st.button("Desbloquear imagem")

if botao:
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
            st.error("Erro: chave.key ou foto.enc não foram encontrados.")
        except Exception as erro:
            st.error("Erro ao desbloquear a imagem.")
            st.write(erro)

    else:
        st.error("Senha incorreta. Tente novamente.")

st.markdown('</div>', unsafe_allow_html=True)

st.markdown(
    '<div class="footer">Projeto desenvolvido em Python com Streamlit</div>',
    unsafe_allow_html=True
)
