
# Distribution of users by age
users['age'].hist(bins=30, color='k', alpha=0.7)
plt.title('Count of Users (y-axis) by Age Groups (x-axis)')

# Binning users into age groups
bins = ['0-9', '10-19', '20-29', '30-39', '40-49', '50-59', '60-69', '70-79']

# Create a new column
lens['age_group'] = pd.cut(lens.age, range(0, 81, 10), right=False, labels=bins)

# Check if binning went okay
print lens[['age', 'age_group']].drop_duplicates()[:10]

%%timeit 

# Method 1
pd.pivot_table(data=lens.loc[lens.title.isin(voted_100), :], 
               index='title', 
               columns='age_group', 
               values='rating', 
               aggfunc=np.mean).std(axis=1).sort_values(ascending=False)

%%timeit

# Method 2
(lens
 .loc[lens.title.isin(voted_100), :]
 .groupby(['title', 'age_group'])
 .apply(lambda x: x.rating.mean())
).unstack().std(axis=1).sort_values(ascending=False)

### Using `unstack` to convert ***long-to-wide*** data

age_group_ratings = allRatings_50most.reset_index().groupby(['title', 'age_group']).apply(avg_score)['mean_rating'].unstack(1).fillna(0)[10:20]
age_group_ratings.head()

# A high standard deviation in ratings across groups means that the different age groups gave ratings far from the mean
# I'm ignoring the ratings of the 0-9 and 80-89 age groups because they pollute the results.
most_controversial = np.std(age_group_ratings.ix[:, 1:7], axis=1).order(ascending=False)
most_controversial.head()

age_group_ratings.ix[most_controversial.index]