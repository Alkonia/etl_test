import os
import re
import unidecode
import importlib.util


def import_all_modules_from_folder(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith('.py') and filename != '__init__.py':
            module_name = filename[:-3]
            module_path = os.path.join(folder_path, filename)
            spec = importlib.util.spec_from_file_location(
                module_name, module_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)


def clean_column_name(col_name):
    col_name = col_name.replace("Ã±", "ñ")
    col_name = col_name.strip()
    col_name = unidecode.unidecode(col_name)
    col_name = col_name.replace(" ", "_")
    col_name = re.sub(r'[^\wÑñ]', '', col_name)
    return col_name.lower()
