import unittest
import pandas as pd
import os
from refactored_code import classify_theses, process_file, process_files, save_classified_theses_to_excel

class TestRefactoredCode(unittest.TestCase):

    def setUp(self):
        self.ods = {
            'ODS1': pd.DataFrame({'ODS1': ['palavra1', 'palavra2']}),
            'ODS2': pd.DataFrame({'ODS2': ['palavra3', 'palavra4']})
        }
        self.teses = pd.DataFrame({'palavras_chave': ['palavra1 palavra2', 'palavra3 palavra4', 'palavra5 palavra6']})
        self.file_paths = {
            'file1': 'path/to/file1',
            'file2': 'path/to/file2'
        }
        self.new_folder = 'path/to/new/folder'

    def test_classify_theses(self):
        result = classify_theses(self.ods, self.teses)
        expected = {'ODS1': [0], 'ODS2': [1]}
        self.assertEqual(result, expected)

    def test_process_file(self):
        # Use a real file path for testing
        df = process_file('file1', 'path/to/file1', self.new_folder)
        self.assertIsInstance(df, pd.DataFrame)

    def test_process_files(self):
        # Use real file paths for testing
        dfs = process_files(self.file_paths, self.new_folder)
        self.assertIsInstance(dfs, dict)
        for df in dfs.values():
            self.assertIsInstance(df, pd.DataFrame)

    def test_save_classified_theses_to_excel(self):
        classified_theses = classify_theses(self.ods, self.teses)
        save_classified_theses_to_excel(classified_theses, 'classified_theses.xlsx', self.teses)
        self.assertTrue(os.path.exists('classified_theses.xlsx'))

if __name__ == '__main__':
    unittest.main()