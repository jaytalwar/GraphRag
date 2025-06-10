import os
import json
import re

class DirectoryParser:

    def __init__(self, root_path='docs', output_path='temp_data'):
        """ Initialize root and output paths """        
        self.root_path = root_path
        self.output_path = output_path

    @staticmethod
    def clean_text(text):
        """ Clean text using regex for code blocks, markdown symbols, etc """
        text = re.sub(r'```.*?```', '', text, flags=re.DOTALL)
        text = re.sub(r'\[.*?\]\(.*?\)', '', text)
        text = re.sub(r'#|\*|\-|\>|\`', '', text)
        return ' '.join(text.split())

    def parse(self):
        """ Recursively walks through the root directory and processes each Markdown (.md) file to extract content and structure, converting them into JSON format. """

        for dirpath, dirnames, filenames in os.walk(self.root_path):
            self.process_folder(dirpath,dirnames,filenames)

    def process_folder(self, dirpath, dirnames, filenames):
        """ This function scans a folder to gather information about its subfolders and markdown files , and saves this structure as a JSON file  """
        folder_children = []

        for entry in sorted(dirnames + filenames):
            entry_path = os.path.join(dirpath, entry)

            if entry.startswith('.'):
                continue
            entry_type = 'directory' if os.path.isdir(entry_path) else 'file'
            name = os.path.splitext(entry)[0] if entry_type == 'file' else entry

            if entry_type == 'file' and not entry.endswith('.md'):
                continue
           
            folder_children.append({
                "name": name,
                "type": entry_type,
                "path": os.path.relpath(entry_path, self.root_path).replace('\\', '/')
            })

            if entry_type == 'file':
                self.process_markdown_file(entry_path, folder_children)

        if folder_children:
            folder_json = {
                "name": os.path.basename(dirpath),
                "content": "",
                "children": folder_children,
                "path": os.path.relpath(dirpath, self.root_path).replace('\\', '/')
            }
            folder_name = os.path.basename(dirpath) or "root"
            output_path = os.path.join(self.output_path, folder_name + ".json")
            self._save_json(folder_json, output_path)

    def _process_markdown_file(self, file_path, folder_children):
        """Clean and save individual markdown file as JSON."""
        with open(file_path, 'r', encoding='utf-8') as file:
            raw_content = file.read()

        cleaned_content = self.clean_text(raw_content)
        file_name = os.path.splitext(os.path.basename(file_path))[0]

        json_data = {
            "name": file_name,
            "content": cleaned_content,
            "children": [],
            "path": os.path.relpath(file_path, self.root_path).replace('\\', '/')
        }

        rel_path = file_name
        self._save_json(json_data, rel_path)

    def _save_json(self, data, output_name):
        """Save given data to a JSON file in the output path."""
        output_path = os.path.join(self.output_path, output_name + ".json")
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    @classmethod
    def start(cls):
        parser = cls()
        parser.parse()