import glob
import os
import pandas as pd
from app.config import Config
from app.file_ops.__init__ import FileOperations


class FileInteractor:

    @classmethod
    def read_input_data_file(cls):
        input_file_path = FileOperations.get_calculate_file_path(Config.data_directory, Config.data_file_name)
        input_df = pd.read_csv(input_file_path)
        return input_df

    @classmethod
    def get_output_dir(cls):
        output_dir = FileOperations.get_project_root_directory() + "sample_files_output/"
        return output_dir

    @classmethod
    def get_sample_file_path(cls, sample_file):
        sample_path = FileOperations.get_calculate_file_path("sample_files_output", sample_file)
        return sample_path

    @classmethod
    def clear_output_dir(cls):
        output_dir = cls.get_output_dir()
        pattern = output_dir + "sample_data_*.csv"
        for f in glob.iglob(pattern):
            os.remove(f)
        return 0

    @classmethod
    def write_to_file(cls, file_path, df):
        df.to_csv(file_path, mode='a', index=False, header=['state', 'pop'])
        return 0

    @classmethod
    def create_file(cls, file_path):
        f = open(file_path, "x")
        f.close()
        return 0
