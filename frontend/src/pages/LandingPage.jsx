import React, { useEffect } from "react";
import { useNavigate } from "react-router-dom";

function LandingPage() {
  const navigate = useNavigate();
  const therapistId = localStorage.getItem("therapist_id");

  // Redirect to login if not logged in
  useEffect(() => {
    if (!therapistId) {
      navigate("/");
    }
  }, [therapistId, navigate]);

  const handleLogout = () => {
    localStorage.removeItem("therapist_id");
    navigate("/");
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-indigo-100 to-purple-100 relative">
      {/* Header with Logout Button */}
      <div className="absolute top-0 left-0 w-full p-6 flex justify-between items-center">
        <h1 className="text-2xl font-bold text-indigo-700">AFFECTA</h1>
        <button
          onClick={handleLogout}
          className="bg-red-500 text-white px-4 py-2 rounded-lg hover:bg-red-600 transition"
        >
          Logout
        </button>
      </div>

      {/* Centered Content */}
      <div className="flex items-center justify-center h-screen">
        <div className="text-center px-4">
          <h1 className="text-4xl font-bold mb-6 text-indigo-800">
            Welcome to AFFECTA
          </h1>
          <p className="mb-10 text-lg text-indigo-600 max-w-xl mx-auto">
            A mental health tool powered by AI to analyze facial and vocal emotions in therapy sessions.
          </p>

          <div className="space-x-4">
            <button
              onClick={() => navigate("/upload")}
              className="bg-indigo-600 text-white px-6 py-3 rounded-2xl hover:bg-indigo-700 transition"
            >
              Upload Session
            </button>
            <button
              onClick={() => navigate("/analyze")}
              className="bg-purple-600 text-white px-6 py-3 rounded-2xl hover:bg-purple-700 transition"
            >
              Analyze Session
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}

export default LandingPage;
