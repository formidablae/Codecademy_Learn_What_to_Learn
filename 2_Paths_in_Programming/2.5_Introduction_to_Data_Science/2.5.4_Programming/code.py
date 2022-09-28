# Welcome to the behind-the-scenes code!
# Feel free to look through this file, but don't worry if you don't understand something. You'll learn how to do all of this in later courses.

# Import libraries for making and displaying figures

import matplotlib.pyplot as plt
import codecademylib3_seaborn
import pandas as pd

# Import a package for generating a model of a dataset

from sklearn.cluster import KMeans

# Load the three penguin species data

adelie = pd.read_csv('adelie.csv')
adelie['Species'] = 'Adelie'
gentoo = pd.read_csv('gentoo.csv')
gentoo['Species'] = 'Gentoo'
chinstrap = pd.read_csv('chinstrap.csv')
chinstrap['Species'] = 'Chinstrap'

# Combine the three datasets into one and select relevant columns

penguins = pd.concat([adelie,gentoo,chinstrap])[['Species','Flipper Length (mm)','Culmen Length (mm)']]

# Rename the columns for ease of use

penguins.columns = ['Species','Flipper Length','Bill Length']

# Create and label the scatterplots

for penguin in ['Adelie','Gentoo','Chinstrap']:
    plt.scatter(penguins[penguins['Species'] == penguin]['Flipper Length'],penguins[penguins['Species']==penguin]['Bill Length'],alpha=.75,linewidths=.5,label=penguin)
plt.legend()
plt.xlabel('Flipper Length (mm)')
plt.ylabel('Bill Length (mm)')
plt.title('Penguin Flippers and Bills by Species')


# Create a model of this data using the K Means algorithm

km_model = KMeans(n_clusters = 3, random_state=17).fit(penguins[['Flipper Length','Bill Length']].dropna().values)

# Define a function that uses the KMeans model to predict species

def predict(flipper,bill):
    #plt.scatter(flipper,bill,marker='*',s=600,c='black')
    species_name = {0:'Adelie',1:'Gentoo',2:'Chinstrap'}
    print('Prediction: this penguin belongs to the ' + species_name[list(km_model.predict([[flipper,bill]]))[0]] + ' species!')
    plt.show()
