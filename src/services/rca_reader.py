"""
This module contains artefacts needed to read the RCAs and clean the text data
"""

from io import TextIOWrapper
import re
import os


class RCAReader:
    """
    The class to read the RCA text files and clean the text data
    """

    def __init__(self):
        pass

    def clean_text(self, text: str) -> str:
        """
        Clean the text by removing the special characters and extra spaces

        Args:
            text (str): The text to clean

        Returns:
            str: The cleaned text
        """
        # Remove the extra spaces
        cleaned_text = re.sub(r"\s+", " ", text)
        cleaned_text = re.sub(r"\n+", "\n", cleaned_text)

        return cleaned_text

    def read_rca(self, rca_folder_path: str) -> dict[str, str]:
        """
        Read the RCA text files from the given folder

        Args:
            rca_folder_path (str): The folder containing the RCA text files

        Returns:
            dict[str, str]: The RCA text file names as keys and the RCA text as values
        """
        rca_files = os.listdir(rca_folder_path)
        rca_texts = {}

        for rca_file in rca_files:
            # Skip the hidden files and folders
            full_path: str = os.path.join(rca_folder_path, rca_file)
            if rca_file.startswith(".") or os.path.isdir(full_path):
                continue
            with open(full_path, "r", encoding="unicode_escape") as file:
                content = self.try_read_file(file)
                if content and content.strip():
                    rca_texts[rca_file] = self.clean_text(content)
        return rca_texts

    def try_read_file(self, file: TextIOWrapper) -> str:
        """
        Try to read the file, if there is any error, return an empty string

        Args:
            file (TextIOWrapper): The file to read

        Returns:
            str: The content of the file if read successfully, else an empty string
        """
        try:
            return file.read()
        except UnicodeDecodeError:
            print(f"Error reading file {file}")
            return ""
