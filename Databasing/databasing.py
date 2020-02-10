# Simple function that converts a pyodbc cursor to a dataframe, 
# if for some reason pd.read_sql isn't playing ball
def cur2df(cursor):
  '''Cursor is a pyodbc.connect("Conn string").cursor object'''
    df = pd.DataFrame(columns=[c[0] for c in cursor.description]) # ,
                     #dtype={c[0]:c[1] for c in cursor.description})
    row = cursor.fetchone()
    i = 1
    while row is not None:
        df.loc[i] = [ent for ent in row]
        row = cursor.fetchone()
        i += 1
    return df
