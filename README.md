# libpy
Collection of reusable python modules for data science and machine learning applications.
This will be used in the [model-training](https://github.com/remla23-team14/model-training) repo.

## libpy.data_preprocessing
Load model data from a CSV file into a pandas dataframe:
```py
def load_data(path: pathlib.Path) -> pd.DataFrame:
    pass
```

Process the data to create a corpus of review sentences:
```py
def process_data(dataset: pd.DataFrame) -> List[str]:
    pass
```
