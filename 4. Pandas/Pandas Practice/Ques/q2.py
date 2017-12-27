
# movies with over 100 votes
voted_100 = lens['title'].value_counts()[lens['title'].value_counts() > 150].index.tolist() 

(lens[lens.title.isin(voted_100)]
 .groupby('title')
 .apply(lambda x: x['rating'].mean())
 .sort_values(ascending=False)[:10])