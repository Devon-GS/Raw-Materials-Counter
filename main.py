import pandas as pd

ingrediants_filtered = []

ingrediants = {}

# Load in receipes
df = pd.read_excel('Receipe.xlsx', na_values=None,keep_default_na=True)

# Change nan to None 
df_na = df.fillna('None')

# Get needed column info
data = df_na.iloc[:, [0, 2, 3]].values.tolist()

# Put ingredients into dic (ingrediants)
for x in data:
    if x[0] != 'None':
        ingrediants_filtered.append(x)
        
# Add Raw ingrediants to dic        
for x in ingrediants_filtered:
    ingrediants[x[1]] = 0.0


# Get items made
made = [['2000000000015', '5'], ['2000000000480', '2']]

for x in made:
    print(x)





    # for y in ingrediants_filtered:
    #     # print(x[0], int(y[0]))
    #     if x[0] == int(y[0]):
    #         # print(y[0])
    #         ingrediants[y[1]] += float(y[2]) * float(x[1])
    
# print(ingrediants)    