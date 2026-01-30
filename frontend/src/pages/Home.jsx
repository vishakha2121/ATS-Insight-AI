import { useState } from "react";
import ResumeUpload from "../components/ResumeUpload";
import JDInput from "../components/JDInput";
import ResultCard from "../components/ResultCard";
import ExplanationBox from "../components/ExplanationBox";
import Loader from "../components/Loader";
import { analyzeResume } from "../services/api";

export default function Home() {
  const [resume, setResume] = useState(null);
  const [jd, setJd] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const submit = async () => {
    if (!resume || !jd) {
      alert("Please upload resume and paste job description");
      return;
    }

    setLoading(true);
    const res = await analyzeResume(resume, jd);
    setResult(res);
    setLoading(false);
  };

  return (
    <div className="container">
      {/* Header */}
      <div className="header">
        <h1>ATS Insight AI</h1>
        <p>Smart Resume Screening with Explainable AI</p>
      </div>

      {/* Resume Upload */}
      <label className="label">Upload Candidate Resume</label>
      <ResumeUpload setResume={setResume} />

      {/* Job Description */}
      <label className="label">Job Description</label>
      <JDInput jd={jd} setJd={setJd} />

      {/* Button */}
      <button onClick={submit}>
        {loading ? "Analyzing..." : "Analyze Resume"}
      </button>

      {/* Loader */}
      {loading && <Loader />}

      {/* Result */}
      {result && (
        <div className="result-card">
          <h3>Resume Match Score</h3>
          <div className="score">{result.score}%</div>
          <div className="explanation">
            <strong>AI Insight:</strong> {result.explanation}
          </div>
        </div>
      )}

      {/* Footer */}
      <div className="footer">
        Disclaimer: This tool assists recruiters using AI insights.
        Final hiring decisions should involve human judgment.
      </div>
    </div>
  );
}
