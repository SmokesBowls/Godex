# Godex Tools

These scripts convert `.md` lore into JSON or `.tres` files.

- `parse_to_json.py`: outputs `codex.json`
- `parse_to_tres.py`: outputs `.tres` files to `godot/resources/`

## Usage (Termux / Desktop)

```bash
python tools/parse_to_json.py --input-dir lore --output codex.json
python tools/parse_to_tres.py --input-dir lore --output-dir godot/resources