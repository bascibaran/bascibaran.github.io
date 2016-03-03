import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats
import matplotlib.patches as mpatches
import mpld3
import json

# import our data as a pandas dataframe
print("reading cat_data.csv as a pandas dataframe.")
cat = pd.read_csv("cat_data.csv")

# So we have a pandas dataframe
# Time to go bananas?!
# As we have seen from our forays in the terminal,
# that the csv can be very large, and thus make it very difficult
# for us to analyze the whole population in one go.
# thus the motivation to perform sampling statistics on our data.

## get a vector of the data_size column for initial univariate analysis.
print("extracting size vector")
sizeVec = cat["data_size"]
mean = sizeVec.mean()
median = sizeVec.median()

## write sizevec file for vega visualisation....
#print("writing size vector to sizevec.csv")
#np.savetxt("sizevec.csv", sizeVec)

## grab time 
print("extracting time vector")
timeVec = cat["min"]
## and write it
#print("writing timevector to timevec.csv")
#np.savetxt("timevec.csv",timeVec)

# now we have size and time vectors. 
# use mpld3 to convert matplotlib visualisations
# to d3 objects we can embed into web pages. 
print("creating matplotlib plot for sizeVec")
sizehist = plt.hist(sizeVec, bins=np.logspace(0,15, 200))
plt.xscale('log')
plt.axvline(x=mean, lw=2, color='red')
plt.axvline(x=median, lw=2, color='green')
meanlabel = mpatches.Patch(color='red', label='mean')
medianlabel = mpatches.Patch(color='green', label='median')
plt.legend(handles=[meanlabel,medianlabel])
plt.xlabel("data size (bytes)")
plt.ylabel("frequency")
plt.title("histogram of data size of data on irods-db3 (200 bins)")
sizefig = plt.gcf()
# lets try parsing the figure as a python dict using mpld3
# and then using the json library to parse the dict as a json object
# which we will then use vega to visualize.
#print("parsing matplotlib hist for size to a dictionary") 
#sizeDict = mpld3.fig_to_dict(sizefig)


#print("opening out file for writing...")
#sizeOut = open("size.json",'w')
#print("writing size dict to size.json")
#json.dump(sizeDict, sizeOut)
#sizeOut.close()

print("parsing size vector to html")
# other method is using mpld3's capacity for parsing a figure as an html representation...
sizehtml = mpld3.fig_to_html(sizefig)
sizeOut = open("size.html",'w')
sizeOut.write(sizehtml)
sizeOut.close()

