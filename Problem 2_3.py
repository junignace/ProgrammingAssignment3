import pandas as pd

K = pd.read_csv('cars.csv')

A = K.iloc[[0,1,2,3,4],[0,2,4,6,8]]
B = K.loc[K['Model'] == 'Mazda RX4', :]
C= K.loc[K['Model'] == 'Camaro Z28', ['Model','cyl']]
tempE1 = K.loc[K['Model'] == 'Mazda RX4 Wag', ['Model','cyl', 
               'gear']]

tempE2=K.loc[K['Model'] == 'Ford Pantera L', ['Model','cyl', 
             'gear']]

tempE3= K.loc[K['Model'] == 'Honda Civic', ['Model', 'cyl', 
              'gear']]

tempE4 = tempE1.append(tempE2)

D= tempE4.append(tempE3)