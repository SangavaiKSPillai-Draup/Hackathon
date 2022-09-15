
def read_csv(filename): 
    from pandas import read_csv 
    df = read_csv(filename)
    return df 

def convert_df_to_json(df): 
    df2 = df.T.to_dict().values() 
    json_data = list(df2)
    return json_data