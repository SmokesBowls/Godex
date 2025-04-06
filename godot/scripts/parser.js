export function parseMarkdown(markdown) {
  const lines = markdown.split('\n');
  let html = '';
  for (let line of lines) {
    if (line.startsWith('# ')) {
      html += `<div class='codex-title'>${line.slice(2)}</div>`;
    } else if (line.startsWith('## ')) {
      html += `<h2>${line.slice(3)}</h2>`;
    } else if (line.startsWith('@')) {
      html += `<div class='codex-tag'>${line}</div>`;
    } else {
      html += `<p>${line}</p>`;
    }
  }
  return html;
}
