import os
import json
import re

class DirectoryParser:
    def __init__(self, root_path='docs', output_path='temp_data'):
        """Initialize root and output paths."""
        self.root_path = root_path
        self.output_path = output_path
        os.makedirs(self.output_path, exist_ok=True)

    @staticmethod
    def clean_text(text, indent_width=4):
        """ Clean text using regex for code blocks, markdown symbols, etc and converting headings to H1,H2 etc. and list items to L1,L2 etc """
        text = re.sub(r'```.*?```', '', text, flags=re.DOTALL)
        text = re.sub(r'\[.*?\]\(.*?\)', '', text)

        lines = text.splitlines()
        new_lines = []

        for line in lines:
            line = line.rstrip()
            heading_match = re.match(r'^(#{1,6})\s+(.*)', line)
            if heading_match:
                hashes, content = heading_match.groups()
                level = len(hashes)
                new_lines.append(f"H{level}: {content.strip()}")
                continue

            list_match = re.match(r'^(\s*)-\s+(.*)', line)
            if list_match:
                spaces, content = list_match.groups()
                level = len(spaces) // indent_width + 1
                new_lines.append(f"L{level}: {content.strip()}")
                continue

            cleaned_line = re.sub(r'[>*`]', '', line).strip()
            new_lines.append(cleaned_line)

        return '\n'.join(new_lines)

    def parse(self):
        """ Recursively walks through the root directory and processes each Markdown (.md) file to extract content and structure, converting them into JSON format. """
        for directory_path, sub_directories, file_names in os.walk(self.root_path):
            self.process_directory(directory_path, sub_directories, file_names)

    def process_directory(self, directory_path, sub_directories, file_names):
        """ This function scans a directory to gather information about its subdirectories and markdown files, and saves this structure as a JSON file """
        children = []

        for sub_dir in sub_directories:
            if sub_dir.startswith('.'):
                continue
            entry_path = os.path.join(directory_path, sub_dir)
            children.append({
                "name": sub_dir,
                "type": "directory",
                "path": os.path.relpath(entry_path, self.root_path).replace('\\', '/')
            })

        for file in file_names:
            if file.startswith('.') or not file.endswith('.md'):
                continue
            entry_path = os.path.join(directory_path, file)
            name = os.path.splitext(file)[0]
            rel_path = os.path.relpath(entry_path, self.root_path).replace('\\', '/')
            children.append({
                "name": name,
                "type": "file",
                "path": rel_path
            })
            self.process_markdown_file(entry_path)

        if children:
            dir_json = {
                "name": os.path.basename(directory_path),
                "type": "directory",
                "content": "",
                "children": children,
                "path": os.path.relpath(directory_path, self.root_path).replace('\\', '/')
            }
            rel_path = os.path.relpath(directory_path, self.root_path).replace('\\', '/')
            json_filename = rel_path.replace('/', '_') + '.json'
            output_path = os.path.join(self.output_path, json_filename)
            self.save_json(dir_json, output_path)

    def process_markdown_file(self, file_path):
        """Process each .md file into cleaned JSON with full relative path naming."""
        with open(file_path, 'r', encoding='utf-8') as f:
            raw_content = f.read()

        cleaned_content = self.clean_text(raw_content)
        rel_path = os.path.relpath(file_path, self.root_path).replace('\\', '/')

        json_data = {
            "name": os.path.splitext(os.path.basename(file_path))[0],
            "type": "file",
            "content": cleaned_content,
            "children": [],
            "path": rel_path
        }

        filename_base = os.path.splitext(rel_path)[0]
        json_filename = filename_base.replace('/', '_') + '.json'
        output_file_path = os.path.join(self.output_path, json_filename)
        self.save_json(json_data, output_file_path)

    def save_json(self, data, output_file_path):
        """Save given data to a JSON file in the output path."""
        with open(output_file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
