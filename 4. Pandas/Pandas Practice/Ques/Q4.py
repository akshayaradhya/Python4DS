
pivoted=pd.pivot_table(lens,
            index=['movie_id','title'],
            columns=['sex'],
            values='rating',
            aggfunc=np.mean,
            fill_value=0)

pivoted['diff'] = pivoted.M - pivoted.F

pivoted = pivoted.reset_index().set_index('title').ix[most_50.index].sort('diff', ascending=False)

print pd.concat([pivoted.head(), pivoted.tail()])

pd.concat([pivoted.head(), pivoted.tail()])[['diff']].plot(kind='bar', title='Men vs. Women', )