# Importing libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree

#Importing libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from pandas.plotting import parallel_coordinates

#Metrics
from sklearn import metrics
from sklearn.metrics import make_scorer, accuracy_score,precision_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score ,precision_score,recall_score,f1_score

#Model Select
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from scipy.stats import norm

 
#Datacleaning

#---------------------------------------------Datacleaning---------------------------------------------
# Read data from file into dataframe
df = pd.read_csv("drug200_dirty.csv")

# Describe data
print(df.info())

# Order by given field
df.sort_values("Age", inplace = True)

# Save dataframe to file
df.to_csv("data_WithoutDuplicates.csv",index=False)

# Define a list of strings to be treated as missing values
missing_values = ["n/a", "na", "-", "--"]
# Read the CSV file into a DataFrame, treating the specified missing values as NaN
df = pd.read_csv("data_WithoutDuplicates.csv",na_values = missing_values)


# Delete rows where Date is missing
df.dropna(subset=['Sex'], inplace=True)
print(df.isnull().sum())

df.dropna(subset=['BP'], inplace=True)
print(df.isnull().sum())

df.dropna(subset=['Cholesterol'], inplace=True)
print(df.isnull().sum())

df.dropna(subset=['Drug'], inplace=True)
print(df.isnull().sum())


# Replace missing and incorrect Age,Na_to_K  values using median
median = df['Age'].median()
df['Age'].fillna(median, inplace=True)
print(df.isnull().sum())

median = df['Na_to_K'].median()
df['Na_to_K'].fillna(median, inplace=True)
print(df.isnull().sum())


# Visualizing data
plt.style.use('ggplot')

fig, ax = plt.subplots()
ax.boxplot((df['Age'], df['Na_to_K']), vert=False, showmeans=True, meanline=True,
           labels=('Age','Na_to_K'), patch_artist=True,
           medianprops={'linewidth': 2, 'color': 'purple'},
           meanprops={'linewidth': 2, 'color': 'red'})
plt.show()

# Check Age with histogram
hist, bin_edges = np.histogram(df['Age'], bins=10)
fig, ax = plt.subplots()
ax.hist(df['Age'], bin_edges, cumulative=False)
ax.set_xlabel('Age')
ax.set_ylabel('Frequency')
plt.show()

# Replace outlier value with median
median = df['Age'].median()
df.replace(to_replace=max(df['Age']), value=median, inplace=True)

median = df['Na_to_K'].median()
df.replace(to_replace=max(df['Na_to_K']), value=median, inplace=True)



# Save dataframe to file
df.to_csv("data_cleaned.csv",index=False)

df = pd.read_csv("data_cleaned.csv")
# Draw histogram for each numeric variable
# Normal distribution over histogram
# List of all attributes
all_attributes = ['Age', 'Sex', 'BP', 'Cholesterol', 'Na_to_K', 'Drug']

# Use label encoding for non-numeric attributes
label_encoder = LabelEncoder()
attributes = ['Age','Na_to_K']
for attr in all_attributes:
    label_mapping=df[attr].unique()
    print(label_mapping)
    if df[attr].dtype == 'object':
        # For non-numeric attributes, use label encoding
        df[attr] = label_encoder.fit_transform(df[attr])
        tick_marks = np.arange(len(label_mapping))
        plt.xticks(tick_marks, label_mapping, rotation=45)
    
    # Fit a normal distribution to the data:
    # mean and standard deviation
    mu, std = norm.fit(df[attr])
    # Plot the histogram
    plt.hist(df[attr], bins=10, density=True, alpha=0.6, color='b')
    # Plot density function over histogram
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = norm.pdf(x, mu, std)
    plt.plot(x, p, 'k', linewidth=2)
    title = "Fit Values: {:.2f} and {:.2f}".format(mu, std)
    plt.title(attr)
    plt.show()

#------------------------------------------------Analyze-----------------------------------------------

# Reading the dataset
data = pd.read_csv("data_cleaned.csv")
print(data.head())
print(data.nunique())
print(data.describe(include='all'))
data.info()

# Feature selection
X = data.iloc[:,0:5].values  #
y = data.iloc[:,5].values  # 


# Label encoding for X
le_X1=LabelEncoder()
le_X2 = LabelEncoder()
le_X3=LabelEncoder()
X[:, 1] = le_X1.fit_transform(X[:, 1])  # Encoding Sex
X[:, 2] = le_X2.fit_transform(X[:, 2])  # Encoding BP
X[:, 3] = le_X3.fit_transform(X[:, 3])  # Encoding Cholesterol

# Label encoding for Y
le = LabelEncoder()
y = le.fit_transform(y)

# Splitting the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
#Explore the TRAINING data
train = pd.DataFrame(X_train)
train2=pd.DataFrame(y_train)
#Create histograms for each feature
n_bins = 10
fig, axs = plt.subplots(2, 2)

#Put back original labes to histograms
Age_labels=data['Age'].unique()
Sex_labels = data['Sex'].unique()
BP_labels=data['BP'].unique()
Cholesterol_labels = data['Cholesterol'].unique()
Na_to_K_labels=data['Na_to_K'].unique()
DrugLabel=data['Drug'].unique()
axs[0, 0].hist(train.iloc[:, 3].values, bins=n_bins)
axs[0, 0].set_title('Cholesterol')
axs[0, 0].set_xticks(range(len(Cholesterol_labels)))
axs[0, 0].set_xticklabels(Cholesterol_labels, rotation=45, ha='right')  # Adjust rotation and ha as needed
axs[0, 1].hist(train.iloc[:, 1].values, bins=n_bins)
axs[0, 1].set_title('Sex')
axs[0, 1].set_xticks(range(len(Sex_labels)))
axs[0, 1].set_xticklabels(Sex_labels, rotation=45, ha='right')  # Adjust rotation and ha as needed
axs[1, 0].hist(train.iloc[:, 2].values, bins=n_bins)
axs[1, 0].set_title('Blood Pressure')
axs[1, 0].set_xticks(range(len(BP_labels)))
axs[1, 0].set_xticklabels(BP_labels, rotation=45, ha='right')  # Adjust rotation and ha as needed
axs[1, 1].hist(train2.iloc[:, 0].values, bins=n_bins)
axs[1, 1].set_title('Drug')
axs[1, 1].set_xticks(range(len(DrugLabel)))
axs[1, 1].set_xticklabels(DrugLabel, rotation=45, ha='right')  # Adjust rotation and ha as needed
# add some spacing between subplots
fig.tight_layout(pad=1.0)
plt.show()

train['Drug'] = pd.DataFrame(y_train)
"""
print(train.columns)
sns.pairplot(train, hue="Drug", height = 2, palette = 'colorblind')
plt.show()
"""

#Correlation Matrix
custom_labels=['Age','Sex','BP','Cholesterol','Na_to_K','Drug']
plt.figure(figsize=(15, 15))
sns.heatmap(train.corr(),xticklabels=custom_labels,yticklabels=custom_labels, annot=True)
plt.title('Correlation Matrix')
plt.show()

# Print the correlation matrix
print("Correlation Matrix:")
print(train.corr())


# Decision Tree
mod_dt = DecisionTreeClassifier()
mod_dt.fit(X_train, y_train)
prediction = mod_dt.predict(X_test)

# Print accuracy
print('The accuracy of the Decision Tree is', "{:.3f}".format(metrics.accuracy_score(prediction, y_test)))

# Print the importance of each predictor
print(mod_dt.feature_importances_)

# Print text representation
text_representation = tree.export_text(mod_dt)
print(text_representation)

# Save to file
with open("decision_tree.log", "w") as fout:
    fout.write(text_representation)


# Visualization of decision tree
plt.figure(figsize=(10, 8))
plot_tree(mod_dt, filled=True)
plt.show()

# Confusion matrix for displaying prediction results
cm = metrics.confusion_matrix(y_test, prediction)
print("Confusion matrix\n", cm)
#plt.imshow(cm, cmap='binary')

# Plot the confusion matrix with labels
plt.imshow(cm, cmap='binary', interpolation='nearest')
plt.title('Confusion Matrix')
plt.colorbar()

#classes = ['drugA', 'drugB', 'drugC', 'drugX', 'DrugY'] # Replace with your class labels
classes = data['Drug'].unique()
print(classes)

# Add labels to the plot
tick_marks = np.arange(len(classes))
plt.xticks(tick_marks, classes, rotation=45)
plt.yticks(tick_marks, classes)

# Add numerical values in each cell
for i in range(len(classes)):
    for j in range(len(classes)):
        plt.text(j, i, format(cm[i, j], 'd'),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > cm.max() / 2 else "black")

#plt.ylabel('True label')
#plt.xlabel('Predicted label')
plt.show()

#------------------------------------------------------------------------------------------------------