# import our data as a pandas dataframe
print("reading cat_data.csv as a pandas dataframe.")
cat = pd.read_csv("cat_data.csv")

timeVec = cat['min']
