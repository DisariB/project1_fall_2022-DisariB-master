class Statistics:
    """Calculates summary statistics of state_population DF"""

    @staticmethod
    def pop_count(df):
        record_count = df['pop'].shape[0]
        return record_count

    @staticmethod
    def pop_min(df):
        minimum = df['pop'].min()
        return minimum

    @staticmethod
    def pop_max(df):
        maximum = df['pop'].max()
        return maximum

    @staticmethod
    def pop_mean(df):
        mean = df['pop'].mean()
        return mean

    @staticmethod
    def pop_med(df):
        median = df['pop'].median()
        return median

    @staticmethod
    def pop_mode(df):
        mode = df['pop'].mode()
        return mode

    @staticmethod
    def pop_std_dev(df):
        std_dev = df['pop'].std()
        return std_dev
