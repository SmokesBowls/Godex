
const REPO_PATH = "SmokesBowls/mythtech-archive";
const BRANCH = "main";
const FOLDER_PATH = "lore";

const apiUrl = `https://api.github.com/repos/${REPO_PATH}/contents/${FOLDER_PATH}?ref=${BRANCH}`;

async function fetchMarkdownFiles() {
  const response = await fetch(apiUrl);
  const files = await response.json();
  const mdFiles = files.filter(file => file.name.endsWith(".md"));
  
  const container = document.getElementById('root');
  container.innerHTML = "<h1>Codex Entries</h1>";

  for (const file of mdFiles) {
    const rawUrl = file.download_url;
    const contentResp = await fetch(rawUrl);
    const text = await contentResp.text();

    const titleMatch = text.match(/@title:\s*(.*)/);
    const summaryMatch = text.match(/@summary:\s*(.*)/);
    const title = titleMatch ? titleMatch[1] : "Untitled";
    const summary = summaryMatch ? summaryMatch[1] : "No summary provided.";

    const entry = document.createElement('div');
    entry.className = "entry";
    entry.innerHTML = `<h2>${title}</h2><p>${summary}</p>`;
    container.appendChild(entry);
  }
}

window.onload = fetchMarkdownFiles;
