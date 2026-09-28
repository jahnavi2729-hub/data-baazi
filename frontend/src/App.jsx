import { useEffect, useState } from "react";
import "./App.css";

const moods = [
  {
    id: "jovial",
    emoji: "😄",
    name: "Jovial",
    description: "Keep it fun",
  },
  {
    id: "sarcastic",
    emoji: "😏",
    name: "Sarcastic",
    description: "Bring the attitude",
  },
  {
    id: "chill",
    emoji: "😎",
    name: "Chill",
    description: "No pressure",
  },
  {
    id: "mentor",
    emoji: "🧠",
    name: "Mentor",
    description: "Guide me",
  },
  {
    id: "strict",
    emoji: "🔥",
    name: "Strict",
    description: "Interview mode",
  },
];

const topics = [
  {
    id: "Python",
    emoji: "🐍",
    name: "Python",
  },
  {
    id: "SQL",
    emoji: "🗄️",
    name: "SQL",
  },
  {
    id: "Machine Learning",
    emoji: "🤖",
    name: "Machine Learning",
  },
  {
    id: "Statistics",
    emoji: "📊",
    name: "Statistics",
  },
  {
    id: "Time Series",
    emoji: "📈",
    name: "Time Series",
  },
];

const loadingMessages = {
  jovial: [
    "😄 Cooking up something fun...",
    "🎲 Mixing in a little challenge...",
    "✨ Finding a question worth playing...",
    "🎯 Your baazi is almost ready...",
  ],

  sarcastic: [
    "😏 Finding a question that might humble you...",
    "🧐 Looking for something you can't Google in two seconds...",
    "🎯 Let's see what you've really got...",
    "😈 Cooking up a little trouble...",
  ],

  chill: [
    "😎 No pressure... finding your question...",
    "☕ Taking it easy...",
    "🌿 Keeping things interesting...",
    "✨ Your question is almost ready...",
  ],

  mentor: [
    "🧠 Preparing something worth learning...",
    "📚 Finding a question to sharpen your thinking...",
    "💡 Putting together a good challenge...",
    "🎯 Your learning moment is almost ready...",
  ],

  strict: [
    "🔥 Preparing your challenge...",
    "🎯 Selecting your interview question...",
    "⚡ No shortcuts. Almost ready...",
    "🧠 Time to test your knowledge...",
  ],
};

function App() {
  const [selectedMood, setSelectedMood] = useState("");
  const [selectedTopic, setSelectedTopic] = useState("");
  const [question, setQuestion] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [loadingMessage, setLoadingMessage] = useState("");

  useEffect(() => {
    if (!loading || !selectedMood) {
      return;
    }

    const messages = loadingMessages[selectedMood];

    let index = 0;

    setLoadingMessage(messages[index]);

    const interval = setInterval(() => {
      index = (index + 1) % messages.length;
      setLoadingMessage(messages[index]);
    }, 1600);

    return () => clearInterval(interval);
  }, [loading, selectedMood]);

  const generateQuestion = async () => {
    if (!selectedMood || !selectedTopic) {
      setError("Choose a vibe and a topic first.");
      return;
    }

    setLoading(true);
    setError("");
    setQuestion("");

    try {
      const response = await fetch(
        "http://127.0.0.1:8000/generate-question",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            topic: selectedTopic,
            mood: selectedMood,
          }),
        }
      );

      if (!response.ok) {
        throw new Error("Failed to generate question");
      }

      const data = await response.json();

      setQuestion(data.question);
    } catch (error) {
      console.error(error);

      setError(
        "Could not connect to Data Baazi. Make sure FastAPI is running."
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app">
      <div className="background-glow glow-one"></div>
      <div className="background-glow glow-two"></div>

      <main className="container">

        {/* HEADER */}

        <header className="header">
          <div className="logo">
            <span className="logo-mark">D</span>
            <span>DATA BAAZI</span>
          </div>

          <div className="tagline">
            Your skills. Your mood. Your baazi.
          </div>
        </header>

        {/* HOME */}

        {!question ? (
          <section className="hero">

            <div className="hero-badge">
              ✦ AI INTERVIEW PRACTICE
            </div>

            <h1>
              What's your
              <span> baazi today?</span>
            </h1>

            <p className="hero-description">
              Pick your vibe. Pick your battlefield.
              <br />
              Let's see what you've got.
            </p>

            {/* MOOD */}

            <section className="selection-section">

              <div className="section-heading">

                <span className="step-number">
                  01
                </span>

                <div>
                  <h2>
                    How should I interview you?
                  </h2>

                  <p>
                    Choose your vibe for today's session.
                  </p>
                </div>

              </div>

              <div className="mood-grid">

                {moods.map((mood) => (
                  <button
                    key={mood.id}
                    className={`mood-card ${
                      selectedMood === mood.id
                        ? "selected"
                        : ""
                    }`}
                    onClick={() => {
                      setSelectedMood(mood.id);
                      setError("");
                    }}
                  >

                    <span className="mood-emoji">
                      {mood.emoji}
                    </span>

                    <span className="mood-name">
                      {mood.name}
                    </span>

                    <span className="mood-description">
                      {mood.description}
                    </span>

                  </button>
                ))}

              </div>

            </section>

            {/* TOPIC */}

            <section className="selection-section">

              <div className="section-heading">

                <span className="step-number">
                  02
                </span>

                <div>
                  <h2>
                    Choose your battlefield.
                  </h2>

                  <p>
                    What do you want to practice today?
                  </p>
                </div>

              </div>

              <div className="topic-grid">

                {topics.map((topic) => (

                  <button
                    key={topic.id}
                    className={`topic-card ${
                      selectedTopic === topic.id
                        ? "selected"
                        : ""
                    }`}
                    onClick={() => {
                      setSelectedTopic(topic.id);
                      setError("");
                    }}
                  >

                    <span className="topic-emoji">
                      {topic.emoji}
                    </span>

                    <span>
                      {topic.name}
                    </span>

                    {selectedTopic === topic.id && (
                      <span className="check">
                        ✓
                      </span>
                    )}

                  </button>

                ))}

              </div>

            </section>

            {/* ERROR */}

            {error && (
              <div className="error-message">
                {error}
              </div>
            )}

            {/* GENERATE */}

            <button
              className="play-button"
              onClick={generateQuestion}
              disabled={loading}
            >

              {loading ? (
                <>
                  <span className="spinner"></span>

                  <span className="loading-text">
                    {loadingMessage}
                  </span>
                </>
              ) : (
                <>
                  Let's Play
                  <span className="arrow">
                    →
                  </span>
                </>
              )}

            </button>

          </section>

        ) : (

          /* QUESTION */

          <section className="question-screen">

            <div className="question-top">

              <span className="question-label">
                {
                  moods.find(
                    (mood) =>
                      mood.id === selectedMood
                  )?.emoji
                }{" "}
                {selectedMood.toUpperCase()} MODE
              </span>

              <span className="topic-label">
                {
                  topics.find(
                    (topic) =>
                      topic.id === selectedTopic
                  )?.emoji
                }{" "}
                {selectedTopic}
              </span>

            </div>

            <div className="question-card">

              <div className="question-icon">
                ?
              </div>

              <p className="question-intro">
                Your question for today:
              </p>

              <h2>
                {question}
              </h2>

            </div>

           <div className="question-actions">

  <button
    className="secondary-button"
    onClick={() => {
      setQuestion("");
      setError("");
    }}
  >
    ← Change settings
  </button>



              

            </div>

          </section>
        )}

        <footer>
          <span>DATA BAAZI</span>
          <span>•</span>
          <span>
            Think. Answer. Repeat.
          </span>
        </footer>

      </main>
    </div>
  );
}

export default App;