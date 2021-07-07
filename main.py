import logging
import os
import time

from src.preprocess import preprocess

# ## Project Config ## #
# Log Level
logging.basicConfig(level=logging.INFO)

HERE = os.path.abspath(os.path.dirname(__file__))


def main(file_path: str):
    """
    Main Entrypoint for the feature engineering of the KickStarter dataset
    :param file_path: The local path to the dataset
    :return:
    """
    logging.info(f"Start Preprocessing for file {file_path}")
    start = time.time()
    df = preprocess(file_path)
    end = time.time()
    duration = end - start
    logging.info(f"Done pre-processing. Took {duration} seconds.")
    logging.info(df)


if __name__ == "__main__":
    file_path = os.path.join(HERE, "data", "ks-projects-201612.csv")
    main(file_path)
