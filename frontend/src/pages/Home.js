import { useEffect, useState } from "react";
import { getBooks } from "../api";
import { Link } from "react-router-dom";

function Home() {
  const [books, setBooks] = useState([]);
  const [summaries, setSummaries] = useState({});
  const [loadingId, setLoadingId] = useState(null); // 🔥 track which book is loading

  useEffect(() => {
    getBooks().then(setBooks);
  }, []);

  const handleSummary = async (e, bookId) => {
    e.preventDefault();

    setLoadingId(bookId); // start loading

    try {
      const res = await fetch(
        `http://127.0.0.1:8000/api/summary/${bookId}/`
      );
      const data = await res.json();

      setSummaries((prev) => ({
        ...prev,
        [bookId]: data.summary,
      }));
    } catch (error) {
      console.error(error);
      alert("Failed to fetch summary");
    }

    setLoadingId(null); // stop loading
  };

  return (
    <div className="p-6">
      <h1 className="text-3xl font-bold mb-6">📚 Book List</h1>

      {/* Empty state */}
      {books.length === 0 && (
        <p className="text-gray-400">No books available</p>
      )}

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {books.map((book) => (
          <Link to={`/book/${book.id}`} key={book.id}>
            <div className="backdrop-blur-lg bg-white/10 border border-white/20 p-5 rounded-2xl shadow-lg hover:scale-105 transition duration-300">

              <h2 className="text-lg font-semibold">{book.title}</h2>
              <p className="text-gray-300">{book.author}</p>
              <p className="text-yellow-400">⭐ {book.rating}</p>

              <button
                disabled={loadingId === book.id}
                className="mt-3 px-4 py-2 bg-gradient-to-r from-green-400 to-blue-500 rounded-lg hover:opacity-80 transition disabled:opacity-50"
                onClick={(e) => handleSummary(e, book.id)}
              >
                {loadingId === book.id ? "Generating..." : "✨ Get Summary"}
              </button>

              {/* Summary */}
              {summaries[book.id] && (
                <div className="mt-3 p-3 rounded-lg bg-white/10 border border-white/20 text-sm text-gray-200">
                  {summaries[book.id]}
                </div>
              )}
            </div>
          </Link>
        ))}
      </div>
    </div>
  );
}

export default Home;