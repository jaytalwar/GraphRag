import os
import json
import re

class DirectoryParser:
    
    def __init__(self, root_path='docs', output_path='temp_data'):
        """ Initialize root and output paths """        
        self.root_path = root_path
        self.output_path = output_path

    @staticmethod
    def clean_text(text,indent_width=4):
        """ Clean text using regex for code blocks, markdown symbols, etc and converting headings to H1,H2 etc. and list items to L1,L2 etc. """
        text = re.sub(r'```.*?```', '', text, flags=re.DOTALL)
        text = re.sub(r'\[.*?\]\(.*?\)', '', text)

        lines =text .splitlines()
        new_lines=[]
        for line in lines:
            line =line.rstrip()

            heading_match=re.match(r'^(#{1,6})\s+(.*)', line)
            if heading_match:
                hashes,content=heading_match.groups()
                level=len(hashes)
                new_lines.append(f"H{level}: {content.strip()}")
                continue

            
            list_match=re.match(r'^(\s*)-\s+(.*)', line)
            if list_match:
                spaces,content=list_match.groups()
                level=len(spaces)// indent_width+1
                new_lines.append(f"L{level}:{content.strip()}")
                continue

            cleaned_line=re.sub(r'[>*`]','',line).strip()
            new_lines.append(cleaned_line)

 
        return '\n'.join(new_lines)

    def parse(self):
        """ Recursively walks through the root directory and processes each Markdown (.md) file to extract content and structure, converting them into JSON format. """

        for directory_path, sub_directories, file_names in os.walk(self.root_path):
            self.process_folder(directory_path, sub_directories, file_names)

    def process_folder(self, directory_path, sub_directories, file_names):
        """ This function scans a folder to gather information about its subfolders and markdown files , and saves this structure as a JSON file  """
        folder_children = []

        for entry in sorted(sub_directories + file_names):
            entry_path = os.path.join(directory_path, entry)

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
                "name": os.path.basename(directory_path),
                "type":"directory",
                "content": "",
                "children": folder_children,
                "path": os.path.relpath(directory_path, self.root_path).replace('\\', '/')
            }
            folder_name = os.path.basename(directory_path) or "root"
            output_path = os.path.join(self.output_path, folder_name + ".json")
            self._save_json(folder_json, output_path)


    def process_markdown_file(self, file_path, folder_children):
        """ Clean and save individual markdown file as JSON. """
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
 
        json_filename = file_name + '.json'
        output_path = os.path.join(self.output_path, json_filename)
        self._save_json(json_data, output_path)

    def _save_json(self, data, output_path):
        """ Save given data to a JSON file in the output path. """
        dir_name = os.path.dirname(output_path)
        if dir_name:
            os.makedirs(dir_name, exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)


