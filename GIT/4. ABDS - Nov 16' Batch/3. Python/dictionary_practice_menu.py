
diner = {'ham': 1, 'eggs': 3, 'bacon': 2, 'coffee': 1, 'toast': 0.5, 'jam': 0.2}
diner

'pancakes' in diner

diner['pancakes'] = 4

diner

diner.has_key('pancakes')

diner.has_key('latte')

'latte' in diner

'pancakes' in diner.keys()

diner.items()
# KV pairs as a list of tuples

diner.popitem()

del diner['eggs']; diner

diner.pop('bacon')

diner

### Merge dictionaries