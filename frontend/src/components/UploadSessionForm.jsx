import React, { useState } from "react";
import axios from "axios";

function UploadSessionForm() {
  const [therapistId, setTherapistId] = useState("");
  const [patientId, setPatientId] = useState("");
  const [sessionDate, setSessionDate] = useState("");
  const [file, setFile] = useState(null);

  const [uploadStatus, setUploadStatus] = useState(null);
  const [sessionId, setSessionId] = useState(null);
  const [error, setError] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setUploadStatus("Uploading...");
    setError(null);

    const formData = new FormData();
    formData.append("therapist_id", therapistId);
    formData.append("patient_id", patientId);
    formData.append("session_date", sessionDate);
    formData.append("file", file);

    try {
      const response = await axios.post("http://127.0.0.1:8000/upload-video", formData);
      const data = response.data;
      setSessionId(data.session_id);
      setUploadStatus("Upload successful!");
    } catch (err) {
      setError(`Upload failed: ${err.response?.data?.detail || err.message}`);
      setUploadStatus(null);
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-blue-100 to-white px-4">
      <div className="max-w-lg w-full p-8 shadow-2xl rounded-xl bg-white">
        <h2 className="text-2xl font-bold mb-6 text-center text-[#34495e]">
          Upload Therapy Session
        </h2>

        <form onSubmit={handleSubmit} className="space-y-4">
          <input
            type="number"
            placeholder="Therapist ID"
            value={therapistId}
            onChange={(e) => setTherapistId(e.target.value)}
            required
            className="w-full px-3 py-2 border rounded-lg"
          />
          <input
            type="number"
            placeholder="Patient ID"
            value={patientId}
            onChange={(e) => setPatientId(e.target.value)}
            required
            className="w-full px-3 py-2 border rounded-lg"
          />
          <input
            type="date"
            value={sessionDate}
            onChange={(e) => setSessionDate(e.target.value)}
            required
            className="w-full px-3 py-2 border rounded-lg"
          />
          <input
            type="file"
            accept="video/*"
            onChange={(e) => setFile(e.target.files[0])}
            required
            className="w-full"
          />
          <button
            type="submit"
            className="bg-[#3498db] text-white px-4 py-2 rounded-lg w-full hover:bg-[#2980b9] transition"
          >
            Upload
          </button>
        </form>

        {uploadStatus && (
          <div className="mt-4 text-green-600 font-medium">
            ✅ {uploadStatus} Session ID: {sessionId}
          </div>
        )}
        {error && (
          <div className="mt-4 text-red-600 font-medium">
            ❌ {error}
          </div>
        )}
      </div>
    </div>
  );
}

export default UploadSessionForm;
