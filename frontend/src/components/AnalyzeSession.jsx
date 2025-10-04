import React, { useState } from "react";
import axios from "axios";
import {
  BarChart, Bar, XAxis, YAxis, Tooltip, Legend, ResponsiveContainer, LabelList,
} from "recharts";

function AnalyzeSession() {
  const [sessionId, setSessionId] = useState("");
  const [ferResults, setFerResults] = useState([]);
  const [verResult, setVerResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const analyzeSession = async () => {
    if (!sessionId) {
      setError("Please enter a session ID");
      return;
    }

    setLoading(true);
    setError("");
    setFerResults([]);
    setVerResult(null);

    try {
      const response = await axios.get(`http://localhost:8000/analyze-session/${sessionId}`);
      setFerResults(response.data.FER_results);
      setVerResult(response.data.VER_result);
    } catch (err) {
      setError(err.response?.data?.detail || "Analysis failed");
    } finally {
      setLoading(false);
    }
  };

  const ferChartData = ferResults.map((entry) => ({
    timestamp: `T${entry.timestamp}s`,
    ...entry.emotion_scores,
  }));

  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-blue-50 to-white px-4 py-8">
      <div className="w-full max-w-4xl p-8 bg-white shadow-xl rounded-2xl">
        <h2 className="text-2xl font-semibold mb-6 text-center text-gray-800">
          🎥 Analyze Therapy Session
        </h2>

        <div className="mb-4">
          <label className="block font-medium text-gray-700 mb-1">Session ID:</label>
          <input
            type="number"
            value={sessionId}
            onChange={(e) => setSessionId(e.target.value)}
            className="w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
            placeholder="Enter session ID"
          />
        </div>

        <button
          onClick={analyzeSession}
          disabled={loading}
          className="bg-blue-600 text-white px-6 py-2 rounded-xl hover:bg-blue-700 transition w-full"
        >
          {loading ? "Analyzing..." : "Analyze Session"}
        </button>

        {error && (
          <p className="mt-4 text-red-600 font-medium text-center">{error}</p>
        )}

        {verResult && (
          <div className="mt-6 bg-gray-100 p-4 rounded-xl shadow-sm">
            <h3 className="text-xl font-semibold text-gray-700">🎤 VER Result</h3>
            <p className="text-lg mt-2 text-blue-800">
              Dominant Voice Emotion: <strong>{verResult}</strong>
            </p>
          </div>
        )}

        {ferChartData.length > 0 && (
          <div className="mt-8">
            <h3 className="text-xl font-semibold mb-2 text-gray-700">
              🎭 FER Results (Emotion Scores per Frame)
            </h3>
            <ResponsiveContainer width="100%" height={300}>
              <BarChart data={ferChartData} margin={{ top: 10, right: 30, left: 0, bottom: 5 }}>
                <XAxis dataKey="timestamp" />
                <YAxis />
                <Tooltip />
                <Legend />
                {["angry", "happy", "neutral", "sad", "fear", "disgust", "surprise"].map((emotion) => (
                  <Bar key={emotion} dataKey={emotion} stackId="a" fill={emotionColor(emotion)}>
                    <LabelList dataKey={emotion} position="top" style={{ fontSize: 10 }} />
                  </Bar>
                ))}
              </BarChart>
            </ResponsiveContainer>
          </div>
        )}
      </div>
    </div>
  );
}

// 🎨 Emotion color mapping
function emotionColor(emotion) {
  const palette = {
    angry: "#EF4444",      // Red
    happy: "#FACC15",      // Yellow
    neutral: "#9CA3AF",    // Gray
    sad: "#3B82F6",        // Blue
    fear: "#8B5CF6",       // Purple
    disgust: "#10B981",    // Green
    surprise: "#F97316",   // Orange
  };
  return palette[emotion] || "#A3A3A3";
}

export default AnalyzeSession;
