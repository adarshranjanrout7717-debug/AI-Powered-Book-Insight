import { useState } from "react";
import { askQuestion } from "../api";

function QA() {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [sources, setSources] = useState([]);
  const [loading, setLoading] = useState(false);

  const handleAsk = async () => {
    if (!question.trim()) return;

    setLoading(true);
    const res = await askQuestion(question);
    setAnswer(res.answer);
    setSources(res.source || []);
    setLoading(false);
  };

  return (
    <div className="flex flex-col items-center p-8">
      <h1 className="text-3xl font-bold mb-6">🤖 Ask AI</h1>

      <div className="w-full max-w-2xl space-y-4">
        <textarea
          className="w-full p-4 rounded-xl bg-white/10 border border-white/20 focus:outline-none"
          rows="3"
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          placeholder="Ask anything about books..."
        />

        <button
          onClick={handleAsk}
          disabled={loading}
          className="w-full py-3 bg-gradient-to-r from-orange-500 to-pink-500 rounded-xl hover:opacity-80 transition disabled:opacity-50"
        >
          🚀 Ask AI
        </button>

        {loading && (
          <p className="text-gray-400 animate-pulse">
            🤖 Thinking...
          </p>
        )}

        {answer && (
          <div className="p-4 rounded-xl bg-white/10 border border-white/20">
            <h2 className="font-semibold mb-2">Answer:</h2>
            <p>{answer}</p>

            {sources.length > 0 && (
              <div className="mt-3 text-sm text-gray-400">
                <strong>Sources:</strong>
                {sources.map((s, i) => (
                  <p key={i}>• {s}</p>
                ))}
              </div>
            )}
          </div>
        )}
      </div>
    </div>
  );
}

export default QA;