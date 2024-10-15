import pandas as pd

def raw_materials():
    ingredients_filtered = []
    
    ingredients = {}
    
    # Load in receipes
    df_r = pd.read_excel('Assets/Receipe.xlsx', na_values=None,keep_default_na=True)
    
    # Change nan to None 
    df_r_na = df_r.fillna('None')
    
    # Get needed column info
    data = df_r_na.iloc[:, [0, 2, 3]].values.tolist()
    
    # Put ingredients into dic (ingredients)
    for x in data:
            if x[0] != 'None':
                ingredients_filtered.append(x)
                
    # Add Raw ingredients to dic        
    for x in ingredients_filtered:
        ingredients[x[1]] = 0.0
        
    # Load items made and make list 
    made = []
    
    df_m = pd.read_excel('Items_Made.xlsx', na_values=None, keep_default_na=True)
    df_m_na = df_m.fillna('None')
    df_m_data = df_m_na.iloc[:, [0, 2]].values.tolist()
    
    for x in df_m_data:
        if x[1] != 'None':
            made.append(x)
            
    # Calculate total ingredients and add to ingredient dic
    for x in made:
            for y in ingredients_filtered:
                if int(x[0]) == int(y[0]):
                    ingredients[y[1]] += float(y[2]) * float(x[1])
                    
    return ingredients

# ######################################################################
# User Interface
# ######################################################################

while True:
    print()
    
    for x, y in raw_materials().items():
        print('{:<35s} {}'.format(x, y))
        
    print()
    print('Type q to exit! or push any button to reload')
    
    user = input()
        
    if user == 'q':
        print()
        print('Exiting Program...')
        break