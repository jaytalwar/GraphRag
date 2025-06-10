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
