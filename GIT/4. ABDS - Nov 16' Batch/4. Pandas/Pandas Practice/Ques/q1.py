
# Use the size method to get the count of records in each group
lens.groupby('title').size().sort_values(ascending=False)[:15]

# Aliter: 
lens['title'].value_counts()[:15]