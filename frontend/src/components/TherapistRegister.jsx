import React, { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";

function TherapistRegister() {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const [errorMsg, setErrorMsg] = useState("");
  const [successMsg, setSuccessMsg] = useState("");

  const navigate = useNavigate();

  const handleRegister = async (e) => {
    e.preventDefault();
    setErrorMsg("");
    setSuccessMsg("");

    const formData = new FormData();
    formData.append("name", name);
    formData.append("email", email);
    formData.append("password", password);

    try {
      const response = await axios.post("http://localhost:8000/register", formData);

      setSuccessMsg("🎉 Registration successful! Redirecting to login...");
      setTimeout(() => {
        navigate("/"); // Redirect after 2 seconds
      }, 2000);
    } catch (err) {
      const detail = err.response?.data?.detail;

      // FastAPI-style validation errors
      if (Array.isArray(detail)) {
        const firstError = detail[0]?.msg || "Invalid input.";
        setErrorMsg(firstError);
      } else {
        setErrorMsg(detail || "Registration failed.");
      }
    }
  };

  return (
    <div className="flex justify-center items-center min-h-screen bg-gradient-to-br from-indigo-50 to-white px-4">
      <div className="w-full max-w-md bg-white p-8 rounded-2xl shadow-md border">
        <h2 className="text-2xl font-bold text-center text-indigo-600 mb-6">
          Therapist Registration
        </h2>

        {/* Feedback */}
        {errorMsg && (
          <p className="text-red-600 text-sm mb-4 text-center">{errorMsg}</p>
        )}
        {successMsg && (
          <p className="text-green-600 text-sm mb-4 text-center">{successMsg}</p>
        )}

        <form onSubmit={handleRegister} className="space-y-5">
          <div>
            <label className="block text-sm font-medium text-gray-700">Name</label>
            <input
              type="text"
              value={name}
              onChange={(e) => setName(e.target.value)}
              required
              className="w-full mt-1 p-2 border rounded-md focus:ring-indigo-500 focus:border-indigo-500"
            />
          </div>

          <div>
            <label className="block text-sm font-medium text-gray-700">Email</label>
            <input
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
              className="w-full mt-1 p-2 border rounded-md focus:ring-indigo-500 focus:border-indigo-500"
            />
          </div>

          <div>
            <label className="block text-sm font-medium text-gray-700">Password</label>
            <input
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
              className="w-full mt-1 p-2 border rounded-md focus:ring-indigo-500 focus:border-indigo-500"
            />
          </div>

          <button
            type="submit"
            className="w-full py-2 px-4 bg-indigo-600 text-white font-semibold rounded-md hover:bg-indigo-700 transition"
          >
            Register
          </button>
        </form>
      </div>
    </div>
  );
}

export default TherapistRegister;
