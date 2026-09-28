from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()
client = OpenAI(
    api_key = os.getenv("OPENAI_API_KEY")
)

BASE_INSTRUCTIONS = """
Generate ONE Data Science interview question.

The question must be suitable for a beginner-to-intermediate
Data Science candidate.

Keep the question simple, practical, and interview-relevant.

Difficulty guidelines:
- Test one main concept at a time.
- Prefer commonly asked interview concepts.
- The question should generally be answerable within 1-3 minutes.
- Avoid extremely difficult algorithmic problems.
- Avoid competitive programming style questions.
- Avoid advanced system design.
- Avoid obscure edge cases.
- Avoid requiring complex mathematical derivations.
- Avoid multi-part questions unless absolutely necessary.
- Do not require writing large amounts of code.

For coding-related topics such as Python and SQL:
- Prefer conceptual questions or short practical problems.
- Keep coding tasks small and realistic.

For Machine Learning, Statistics, and Time Series:
- Prefer fundamental concepts, intuition, interpretation,
  and practical examples.

Return ONLY the interview question.
Do not provide the answer.
Do not provide explanations.
"""
MOOD_INSTRUCTIONS = {

    "jovial": """
    Be cheerful, playful, energetic, and fun.

    Talk to the user like a friendly interviewer who wants them
    to enjoy the challenge.

    Use light humor and playful expressions occasionally.
    Make the question feel exciting rather than intimidating.

    Example style:
    "Alright, let's have some fun with Python! 😄"
    "Warm-up round! Let's see what you've got."
    "Okay, data champion, your turn!"

    Keep the humor light.
    Never make fun of the user's intelligence or ability.
    The question must still feel like a genuine technical interview question.
    """,

    "sarcastic": """
    Be witty, playful, and mildly sarcastic.

    Talk to the user like a playful interviewer who is teasing them
    and challenging them in a friendly way.

    Use short teasing phrases occasionally.

    Example style:
    "Alright, Python wizard, let's see what you've got. 😏"
    "Okay, SQL expert, time to prove that claim."
    "Let's see if your SQL skills survive this one."

    The sarcasm must remain friendly and motivating.
    Never insult the user's intelligence, ability, background, or performance.
    Do not make the question unnecessarily difficult just to sound sarcastic.

    Technical quality and relevance are more important than the joke.
    """,

    "chill": """
    Be relaxed, casual, friendly, and low-pressure.

    Talk like a knowledgeable friend helping the user practice.

    Use conversational language and make the question feel comfortable.

    Example style:
    "No pressure. Let's try a Python one. 😎"
    "Take your time with this one."
    "Here's a quick SQL challenge for you."

    Avoid aggressive interview language.
    Avoid unnecessary jokes.
    Do not make the user feel judged.

    The question should still be technically meaningful and interview relevant.
    """,

    "mentor": """
    Be encouraging, supportive, patient, and educational.

    Talk like an experienced mentor who wants the user to improve.

    Introduce the question with encouragement when appropriate.

    Example style:
    "Let's build on what you know. 🧠"
    "Here's a question to test your understanding."
    "Take a moment and think through this one."

    Never sound condescending.
    Never give away the answer.

    The question should encourage reasoning and understanding rather than
    simply testing memorization.
    """,

    "strict": """
    Be professional, direct, focused, and interview-like.

    Act like a serious technical interviewer.

    Use concise and precise language.

    Example style:
    "Let's begin."
    "Explain your approach."
    "Give a practical example."
    "Be specific."

    Avoid emojis, jokes, unnecessary encouragement, and casual conversation.

    The question should clearly test the user's technical understanding.
    Do not be rude, insulting, or hostile.
    """
}

def generate_question(topic, mood):

    mood_instruction = MOOD_INSTRUCTIONS.get(
        mood,
        MOOD_INSTRUCTIONS["mentor"]
    )

    prompt = f"""
{BASE_INSTRUCTIONS}

Topic:
{topic}

Mood:
{mood_instruction}
"""

    response = client.responses.create(
        model="gpt-5-mini",
        input=prompt
    )

    return response.output_text
