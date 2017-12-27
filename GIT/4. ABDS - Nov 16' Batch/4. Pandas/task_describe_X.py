
def DESCRIBE_X(s=Series(), perc=[]):
    """
    
    """
    s1 = Series({'MIN': s.min(), 
                 'MAX': s.max(), 
                 'SUM': s.sum(), 
                 'MEAN': s.mean(), 
                 'MISSINGS': s.isnull().sum(), 
                 'NONMISSINGS': s.notnull().sum(),
                 'SKEW': s.skew(), 
                 'KURT': s.kurtosis()})
    s2 = s.quantile(perc)
    return pd.concat([s1, s2])