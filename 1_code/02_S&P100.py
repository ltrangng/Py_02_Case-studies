# S&P 100 COMPANIES

# The S&P100 dataset
# S&P 100 is a stock market index made up of 100 major companies in the US in multiple industries.
# Import libraries and lists
import numpy as np
import matplotlib.pyplot as plt
names = open("0_data/names.csv", "r").read().split("," )
sectors = open("0_data/sectors.csv", "r").read().split(",")
prices = open("0_data/prices.csv", "r").read().split(",")
prices = [float(x) for x in prices]
earnings = open("0_data/earnings.csv", "r").read().split(",")
earnings = [float(x) for x in earnings]
# Convert lists into arrays
names_array = np.array(names)
sectors_array = np.array(sectors)
prices_array = np.array(prices)
earnings_array = np.array(earnings)
# Calculate P/E ratio
pe = prices_array / earnings_array 
print(pe)

# Filtering arrays
# Filter elements in sectors that are 'Information Technology'
boolean_array = (sectors_array == "Information Technology")
it_names = names_array[boolean_array]
it_pe = pe[boolean_array]
print(it_names)
print(it_pe)
# Filter for the Consumer Staples sector
cs_names = names_array[(sectors_array == "Consumer Staples")]
cs_pe = pe[(sectors_array == "Consumer Staples")]
print(cs_names)
print(cs_pe)

# Summarize sector data
it_pe_mean = np.mean(it_pe)
it_pe_std = np.std(it_pe)
print(it_pe_mean)
print(it_pe_std)
print(np.mean(cs_pe))
print(np.std(cs_pe))

# Plot P/E ratios
# Assign each company a numeric ID
it_id = range(0, 15)
cs_id = range(0, 12)
# Make a scatterplot
plt.scatter(it_id, it_pe, color = "red", label = "IT")
plt.scatter(cs_id, cs_pe, color = "green", label = "CS")
# Add legend
plt.legend()
# Add labels
plt.xlabel("Company ID")
plt.ylabel("P/E Ratio")
plt.show()
# Use histogram to understand the distribution of the P/E ratios
plt.hist(it_pe, bins = 8)
plt.xlabel("P/E ratio")
plt.ylabel("Frequency") 
plt.show() 
# Name the outlier
outlier_price = it_pe[it_pe > 50]
outlier_name = it_names[it_pe > 50]
# Display the result
print("In 2017, " + str(outlier_name[0]) + "had an abnormally high P/E ratio of " + str(round(outlier_price[0], 2)) + ".")