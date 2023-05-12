import math
import random
from app import file_io
from app import stats
from app.config import Config
from app.stats import Statistics
import pandas as pd


class SampleGenerator:

    @classmethod
    def clear_old_samples(cls):
        file_io.FileInteractor.clear_output_dir()

    @classmethod
    def get_input_pop(cls):
        df = file_io.FileInteractor.read_input_data_file().loc[:, "pop"]
        return df

    @classmethod
    def process_file(cls, sample_file, ss):
        sample_full_path = file_io.FileInteractor.get_sample_file_path(sample_file)

        popdf = cls.get_input_pop()
        data_count = popdf.shape[0]
        data_min = popdf.min()
        data_max = popdf.max()

        sample_list = []
        for i in range(ss):
            r = random.randrange(0, data_count)
            while r in sample_list:
                r = random.randrange(0, data_count)
            sample_list.append(r)

        sample_list.sort()

        original_df = file_io.FileInteractor.read_input_data_file()
        chosen_df = pd.DataFrame(columns=['state', 'pop'])

        for i in original_df.index:
            p = original_df['pop'][i]
            s = original_df['state'][i]
            item = str(s) + ", " + str(p)
            if p == data_min or p == data_count:
                df_new_row = pd.DataFrame({'state': [s], 'pop': [p]})
                chosen_df = pd.concat([chosen_df, df_new_row])
            elif i in sample_list:
                df_new_row = pd.DataFrame({'state': [s], 'pop': [p]})
                chosen_df = pd.concat([chosen_df, df_new_row])

        file_io.FileInteractor.write_to_file(sample_full_path, chosen_df)

    @classmethod
    def get_sample_size(cls, z_score, moe, pop_size):
        # Note use .5 standard deviation instead of the actual standard deviation to calculate the sample size
        stddev = 0.5
        size_num = round(((pow(z_score, 2)) * (stddev * (1 - stddev))) / (pow(moe, 2)), Config.rounding_precision)
        size_den = round((1 + (((pow(z_score, 2)) * (stddev * (1 - stddev))) / ((pow(moe, 2)) * pop_size))),
                         Config.rounding_precision)

        size = math.floor((size_num / size_den))

        return size

    @classmethod
    def sample_processor(cls):
        pop = cls.get_input_pop()
        pop_size = pop.shape[0]
        moe = Config.margin_of_error
        z_score = Config.z_scores

        # Clear output directory
        file_io.FileInteractor.clear_output_dir()

        for m in moe:
            for z in z_score:
                sample_size = cls.get_sample_size(z, m, pop_size)
                sample_file = "sample_data_number_" + str(z) + "_" + str(m) + "_" + str(sample_size) + ".csv"
                cls.process_file(sample_file, sample_size)
