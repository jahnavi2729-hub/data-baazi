import time
import streamlit as st

from backend.services.openai_Services import generate_question


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Data Baazi",
    page_icon="🎯",
    layout="centered"
)


# ============================================================
# DATA
# ============================================================

MOODS = {
    "😄 Jovial": {
        "key": "jovial",
        "description": "Cheerful, playful & energetic"
    },
    "😏 Sarcastic": {
        "key": "sarcastic",
        "description": "Witty, teasing & playful"
    },
    "😎 Chill": {
        "key": "chill",
        "description": "Relaxed, casual & low pressure"
    },
    "🧠 Mentor": {
        "key": "mentor",
        "description": "Supportive, patient & educational"
    },
    "🔥 Strict": {
        "key": "strict",
        "description": "Professional, direct & interview-like"
    }
}

TOPICS = [
    "Python",
    "SQL",
    "Machine Learning",
    "Statistics",
    "Time Series"
]

LOADING_MESSAGES = {
    "jovial": [
        "😄 Cooking up something fun...",
        "🎲 Mixing in a little challenge...",
        "✨ Finding a question worth playing...",
        "🎯 Your baazi is almost ready..."
    ],
    "sarcastic": [
        "😏 Finding a question that might humble you...",
        "🧐 Looking for something you can't Google in two seconds...",
        "🎯 Let's see what you've really got...",
        "😈 Cooking up a little trouble..."
    ],
    "chill": [
        "😎 No pressure... finding your question...",
        "☕ Taking it easy...",
        "🌿 Keeping things interesting...",
        "✨ Your question is almost ready..."
    ],
    "mentor": [
        "🧠 Preparing something worth learning...",
        "📚 Finding a question to sharpen your thinking...",
        "💡 Putting together a good challenge...",
        "🎯 Your learning moment is almost ready..."
    ],
    "strict": [
        "🔥 Preparing your challenge...",
        "🎯 Selecting your interview question...",
        "⚡ No shortcuts. Almost ready...",
        "🧠 Time to test your knowledge..."
    ]
}


# ============================================================
# CSS
# ============================================================

st.markdown("""
<style>

.stApp {
    background:
        radial-gradient(
            circle at 10% 10%,
            rgba(139, 92, 246, 0.18),
            transparent 30%
        ),
        radial-gradient(
            circle at 90% 20%,
            rgba(236, 72, 153, 0.14),
            transparent 30%
        ),
        #0b0912;
    color: #f5f3ff;
}

.block-container {
    max-width: 850px;
    padding-top: 55px;
    padding-bottom: 50px;
}

.hero {
    text-align: center;
    margin-bottom: 42px;
}

.logo {
    font-size: 18px;
    font-weight: 800;
    letter-spacing: 3px;
    color: #c084fc;
    margin-bottom: 18px;
}

.hero h1 {
    font-size: 48px;
    line-height: 1.1;
    margin: 0;
    font-weight: 800;
    background: linear-gradient(90deg, #c084fc, #f472b6);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.tagline {
    margin-top: 15px;
    font-size: 18px;
    color: #b8b1c9;
}

.section-title {
    font-size: 20px;
    font-weight: 700;
    margin-top: 30px;
    margin-bottom: 12px;
}

.description {
    color: #938ba5;
    font-size: 14px;
    margin-top: -5px;
    margin-bottom: 12px;
}

div[data-testid="stRadio"] > div {
    gap: 10px;
}

div[data-testid="stRadio"] label {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.09);
    border-radius: 14px;
    padding: 13px 16px;
}

div[data-testid="stRadio"] label:hover {
    border-color: rgba(192,132,252,0.55);
    background: rgba(192,132,252,0.08);
}

div.stButton > button {
    width: 100%;
    margin-top: 30px;
    height: 52px;
    border: none;
    border-radius: 14px;
    background: linear-gradient(90deg, #8b5cf6, #ec4899);
    color: white;
    font-size: 17px;
    font-weight: 700;
}

.question-card {
    margin-top: 30px;
    padding: 32px;
    border-radius: 20px;
    background: rgba(255,255,255,0.045);
    border: 1px solid rgba(255,255,255,0.10);
    box-shadow: 0 20px 50px rgba(0,0,0,0.25);
}

.question-label {
    color: #c084fc;
    font-size: 13px;
    font-weight: 800;
    letter-spacing: 2px;
    margin-bottom: 18px;
}

.question-text {
    color: #f8f7fb;
    font-size: 23px;
    line-height: 1.55;
    font-weight: 600;
}

.footer {
    text-align: center;
    margin-top: 60px;
    color: #625b70;
    font-size: 12px;
    letter-spacing: 2px;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# SESSION STATE
# ============================================================

if "question" not in st.session_state:
    st.session_state.question = None


# ============================================================
# HEADER
# ============================================================

st.markdown("""
<div class="hero">
<div class="logo">🎯 DATA BAAZI</div>
<h1>What's your baazi today?</h1>
<div class="tagline">Your skills. Your mood. Your baazi.</div>
</div>
""", unsafe_allow_html=True)


# ============================================================
# QUESTION SCREEN
# ============================================================

if st.session_state.question:

    st.markdown(f"""
<div class="question-card">
<div class="question-label">YOUR QUESTION</div>
<div class="question-text">{st.session_state.question}</div>
</div>
""", unsafe_allow_html=True)

    if st.button("← Change settings"):
        st.session_state.question = None
        st.rerun()

    st.stop()


# ============================================================
# SETTINGS SCREEN
# ============================================================

st.markdown(
    '<div class="section-title">Choose your vibe</div>',
    unsafe_allow_html=True
)

selected_mood = st.radio(
    "Mood",
    list(MOODS.keys()),
    horizontal=True,
    label_visibility="collapsed"
)

st.markdown(
    f'<div class="description">{MOODS[selected_mood]["description"]}</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-title">Choose your battlefield</div>',
    unsafe_allow_html=True
)

selected_topic = st.radio(
    "Topic",
    TOPICS,
    horizontal=True,
    label_visibility="collapsed"
)


# ============================================================
# GENERATE
# ============================================================

if st.button("Let's Play 🎲"):

    mood_key = MOODS[selected_mood]["key"]

    loading_placeholder = st.empty()

    try:

        for message in LOADING_MESSAGES[mood_key]:

            loading_placeholder.markdown(
                f"""
<div style="text-align:center;
            margin-top:30px;
            color:#c084fc;
            font-size:18px;
            font-weight:600;">
{message}
</div>
""",
                unsafe_allow_html=True
            )

            time.sleep(0.8)

        question = generate_question(
            selected_topic,
            mood_key
        )

        loading_placeholder.empty()

        if question and str(question).strip():

            st.session_state.question = str(question).strip()
            st.rerun()

        else:

            st.error(
                "The AI did not return a question. Please try again."
            )

    except Exception as e:

        loading_placeholder.empty()

        st.error(
            f"Something went wrong while generating the question: {e}"
        )


# ============================================================
# FOOTER
# ============================================================

st.markdown("""
<div class="footer">
DATA BAAZI • Think. Answer. Repeat.
</div>
""", unsafe_allow_html=True)