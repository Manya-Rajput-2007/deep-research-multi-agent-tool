import streamlit as st
from pipeline import run_research_pipeline


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="ResearchFlow AI",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# ============================================================
# CUSTOM CSS — DARK / ORANGE RESEARCHMIND STYLE
# ============================================================

st.markdown(
    """
    <style>
    /* ---------- Global ---------- */
    .stApp {
        background:
            radial-gradient(circle at 50% -10%, rgba(255, 91, 0, 0.10), transparent 32%),
            #07070b;
        color: #f5f5f5;
    }

    .main .block-container {
        max-width: 1180px;
        padding: 34px 28px 70px;
    }

    header[data-testid="stHeader"] {
        background: transparent;
    }

    footer {
        visibility: hidden;
    }

    /* ---------- Remove default Streamlit clutter ---------- */
    [data-testid="stSidebar"] {
        display: none;
    }

    [data-testid="stDecoration"] {
        display: none;
    }

    /* ---------- Hero ---------- */
    .hero {
        text-align: center;
        padding: 36px 0 18px;
    }

    .eyebrow {
        color: #ff8a32;
        font-size: 11px;
        font-weight: 700;
        letter-spacing: 4px;
        text-transform: uppercase;
        margin-bottom: 15px;
    }

    .brand {
        margin: 0;
        font-size: clamp(48px, 7vw, 76px);
        line-height: 0.95;
        font-weight: 900;
        letter-spacing: -4px;
        color: #f4f4f4;
    }

    .brand span {
        color: #ff6b1a;
    }

    .hero-subtitle {
        max-width: 650px;
        margin: 22px auto 0;
        color: #9a9aa5;
        font-size: 14px;
        line-height: 1.65;
    }

    .hero-line {
        width: 72px;
        height: 2px;
        margin: 28px auto 0;
        background: linear-gradient(90deg, #ff5a00, #ff8a32);
        border-radius: 10px;
    }

    /* ---------- Cards ---------- */
    .section-card {
        background: rgba(16, 16, 22, 0.86);
        border: 1px solid #202027;
        border-radius: 16px;
        padding: 22px;
        box-shadow: 0 14px 45px rgba(0, 0, 0, 0.22);
    }

    .section-label {
        color: #ff8a32;
        font-size: 11px;
        font-weight: 800;
        letter-spacing: 2px;
        text-transform: uppercase;
        margin-bottom: 9px;
    }

    .section-title {
        color: #f4f4f5;
        font-size: 20px;
        font-weight: 800;
        margin-bottom: 16px;
    }

    /* ---------- Text area ---------- */
    div[data-testid="stTextArea"] textarea {
        background: #101016 !important;
        color: #f5f5f5 !important;
        border: 1px solid #272730 !important;
        border-radius: 12px !important;
        min-height: 145px !important;
        font-size: 14px !important;
        padding: 16px !important;
    }

    div[data-testid="stTextArea"] textarea:focus {
        border-color: #ff6b1a !important;
        box-shadow: 0 0 0 1px #ff6b1a !important;
    }

    div[data-testid="stTextArea"] label {
        color: #8f8f99 !important;
        font-size: 11px !important;
        font-weight: 700 !important;
        letter-spacing: 1.5px !important;
        text-transform: uppercase !important;
    }

    /* ---------- Main orange button ---------- */
    div.stButton > button {
        width: 100%;
        min-height: 46px;
        border: none !important;
        border-radius: 10px !important;
        background: linear-gradient(90deg, #ff7518, #ff5a00) !important;
        color: white !important;
        font-weight: 800 !important;
        font-size: 14px !important;
        box-shadow: 0 7px 24px rgba(255, 91, 0, 0.22);
        transition: 0.2s ease;
    }

    div.stButton > button:hover {
        transform: translateY(-1px);
        box-shadow: 0 10px 30px rgba(255, 91, 0, 0.32);
    }

    /* ---------- Pipeline ---------- */
    .pipeline-card {
        background: rgba(16, 16, 22, 0.86);
        border: 1px solid #202027;
        border-radius: 16px;
        padding: 22px;
        height: 100%;
    }

    .pipeline-title {
        font-size: 20px;
        font-weight: 800;
        margin-bottom: 17px;
    }

    .agent {
        background: #101016;
        border: 1px solid #24242c;
        border-radius: 12px;
        padding: 15px 16px;
        margin-bottom: 10px;
    }

    .agent-top {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 10px;
    }

    .agent-name {
        font-size: 14px;
        font-weight: 800;
        color: #eeeeef;
    }

    .agent-number {
        color: #ff7a25;
        font-size: 10px;
        font-weight: 800;
        margin-right: 7px;
    }

    .agent-description {
        color: #74747e;
        font-size: 11px;
        margin-top: 7px;
    }

    .status {
        color: #62626d;
        font-size: 9px;
        font-weight: 800;
        letter-spacing: 1.2px;
    }

    .status.done {
        color: #ff7a25;
    }

    /* ---------- Topic chips ---------- */
    .try-label {
        color: #777782;
        font-size: 10px;
        font-weight: 700;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        margin: 20px 0 9px;
    }

    .chips {
        display: flex;
        flex-wrap: wrap;
        gap: 7px;
    }

    .chip {
        background: #15151c;
        border: 1px solid #292932;
        color: #8d8d98;
        border-radius: 6px;
        padding: 6px 10px;
        font-size: 10px;
    }

    /* ---------- Results ---------- */
    .results-heading {
        font-size: 26px;
        font-weight: 850;
        margin: 28px 0 14px;
    }

    .metric-card {
        background: #101016;
        border: 1px solid #23232b;
        border-radius: 10px;
        padding: 12px 15px;
    }

    .metric-label {
        color: #777782;
        font-size: 10px;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    .metric-value {
        color: #ff7a25;
        font-size: 13px;
        font-weight: 800;
        margin-top: 4px;
    }

    /* ---------- Tabs ---------- */
    button[data-baseweb="tab"] {
        color: #777782 !important;
    }

    button[data-baseweb="tab"][aria-selected="true"] {
        color: #ff7a25 !important;
    }

    div[data-baseweb="tab-highlight"] {
        background-color: #ff6b1a !important;
    }

    /* ---------- Alerts ---------- */
    div[data-testid="stAlert"] {
        background: #111117;
        border: 1px solid #282832;
        border-radius: 10px;
    }

    /* ---------- Download button ---------- */
    div[data-testid="stDownloadButton"] button {
        background: #15151c !important;
        border: 1px solid #30303a !important;
        color: #eeeeef !important;
        border-radius: 9px !important;
    }

    /* ---------- Footer ---------- */
    .footer {
        text-align: center;
        color: #4f4f58;
        font-size: 10px;
        letter-spacing: 1px;
        margin-top: 35px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# HELPERS
# ============================================================

def pipeline_agent(number, name, description, completed=False):
    status_class = "done" if completed else ""
    status_text = "COMPLETED" if completed else "WAITING"

    st.markdown(
        f"""
        <div class="agent">
            <div class="agent-top">
                <div>
                    <span class="agent-number">{number:02d}</span>
                    <span class="agent-name">{name}</span>
                </div>
                <span class="status {status_class}">{status_text}</span>
            </div>
            <div class="agent-description">{description}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


# ============================================================
# HERO
# ============================================================

st.markdown(
    """
    <div class="hero">
        <div class="eyebrow">MULTI-AGENT AI SYSTEM</div>
        <h1 class="brand">Research<span>Flow</span></h1>
        <div class="hero-subtitle">
            Four specialized AI agents collaborate — searching, reading,
            writing, and critiquing — to deliver a polished research report
            on any topic.
        </div>
        <div class="hero-line"></div>
    </div>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# MAIN INPUT + PIPELINE
# ============================================================

left, right = st.columns([1.05, 0.95], gap="large")

with left:
    st.markdown(
        """
        <div class="section-label">Research topic</div>
        """,
        unsafe_allow_html=True,
    )

    topic = st.text_area(
        "Research topic",
        placeholder="e.g. Quantum computing breakthroughs in 2026",
        height=120,
        label_visibility="collapsed",
    )

    st.markdown(
        """
        <div class="try-label">Try →</div>
        <div class="chips">
            <div class="chip">LLM agents 2026</div>
            <div class="chip">CRISPR gene editing</div>
            <div class="chip">Fusion energy progress</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")

    start = st.button(
        "⚡ Run Research Pipeline",
        use_container_width=True,
    )


with right:
    st.markdown(
        '<div class="pipeline-card"><div class="pipeline-title">Pipeline</div>',
        unsafe_allow_html=True,
    )

    completed = "research_result" in st.session_state

    pipeline_agent(
        1,
        "Search Agent",
        "Gathers recent web information",
        completed,
    )

    pipeline_agent(
        2,
        "Reader Agent",
        "Reads and extracts relevant content",
        completed,
    )

    pipeline_agent(
        3,
        "Writer Agent",
        "Drafts the full research report",
        completed,
    )

    pipeline_agent(
        4,
        "Critic Agent",
        "Reviews and scores the report",
        completed,
    )

    st.markdown("</div>", unsafe_allow_html=True)


# ============================================================
# RUN RESEARCH
# ============================================================

if start:
    if not topic.strip():
        st.warning("Please enter a research topic before starting.")
    else:
        try:
            with st.status(
                "🤖 AI agents are conducting the research...",
                expanded=True,
            ) as status:
                st.write("🔎 Search Agent is gathering sources...")
                result = run_research_pipeline(topic.strip())

                st.write("📖 Reader Agent is analyzing sources...")
                st.write("✍️ Writer Agent is preparing the report...")
                st.write("🧐 Critic Agent is reviewing the report...")

                st.session_state["research_result"] = result
                st.session_state["research_topic"] = topic.strip()

                status.update(
                    label="Research pipeline completed",
                    state="complete",
                    expanded=False,
                )

            st.rerun()

        except Exception as e:
            st.error("❌ The research pipeline encountered an error.")

            with st.expander("View technical details"):
                st.exception(e)


# ============================================================
# RESULTS
# ============================================================

if "research_result" in st.session_state:

    result = st.session_state["research_result"]

    st.divider()

    st.markdown(
        '<div class="results-heading">Research Results</div>',
        unsafe_allow_html=True,
    )

    # Metrics
    m1, m2, m3, m4 = st.columns(4)

    for column, number, label in [
        (m1, "01", "Search Agent"),
        (m2, "02", "Reader Agent"),
        (m3, "03", "Writer Agent"),
        (m4, "04", "Critic Agent"),
    ]:
        with column:
            st.markdown(
                f"""
                <div class="metric-card">
                    <div class="metric-label">{number} · {label}</div>
                    <div class="metric-value">COMPLETED</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.write("")

    report_tab, search_tab, reader_tab, critic_tab = st.tabs(
        [
            "📄 Final Report",
            "🔎 Search Results",
            "📖 Source Analysis",
            "🧐 Critic Review",
        ]
    )

    with report_tab:
        st.subheader("AI Generated Research Report")

        report = result.get(
            "report",
            "No report generated.",
        )

        st.markdown(report)

        st.download_button(
            label="⬇️ Download Research Report",
            data=report,
            file_name="research_report.txt",
            mime="text/plain",
            use_container_width=True,
        )

    with search_tab:
        st.subheader("Web Search Results")

        search_results = result.get(
            "search_results",
            "No search results available.",
        )

        st.markdown(search_results)

    with reader_tab:
        st.subheader("Deep Source Analysis")

        scraped_content = result.get(
            "scraped_content",
            "No scraped content available.",
        )

        st.markdown(scraped_content)

    with critic_tab:
        st.subheader("AI Critic Review")

        feedback = result.get(
            "feedback",
            "No critic feedback available.",
        )

        st.markdown(feedback)


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer">
        RESEARCHFLOW AI &nbsp;•&nbsp; POWERED BY LANGCHAIN
        &nbsp;•&nbsp; GROQ &nbsp;•&nbsp; TAVILY &nbsp;•&nbsp; STREAMLIT
    </div>
    """,
    unsafe_allow_html=True,
)
