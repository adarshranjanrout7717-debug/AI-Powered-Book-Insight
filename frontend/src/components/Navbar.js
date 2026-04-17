import { Link } from "react-router-dom";

function Navbar() {
  return (
    <div className="backdrop-blur-md bg-white/10 border-b border-white/20 px-6 py-4 flex justify-between items-center">
      <h1 className="text-xl font-bold tracking-wide">📚 AI Book Platform</h1>

      <div className="space-x-6">
        <Link to="/" className="hover:text-blue-400 transition">Home</Link>
        <Link to="/qa" className="hover:text-blue-400 transition">Ask AI</Link>
      </div>
    </div>
  );
}

export default Navbar;