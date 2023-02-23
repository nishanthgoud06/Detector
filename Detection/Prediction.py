import pandas as pd
import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import RandomForestClassifier
def detection(training,testing):
    print("Preprocessing")
    datacols = ["duration","protocol_type","service","flag","src_bytes",
    "dst_bytes","land","wrong_fragment","urgent","hot","num_failed_logins",
    "logged_in","num_compromised","root_shell","su_attempted","num_root",
    "num_file_creations","num_shells","num_access_files","num_outbound_cmds",
    "is_host_login","is_guest_login","count","srv_count","serror_rate",
    "srv_serror_rate","rerror_rate","srv_rerror_rate","same_srv_rate",
    "diff_srv_rate","srv_diff_host_rate","dst_host_count","dst_host_srv_count",
    "dst_host_same_srv_rate","dst_host_diff_srv_rate","dst_host_same_src_port_rate",
    "dst_host_srv_diff_host_rate","dst_host_serror_rate","dst_host_srv_serror_rate",
    "dst_host_rerror_rate","dst_host_srv_rerror_rate","attack", "last_flag"]

    # Load NSL_KDD train dataset
    dfkdd_train = pd.read_table(training, sep=",", names=datacols) # change path to where the dataset is located.
    dfkdd_train = dfkdd_train.iloc[:,:-1] # removes an unwanted extra field
    #print("train=",dfkdd_train)

    # Load NSL_KDD test dataset
    dfkdd_test = pd.read_table(testing, sep=",", names=datacols)
    dfkdd_test = dfkdd_test.iloc[:, :-1]


    mapping = {'ipsweep': 'Probe', 'satan': 'Probe', 'nmap': 'Probe', 'portsweep': 'Probe', 'saint': 'Probe',
               'mscan': 'Probe',
               'teardrop': 'DoS', 'pod': 'DoS', 'land': 'DoS', 'back': 'DoS', 'neptune': 'DoS', 'smurf': 'DoS',
               'mailbomb': 'DoS',
               'udpstorm': 'DoS', 'apache2': 'DoS', 'processtable': 'DoS',
               'perl': 'U2R', 'loadmodule': 'U2R', 'rootkit': 'U2R', 'buffer_overflow': 'U2R', 'xterm': 'U2R',
               'ps': 'U2R',
               'sqlattack': 'U2R', 'httptunnel': 'U2R',
               'ftp_write': 'R2L', 'phf': 'R2L', 'guess_passwd': 'R2L', 'warezmaster': 'R2L', 'warezclient': 'R2L',
               'imap': 'R2L',
               'spy': 'R2L', 'multihop': 'R2L', 'named': 'R2L', 'snmpguess': 'R2L', 'worm': 'R2L',
               'snmpgetattack': 'R2L',
               'xsnoop': 'R2L', 'xlock': 'R2L', 'sendmail': 'R2L',
               'normal': 'Normal'
               }

    dfkdd_train['attack_class'] = dfkdd_train['attack'].apply(lambda v: mapping[v])
    dfkdd_test['attack_class'] = dfkdd_test['attack'].apply(lambda v: mapping[v])

    dfkdd_train.drop(['attack'], axis=1, inplace=True)
    dfkdd_test.drop(['attack'], axis=1, inplace=True)

    #'num_outbound_cmds' field has all 0 values, so drop it
    dfkdd_train.drop(['num_outbound_cmds'], axis=1, inplace=True)
    dfkdd_test.drop(['num_outbound_cmds'], axis=1, inplace=True)

    print("Normalization")
    #Normalization
    from sklearn.preprocessing import StandardScaler
    scaler = StandardScaler()
    cols = dfkdd_train.select_dtypes(include=['float64', 'int64']).columns
    sc_train = scaler.fit_transform(dfkdd_train.select_dtypes(include=['float64', 'int64']))
    sc_test = scaler.fit_transform(dfkdd_test.select_dtypes(include=['float64', 'int64']))
    sc_traindf = pd.DataFrame(sc_train, columns=cols)
    sc_testdf = pd.DataFrame(sc_test, columns=cols)
    #print(sc_traindf.head())
    #print(sc_testdf.head())

    print("Feature Selecction")
    #Feature Selecction
    feature_select = ['duration','src_bytes', 'dst_bytes', 'logged_in', 'count', 'srv_count', 'dst_host_srv_count',
                      'dst_host_diff_srv_rate', 'dst_host_same_src_port_rate', 'dst_host_serror_rate']

    print("Prediction")
    x_train=sc_traindf[feature_select]
    y_train=dfkdd_train['attack_class']
    x_test=sc_testdf[feature_select]
    nn = MLPClassifier(hidden_layer_sizes=(3),max_iter=50)#RandomForestClassifier()#MLPClassifier(); # Creation of ANN classifier
    nn.fit(x_train, y_train); # fit ANN classifier on the training set
    result=nn.predict(x_test) # Prediction of ANN
    return result
    '''refclasscol = pd.concat([sc_traindf], axis=1).columns
    from sklearn.feature_selection import RFE
    import itertools
    rfc = RandomForestClassifier()

    #create the RFE model and select 10 attributes
    rfe = RFE(rfc, n_features_to_select=10)
    rfe = rfe.fit(x, y)
    # summarize the selection of the attributes
    feature_map = [(i, v) for i, v in itertools.zip_longest(rfe.get_support(), refclasscol)]
    selected_features = [v for i, v in feature_map if i == True]
    print(selected_features)'''
    #feature_select=['src_bytes','dst_bytes','logged_in','count','srv_count','dst_host_srv_count','dst_host_diff_srv_rate','dst_host_same_src_port_rate','dst_host_serror_rate']


#print(detection("KDDTrain.txt","testing.txt"))