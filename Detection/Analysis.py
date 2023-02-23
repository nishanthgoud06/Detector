import pandas as pd
import numpy as np
from sklearn.neural_network import MLPClassifier
from Barchart import graph
from sklearn.svm import LinearSVC
from sklearn import metrics
import warnings
import sys
from sklearn import svm
from sklearn.metrics import classification_report, f1_score, accuracy_score, confusion_matrix
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import roc_auc_score

def process(training,testing):
    print("Start Analysing...")
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

    print("Analysis")
    x_train=sc_traindf[feature_select]
    y_train=dfkdd_train['attack_class']
    x_test=sc_testdf[feature_select]
    y_test = dfkdd_test['attack_class']

    #MLPClassifier as Neural Networks
    nn = MLPClassifier(hidden_layer_sizes=(3),max_iter=50)#RandomForestClassifier()#MLPClassifier(); # Creation of ANN classifier
    nn.fit(x_train, y_train); # fit ANN classifier on the training set
    predicted_nn=nn.predict(x_test) # Prediction of ANN
    nn_ac = metrics.accuracy_score(y_test, predicted_nn) * 100
    print(nn_ac)

    # Next use SVM
    clf_svm = svm.LinearSVC()
    clf_svm.fit(x_train, y_train)
    predicted_svm = clf_svm.predict(x_test)
    svm_ac = metrics.accuracy_score(y_test, predicted_svm) * 100
    print(svm_ac)

    list = []
    list.clear()
    list.append(nn_ac)
    list.append(svm_ac)
    
    graph(list)


