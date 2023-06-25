import pathlib
import re
from typing import List

import pandas as pd
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer


def load_data(path: pathlib.Path) -> pd.DataFrame:
    """Function to load data from a csv file"""
    dataset = pd.read_csv(
        path,
        dtype={'Review': object, 'Liked': int},
    )
    dataset = dataset[['Review', 'Liked']]
    return dataset


def process_data(dataset: pd.DataFrame) -> List[str]:
    """Function to perform some basic preprocessing on the loaded dataset"""
    ps_obj = PorterStemmer()

    all_stopwords = stopwords.words('english')
    all_stopwords.remove('not')

    corpus = []

    for i in range(0, 900):
        review = re.sub('[^a-zA-Z]', ' ', dataset['Review'][i])
        review = review.lower()
        review = review.split()
        review = [
            ps_obj.stem(word) for word in review if not word in set(all_stopwords)
        ]
        review = ' '.join(review)
        corpus.append(review)

    return corpus
