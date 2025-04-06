import os
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
            key = tag[1:]
            if key in ["connected_characters", "connected_locations", "connected_artifacts", "connected_factions", "dialogue_triggers", "tags"]:
                try:
                    entry[key] = eval(value)
                except:
                    entry[key] = [v.strip() for v in value.split(',')]
            else:
                entry[key] = value
        else:
            content.append(line.strip())

    entry["body"] = "\n".join([line for line in content if line])
    return entry

def convert_to_tres(entry, output_path):
    lines = []
    lines.append("[gd_resource type="Resource" load_steps=2 format=2]")
    lines.append("")
    lines.append("[resource]")
    lines.append(f"resource_name = "{entry.get('title', 'CodexEntry')}"")
    lines.append(f"category = "{entry.get('category', '')}"")
    lines.append(f"title = "{entry.get('title', '')}"")
    lines.append(f"id = "{entry.get('id', '')}"")
    lines.append(f"summary = "{entry.get('summary', '')}"")
    lines.append(f"timeline = "{entry.get('timeline', '')}"")
    lines.append(f"chapter = {entry.get('chapter', '0')}")
    lines.append(f"version = "{entry.get('version', '')}"")
    lines.append(f"unlock_condition = "{entry.get('unlock_condition', '')}"")
    lines.append(f"body = """{entry.get('body', '').replace('"', '\"')}"""")

    def format_array(values):
        return "[%s]" % ", ".join([f""{v}"" for v in values]) if values else "[]"

    lines.append(f"connected_characters = {format_array(entry.get('connected_characters', []))}")
    lines.append(f"connected_locations = {format_array(entry.get('connected_locations', []))}")
    lines.append(f"connected_artifacts = {format_array(entry.get('connected_artifacts', []))}")
    lines.append(f"connected_factions = {format_array(entry.get('connected_factions', []))}")
    lines.append(f"dialogue_triggers = {format_array(entry.get('dialogue_triggers', []))}")
    lines.append(f"tags = {format_array(entry.get('tags', []))}")

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("\n".join(lines))

def process_lore_dir(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        if filename.endswith('.md'):
            entry = parse_codex_file(os.path.join(input_dir, filename))
            out_path = os.path.join(output_dir, f"{entry.get('id', filename[:-3])}.tres")
            convert_to_tres(entry, out_path)
            print(f"Generated: {out_path}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Convert Codex .md files to Godot .tres resources")
    parser.add_argument('--input-dir', required=True, help="Path to folder containing .md files")
    parser.add_argument('--output-dir', required=True, help="Path to save .tres files")
    args = parser.parse_args()

    process_lore_dir(args.input_dir, args.output_dir)
