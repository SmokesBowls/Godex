import os
import json
import re

def parse_codex_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    entry = {}
    content = []
    for line in lines:
        if line.startswith('@'):
            tag, _, value = line.partition(':')
            tag = tag.strip()
            value = value.strip()
            if tag in ["@connected_characters", "@connected_locations", "@connected_artifacts", "@connected_factions", "@dialogue_triggers", "@tags"]:
                try:
                    entry[tag[1:]] = json.loads(value)
                except json.JSONDecodeError:
                    entry[tag[1:]] = [v.strip() for v in value.split(',')]
            else:
                entry[tag[1:]] = value
        else:
            content.append(line.strip())

    entry["body"] = "\n".join([line for line in content if line])
    return entry

def parse_all_to_json(input_dir, output_file):
    codex = []
    for filename in os.listdir(input_dir):
        if filename.endswith(".md"):
            filepath = os.path.join(input_dir, filename)
            entry = parse_codex_file(filepath)
            codex.append(entry)

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(codex, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Parse Codex Markdown into JSON")
    parser.add_argument('--input-dir', required=True, help="Path to folder containing .md lore files")
    parser.add_argument('--output', default="codex.json", help="Output JSON file")
    args = parser.parse_args()

    parse_all_to_json(args.input_dir, args.output)
    print(f"Codex JSON written to: {args.output}")
