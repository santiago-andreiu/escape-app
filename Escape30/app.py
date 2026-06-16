import streamlit as st
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
    <div class="hero-subtitle">Sistema de acesso protegido por senha</div>
</div>
""", unsafe_allow_html=True)


st.markdown("""
<div class="info-card">
    <div class="info-title">Área protegida</div>
    <div class="info-text">
        Digite a senha correta para liberar o acesso ao conteúdo protegido.
        Caso a senha esteja incorreta, o acesso continuará bloqueado.
    </div>
</div>
""", unsafe_allow_html=True)


senha_correta = st.secrets.get("SENHA_APP", "478593")

senha = st.text_input(
    "Senha:",
    type="password",
    placeholder="Digite a senha de acesso"
)

if st.button("Acessar conteúdo"):
    if senha == senha_correta:
        st.success("Acesso liberado com sucesso!")

        pasta = Path(__file__).parent
        caminho_imagem = pasta / "imagem.jpg"

        if caminho_imagem.exists():
            st.image(
                str(caminho_imagem),
                use_container_width=True
            )
        else:
            st.error("Erro: o arquivo imagem.jpg não foi encontrado.")

    else:
        st.error("Senha incorreta. Tente novamente.")


st.markdown("""
<div class="footer">
    Projeto desenvolvido em Python com Streamlit
</div>
""", unsafe_allow_html=True)
