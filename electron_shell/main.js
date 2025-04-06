const { ipcRenderer } = require('electron');

// Simple mock of Codex content
document.getElementById('root').innerHTML = `
  <h1>Codex Viewer</h1>
  <p>This will load your markdown-powered codex files.</p>
`;
