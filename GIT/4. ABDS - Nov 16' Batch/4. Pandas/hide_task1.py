
titanic = pd.read_csv('train.csv')

# Shape and data types
print titanic.shape
print
print titanic.dtypes
print
print titanic.get_dtype_counts()

# retain only the passengers that survived
survivors = titanic.loc[titanic.Survived == 1, :]
print survivors.shape
print survivors[['Age', 'Fare']].describe()

# Subset the data to retain only Female passengers.
# Find out how many females over the age of 30 survived.
survivors.loc[(survivors.Sex == 'female') & (survivors.Age > 30), :].shape[0]

# Are there any missing values in the Age column?
print titanic.Age.isnull().sum()

# Draw a histogram of this column.
titanic.Age.hist()
titanic.Age.plot.hist()
titanic.Age.plot(kind='hist')

# Replace missing values with 
# a) Mean
titanic.Age.fillna(titanic.Age.mean())

# b) Median
titanic.Age.fillna(titanic.Age.median())

# Report the new summary statistics on this variable
pd.concat([titanic.Age.describe(),
           titanic.Age.fillna(titanic.Age.mean()).describe(),
           titanic.Age.fillna(titanic.Age.median()).describe(),
           titanic.Age.fillna(0).describe()], axis=1)