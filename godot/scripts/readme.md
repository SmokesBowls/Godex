#### **Inside `/godot/scripts/` → `README.md`:**
```markdown
# Godot Codex Scripts

- `CodexEntry.gd` defines the data structure used in `.tres` files
- `CodexLoader.gd` loads all `.tres` entries from a folder and returns them as a dictionary

## Example (in a scene script)

```gdscript
var codex = CodexLoader.load_codex_entries("res://godot/resources/")
print(codex["chapter_star_awakening_006"].title)