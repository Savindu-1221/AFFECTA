import React, { useState } from "react";
import axios from "axios";
import { useNavigate, Link } from "react-router-dom";

const TherapistLogin = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [errorMsg, setErrorMsg] = useState("");
  const navigate = useNavigate();

  const handleLogin = async (e) => {
    e.preventDefault();
    const formData = new FormData();
    formData.append("email", email);
    formData.append("password", password);

    try {
      const response = await axios.post("http://localhost:8000/login", formData);
      const therapistId = response.data.therapist_id;

      // Store therapist ID temporarily
      localStorage.setItem("therapist_id", therapistId);
      navigate("/home", { state: { therapistId } });
    } catch (err) {
      const detail = err.response?.data?.detail || "Login failed.";
      setErrorMsg(detail);
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-[#e0f7fa] to-[#ffffff] px-4">
      <div className="bg-white shadow-2xl rounded-xl p-8 w-full max-w-md border">
        <h2 className="text-2xl font-semibold text-center text-sky-700 mb-6">Therapist Login</h2>

        <form onSubmit={handleLogin} className="space-y-4">
          <input
            type="email"
            placeholder="Email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
            className="w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-sky-500"
          />
          <input
            type="password"
            placeholder="Password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
            className="w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-sky-500"
          />

          {errorMsg && (
            <p className="text-sm text-red-600 font-medium">{errorMsg}</p>
          )}

          <button
            type="submit"
            className="w-full bg-sky-600 hover:bg-sky-700 text-white py-2 rounded-lg transition duration-200"
          >
            Sign In
          </button>
        </form>

        <div className="mt-6 text-center">
          <p className="text-sm text-gray-600">
            Don't have an account?{" "}
            <Link
              to="/register"
              className="text-sky-600 font-semibold hover:underline"
            >
              Register here
            </Link>
          </p>
        </div>
      </div>
    </div>
  );
};

export default TherapistLogin;
