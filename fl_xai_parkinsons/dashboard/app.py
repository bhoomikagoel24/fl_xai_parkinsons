# ============================================================================================================================================================
""" dashboard/app.py — Entry point ==> Run from fl_xai_parkinsons/ folder:
    streamlit run dashboard/app.py """
# ============================================================================================================================================================

import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import streamlit as st

st.set_page_config(
    page_title="FL-XAI · Parkinson's UPDRS",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Theme toggle state ────────────────────────────────────────────────────────
if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = True

dark = st.session_state.dark_mode

# ── CSS variables based on theme ──────────────────────────────────────────────
if dark:
    bg        = "#0a0e1a"
    surface   = "#111827"
    card      = "#161d2e"
    text      = "#e8edf5"
    muted     = "#7a8ba8"
    dim       = "#4a5568"
    border    = "rgba(0,212,200,0.12)"
    border_h  = "rgba(0,212,200,0.30)"
    info_bg   = "#161d2e"
    sidebar_border = "rgba(0,212,200,0.12)"
else:
    bg        = "#f8fafc"
    surface   = "#ffffff"
    card      = "#f1f5f9"
    text      = "#0f172a"
    muted     = "#475569"
    dim       = "#94a3b8"
    border    = "rgba(0,0,0,0.08)"
    border_h  = "rgba(0,150,136,0.4)"
    info_bg   = "#e8f5f3"
    sidebar_border = "rgba(0,0,0,0.08)"

teal   = "#00b4aa" if not dark else "#00d4c8"
violet = "#6c5ce7" if not dark else "#7c6aff"
amber  = "#d48806" if not dark else "#f5a623"
red    = "#e53e3e" if not dark else "#ff6b6b"
green  = "#38a169" if not dark else "#56d99f"

st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;600&family=Sora:wght@300;400;600;700&display=swap');

html, body, [class*="css"] {{
  font-family: 'Sora', sans-serif !important;
  background-color: {bg} !important;
  color: {text} !important;
}}
.main .block-container {{ padding: 1.5rem 2.5rem; max-width: 1400px; }}

/* Hide Streamlit auto file-based page nav */
[data-testid="stSidebarNav"] {{ display: none !important; }}

section[data-testid="stSidebar"] {{
  background: {surface} !important;
  border-right: 1px solid {border} !important;
}}
section[data-testid="stSidebar"] .stRadio > label {{
  display: none;
}}
section[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label {{
  font-family: 'IBM Plex Mono', monospace !important;
  font-size: 0.78rem !important;
  color: {muted} !important;
  padding: 6px 10px !important;
  border-radius: 6px !important;
  margin: 2px 0 !important;
  transition: all 0.15s;
}}
section[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label:hover {{
  background: {card} !important;
  color: {text} !important;
}}

[data-testid="stMetric"] {{
  background: {card} !important;
  border: 1px solid {border} !important;
  border-radius: 12px !important;
  padding: 1.2rem !important;
}}
[data-testid="stMetricLabel"] {{
  font-size: 0.72rem !important;
  letter-spacing: 0.1em !important;
  text-transform: uppercase !important;
  color: {muted} !important;
  font-family: 'IBM Plex Mono', monospace !important;
}}
[data-testid="stMetricValue"] {{
  font-size: 1.9rem !important;
  font-weight: 700 !important;
  color: {teal} !important;
  font-family: 'IBM Plex Mono', monospace !important;
}}

.stTabs [data-baseweb="tab-list"] {{
  background: {surface} !important;
  border-radius: 10px; gap: 4px; padding: 4px;
}}
.stTabs [data-baseweb="tab"] {{
  background: transparent !important;
  color: {muted} !important;
  border-radius: 8px !important;
  font-size: 0.75rem !important;
  text-transform: uppercase !important;
  font-family: 'IBM Plex Mono', monospace !important;
}}
.stTabs [aria-selected="true"] {{
  background: {card} !important;
  color: {teal} !important;
  border: 1px solid {border_h} !important;
}}

/* Dataframe */
.stDataFrame {{ border: 1px solid {border} !important; border-radius: 8px !important; }}

h1, h2, h3 {{ font-family: 'Sora', sans-serif !important; font-weight: 700 !important; color: {text} !important; }}
h1 {{ font-size: 2.2rem !important; }}
hr {{ border-color: {border} !important; margin: 2rem 0 !important; }}

.badge {{ display: inline-block; padding: 2px 10px; border-radius: 20px;
          font-size: 0.72rem; font-family: 'IBM Plex Mono', monospace;
          letter-spacing: 0.08em; font-weight: 600; margin-right: 6px; margin-top: 4px; }}
.badge-teal   {{ background: rgba(0,212,200,0.15); color: {teal}; border: 1px solid rgba(0,212,200,0.3); }}
.badge-violet {{ background: rgba(124,106,255,0.15); color: {violet}; border: 1px solid rgba(124,106,255,0.3); }}
.badge-amber  {{ background: rgba(245,166,35,0.15); color: {amber}; border: 1px solid rgba(245,166,35,0.3); }}
.badge-red    {{ background: rgba(255,107,107,0.15); color: {red}; border: 1px solid rgba(255,107,107,0.3); }}

.info-box {{
  background: {info_bg}; border: 1px solid {border};
  border-left: 3px solid {teal}; border-radius: 8px;
  padding: 1rem 1.2rem; margin: 0.5rem 0;
  font-size: 0.88rem; line-height: 1.6; color: {muted};
}}

/* Plotly chart background fix for light mode */
.js-plotly-plot .plotly .bg {{ fill: {card} !important; }}

/* Select box */
.stSelectbox > div > div {{
  background: {card} !important;
  border-color: {border} !important;
  color: {text} !important;
}}
</style>
""", unsafe_allow_html=True)

# ── Store theme colors in session state so pages can access them ──────────────
st.session_state["theme"] = {
    "dark": dark, "bg": bg, "surface": surface, "card": card,
    "text": text, "muted": muted, "dim": dim, "border": border,
    "teal": teal, "violet": violet, "amber": amber, "red": red, "green": green,
}

# ── Page imports ──────────────────────────────────────────────────────────────
from dashboard.pages.home             import render as render_home
from dashboard.pages.ensemble_compare import render as render_ensemble
from dashboard.pages.explainability   import render as render_xai
from dashboard.pages.all_pages        import (
    render_federated_monitor,
    render_client_analytics,
    render_convergence,
    render_statistical,
    render_communication,
    render_ablation,
)

PAGES = {
    ":material/dashboard: Overview": render_home,
    ":material/hub: Federated Training": render_federated_monitor,
    ":material/groups: Client Analytics": render_client_analytics,
    ":material/compare_arrows: Ensemble Comparison": render_ensemble,
    ":material/trending_up: Convergence": render_convergence,
    ":material/psychology: Explainability (SHAP)": render_xai,
    ":material/analytics: Statistical Validation": render_statistical,
    ":material/settings_ethernet: Communication Cost": render_communication,
    ":material/science: Ablation Study": render_ablation,
}

# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    # Brand
    st.markdown(f"""
    <div style='padding:1rem 0 0.8rem;border-bottom:1px solid {border};margin-bottom:0.8rem;'>
      <div style='font-family:IBM Plex Mono,monospace;font-size:0.6rem;color:{muted};
                  letter-spacing:0.14em;text-transform:uppercase;margin-bottom:6px;'>
        Healthcare AI
      </div>
      <div style='font-size:1.1rem;font-weight:700;color:{text};line-height:1.3;'>
        FL-XAI<br>
        <span style='color:{teal};'>Parkinson's UPDRS</span>
      </div>
    </div>
    """, unsafe_allow_html=True)

    # Theme toggle
    col_a, col_b = st.columns([1, 1])
    with col_a:
        st.markdown(f"<div style='font-family:IBM Plex Mono,monospace;font-size:0.62rem;color:{muted};padding-top:8px;'>{'🌙 Dark' if dark else '☀️ Light'}</div>", unsafe_allow_html=True)
    # with col_b:
    #     if st.button("Switch", use_container_width=True):
    #         st.session_state.dark_mode = not st.session_state.dark_mode
    #         st.rerun()

    st.markdown(f"<hr style='border-color:{border};margin:0.6rem 0;'>", unsafe_allow_html=True)

    # Navigation
    page_name = st.radio(
        "Navigation",
        list(PAGES.keys()),
        label_visibility="collapsed"
    )

    st.markdown(f"<hr style='border-color:{border};margin:0.6rem 0;'>", unsafe_allow_html=True)

    # Footer info
    st.markdown(f"""
    <div style='font-family:IBM Plex Mono,monospace;font-size:0.6rem;color:{dim};line-height:1.9;'>
      Dataset · Oxford UPDRS<br>
      Clients · 5 Hospitals<br>
      Models  · RF · GB · AB · DT<br>
      Rounds  · 6 (early stop)<br>
      Target  · Total UPDRS
    </div>
    """, unsafe_allow_html=True)

# ── Render page ───────────────────────────────────────────────────────────────
PAGES[page_name]()