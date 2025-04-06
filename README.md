# Godex

**Godex** is a lore-first, game-integrated Codex system built to bridge narrative design and real-time game logic—directly from Markdown to Godot.

It allows writers and developers to collaborate in a unified pipeline where:
- Markdown files are the source of truth
- GitHub syncs lore revisions and expansions
- A web-based Electron viewer renders Codex entries for writers, editors, or designers
- A GitHub Actions pipeline converts `.md` to `.json` or `.tres` for direct Godot use

---

## Folder Structure

```
Godex/
├── electron_shell/       # Desktop Codex viewer (Electron)
│   ├── index.html
│   ├── style.css
│   ├── main.js
│   └── ...
├── lore/                 # Markdown lore files tagged with @metadata
├── tools/                # Parsers and generators (md → json/tres)
├── godot/resources/      # Auto-generated `.tres` files for in-game use
└── README.md             # You're here
```

---

## How to Run the Desktop Codex Viewer

```bash
cd electron_shell
npm install
npm start
```

Requires:
- Node.js
- Electron

---

## How to Use

1. Write your lore in `.md` files inside `/lore/`
2. Use `@title:`, `@id:`, `@category:` and other structured tags
3. Push to GitHub
4. GitHub Actions or `tools/parse_to_json.py` will process the entries
5. Codex entries become viewable via Electron or loadable in Godot

---

## Example Markdown Format

```markdown
@title: Blood of the Star Needle
@id: chapter_star_awakening_006
@category: chapter
@summary: A wanderer's fateful encounter with an ancient monolith...
@connected_characters: ["The Wanderer", "Tran Crimsonblood"]
@tags: [awakening, bloodline, geometric_magic]
```

---

## Future Plans

- Timeline filter and tag search in Electron viewer
- Quest system and Codex unlock logic in Godot
- Auto-dialogue JSON extraction
- Lore import from Obsidian vaults

---

Created with mythic intent by SmokesBowls.
Codex must live. Knowledge must awaken.
