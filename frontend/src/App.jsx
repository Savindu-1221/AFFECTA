import React from "react";
import { Routes, Route } from "react-router-dom";
import TherapistLogin from "./components/TherapistLogin";
import TherapistRegister from "./components/TherapistRegister";
import UploadSessionForm from "./components/UploadSessionForm";
import AnalyzeSession from "./components/AnalyzeSession";
import LandingPage from "./pages/LandingPage";

export default function App() {
  return (
    <Routes>
      <Route path="/" element={<TherapistLogin />} />
      <Route path="/register" element={<TherapistRegister />} />
      <Route path="/upload" element={<UploadSessionForm />} />
      <Route path="/analyze" element={<AnalyzeSession />} />
      <Route path="/home" element={<LandingPage />} />
    </Routes>
  );
}
