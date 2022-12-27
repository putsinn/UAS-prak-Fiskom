import numpy as np
import csv
import time

from sklearn import svm
import pandas as pd

#Database: Gerbang LOgika AND
#Membaca data dari file
FileDB = 'Trapezoid.txt'
Database = pd.read_csv(FileDB, sep=",", header=0)
print(Database)

#x = Data, y=Target
X = Database[[u'a',u'b']]
y = Database.Target

#Training and Classify
clf = svm.SVC()
clf.fit(X.values,y)
print   ( clf.predict([ [1,2] ])  )
