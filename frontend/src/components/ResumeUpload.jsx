export default function ResumeUpload({ setResume }) {
  return (
    <input
      type="file"
      accept=".pdf,.txt"
      onChange={(e) => setResume(e.target.files[0])}
    />
  );
}
