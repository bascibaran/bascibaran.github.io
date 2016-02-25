import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats
import matplotlib.patches as mpatches

# import our data as a pandas dataframe
print("reading cat_data.csv as a pandas dataframe.")
cat = pd.read_csv("cat_data.csv")

# So we have a pandas dataframe
# Time to go bananas?!
# As we have seen from our forays in the terminal,
# that the csv can be very large, and thus make it very difficult
# for us to analyze the whole population in one go.
# thus the motivation to perform sampling statistics on our data.

# get a vector of the data_size column for initial univariate analysis.
print("extracting size vector")
sizeVec = cat["data_size"]
mean = sizeVec.mean()
median = sizeVec.median()

# write sizevec file for vega visualisation....
np.savetxt("sizevec.csv", sizeVec);


#print("plotting")
#hgram = plt.hist(sizeVec, bins=np.logspace(0,15, 200))
#plt.xscale('log')
#plt.axvline(x=mean, lw=2, color='red')
#plt.axvline(x=median, lw=2, color='green')
#meanlabel = mpatches.Patch(color='red', label='mean')
#medianlabel = mpatches.Patch(color='green', label='median')
#plt.legend(handles=[meanlabel,medianlabel])
#plt.xlabel("data size (bytes)")
#plt.ylabel("frequency")
#plt.title("histogram of data size of data on irods-db3 (200 bins)")
#print("saving plot as png file")
#plt.savefig("datasizehist.png", bbox_inches='tight')
