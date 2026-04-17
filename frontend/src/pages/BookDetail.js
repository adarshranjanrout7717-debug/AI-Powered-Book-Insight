import { useParams } from "react-router-dom";
import { useEffect, useState } from "react";

function BookDetail() {
  const { id } = useParams();

  const [book, setBook] = useState(null);
  const [insights, setInsights] = useState(null);
  const [recommendations, setRecommendations] = useState([]);

  useEffect(() => {
    fetch(`http://127.0.0.1:8000/api/books/${id}/`)
      .then(res => res.json())
      .then(setBook);
  }, [id]);

  const getInsights = async () => {
    const res = await fetch(`http://127.0.0.1:8000/api/insights/${id}/`);
    const data = await res.json();
    setInsights(data);
  };

  const getRecommendations = async () => {
  try {
    const res = await fetch(`http://127.0.0.1:8000/api/recommend/${id}/`);
    const data = await res.json();

    console.log("RESPONSE:", data); // 🔥 debug

    if (data.recommendations) {
      setRecommendations(data.recommendations);
    } else {
      alert("No recommendations found");
    }
  } catch (err) {
    console.error(err);
    alert("Error fetching recommendations");
  }
};

  if (!book) return <p className="p-6">Loading...</p>;

  return (
    <div className="p-8 max-w-3xl mx-auto backdrop-blur-lg bg-white/10 border border-white/20 rounded-2xl shadow-xl">

      <h1 className="text-3xl font-bold">{book.title}</h1>
      <p className="text-gray-300 mt-2">{book.author}</p>

      <p className="mt-4 text-gray-200">{book.description}</p>

      {/* Buttons */}
      <div className="mt-6 flex gap-4">
        <button
          onClick={getInsights}
          className="px-5 py-2 bg-blue-500 rounded-lg hover:bg-blue-600 transition"
        >
          📊 Insights
        </button>

        <button
          onClick={getRecommendations}
          className="px-5 py-2 bg-green-500 rounded-lg hover:bg-green-600 transition"
        >
          📚 Recommend
        </button>
      </div>

      {/* Insights */}
      {insights && (
        <div className="mt-4 p-4 border border-white/20 rounded bg-white/10">
          <p><strong>Genre:</strong> {insights.genre}</p>
          <p><strong>Sentiment:</strong> {insights.sentiment}</p>
        </div>
      )}

      {/* Recommendations */}
      {recommendations.length > 0 && (
        <div className="mt-4 p-4 border border-white/20 rounded bg-white/10">
          <h2 className="font-bold mb-2">Recommendations:</h2>
          {recommendations.map((rec, index) => (
            <p key={index}>• {rec}</p>
          ))}
        </div>
      )}
    </div>
  );
}

export default BookDetail;