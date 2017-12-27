
from sklearn.datasets import load_boston
boston_bunch = load_boston()

print boston_bunch['data'].shape

boston_bunch.keys()

DataFrame(boston_bunch['data'], columns=boston_bunch['feature_names']).dtypes

pd.concat([DataFrame(boston_bunch['data'], 
          columns=boston_bunch['feature_names']), Series(boston_bunch['target'], 
                                                         name='Target')], axis=1)[:10]