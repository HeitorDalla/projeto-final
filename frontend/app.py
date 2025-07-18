import streamlit as st

# Configuração da página Streamlit
st.set_page_config(
    page_title="Painel de Indicadores",     # Título da aba do navegador
    page_icon="📊",                         # Ícone que aparece na aba e no header
    layout="wide",                          # Usa todo o espaço horizontal
    initial_sidebar_state="collapsed",      # Sidebar começa recolhida
    menu_items={                            # Itens do menu de contexto (canto superior direito)
        'Get help': 'https://github.com/HeitorDalla/projeto-final',
        'Report a bug': 'https://github.com/HeitorDalla/projeto-final/issues',
        'About': "Aplicativo desenvolvido por Matheus V. Nellessen, Flávia ... e Heitor Villa"
    }
)

# Configurações do menu de contexto
from streamlit_option_menu import option_menu

selected = option_menu(
    menu_title=None,
    options=["Home", "Anal. Geral", "Anal. Específica"],
    icons=["house", "bar-chart", "bar-chart"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
)

# Importação de Bibliotecas e Configuração
import pandas as pd
import sys
import os

# Determina o diretório raiz do projeto (um nível "atrás" deste arquivo)
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# Insere o ROOT_DIR no início do sys.path se ainda não estiver presente
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

# Importações de conexão
from src.database.get_connection import get_connection

# Importações das Páginas
from frontend.views.home import show_home_page
from frontend.views.analise_geral import show_analise_geral_page
from frontend.views.analise_especifica import show_analise_especifica_page

# Importações de funções auxiliares
from frontend.utils.shared import aplicar_filtros, load_css

# Carrega CSS centralizado
load_css("frontend/assets/css/style.css")

# Cria três colunas proporcionais (1:2:1) no sidebar para centralizar a logo
col1, col2, col3 = st.sidebar.columns([1, 2, 1])
with col2:
    # Exibe a imagem da logo no centro da segunda coluna
    st.image("frontend/assets/img/logo.png")

# Cria conexão com o banco de dados MySQL
conn, cursor = get_connection()

# Aplicar filtros padrões (aparecem em todas as páginas)
filtros_selecionados = aplicar_filtros(conn)

# Roteamento das páginas com base na opção selecionada
if (selected == "Home"):
    show_home_page(conn, filtros_selecionados)
    # Chama a função "show_home_page" (importada do módulo "frontend.views.home")
    
if selected == 'Anal. Geral':
    show_analise_geral_page(conn, filtros_selecionados)
    # Chama a função "show_analise_geral_page" (importada do módulo "frontend.views.analise_geral")

if (selected == "Anal. Específica"):
    show_analise_especifica_page (conn, filtros_selecionados)
    # Chama a função "show_analise_especifica_page" (importada do módulo "frontend.views.analise_especifica")