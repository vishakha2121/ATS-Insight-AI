export async function analyzeResume(resume, jd) {
  const form = new FormData();
  form.append("resume", resume);
  form.append("jd", jd);

  const res = await fetch("http://localhost:8000/analyze", {
    method: "POST",
    body: form,
  });
  return res.json();
}
