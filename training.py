# Build Simple model for practice with Docker and AWS

import pandas as pd

from sklearn.datasets import load_boston
from sklearn.ensemble import RandomForestRegressor
from sklearn.externals import joblib

data = load_boston()
features = data['data'][:, [5, 12]]
target = data['target']
features = pd.DataFrame(features, columns=['RM', 'LSTAT'])

rf = RandomForestRegressor(n_jobs=-1, n_estimators=1000, max_depth=10)
rf = rf.fit(target, features)
joblib.dump(rf, 'model.pkl')
