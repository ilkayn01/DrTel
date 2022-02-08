from sklearn.preprocessing import MinMaxScaler
features = res.copy()
features = features.drop(['insurance', 'maxJerk', 'meanSpeed', 'meanAcc', 'medianAcc'], axis = 1)

log_list = features.columns.to_list()#['tripDistance', 'maxAcc', 'speedingUrban', 'turno', 'stopNo', 'speed', 'jerkCount', 'medianSpeed', 'speedingHighway']
mmscaler = MinMaxScaler()
features[log_list] = mmscaler.fit_transform(features[log_list])
#features[log_list] = np.log(features[log_list])

#from numpy import inf
#features[features == inf] = 0
#features[features == np.nan] = 0

X, y = features, res.insurance
print(X.shape, y.shape)

from sklearn.model_selection import train_test_split
# split into train test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.77, random_state=42)
