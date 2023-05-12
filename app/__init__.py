"""This is the main startup of the app"""
from app import sample_generator


def main():
    """This is the main function that is run"""
    sample_generator.SampleGenerator.sample_processor()


if __name__ == '__main__':
    main()
