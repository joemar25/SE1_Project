'''
using pandas for visualization
'''


from gingerit.gingerit import GingerIt
import pandas as pd

parser = GingerIt()
pd.set_option('display.max_colwidth', None)

text = 'The smelt of fliwers bring back memories.'

result = parser.parse(text)
corrections = pd.DataFrame(result['corrections'])

# print(result)
print(corrections)
