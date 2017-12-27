
# IMPORT THE DATA

u_cols = ['user_id', 'age', 'sex', 'occupation', 'zip_code']
users = pd.read_csv(path + 'Data/Data/u.user', sep='|', names=u_cols)

r_cols = ['user_id', 'movie_id', 'rating', 'unix_timestamp']
ratings = pd.read_csv(path + 'Data/Data/u.data', sep='\t', names=r_cols)

# Load only the first five columns of the movies file with usecols
m_cols = ['movie_id', 'title', 'release_date', 'video_release_date', 'imdb_url']
movies = pd.read_csv(path + 'Data/Data/u.item', sep='|', names=m_cols, usecols=range(5))

# MERGE ALL THE DATA 
movie_ratings = pd.merge(movies, ratings)

lens = pd.merge(movie_ratings, users)

lens.head()