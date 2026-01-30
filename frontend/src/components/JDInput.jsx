export default function JDInput({ jd, setJd }) {
  return (
    <textarea
      rows="6"
      placeholder="Paste Job Description"
      value={jd}
      onChange={(e) => setJd(e.target.value)}
    />
  );
}
