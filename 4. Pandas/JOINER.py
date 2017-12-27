
def JOINER(*args, **kwargs):
    """
    """
    joined =[]
    col_list = [x.columns.tolist() for x in args]
    pk = reduce(lambda x, y: np.intersect1d(x, y), col_list).tolist()
    
    if bool(pk):
        list_of_dfs = map(lambda df: df.set_index(pk), args)
        joined = list_of_dfs[0].join(list_of_dfs[1:])    
    else:
        print "There are no common columns to join."
        
    return joined