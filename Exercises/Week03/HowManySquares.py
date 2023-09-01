# How many squares do we have to add up to exceed 1e6?
# (An illustration of a while loop)

cumulativeSum=0
counter=0

while cumulative_sum<1000000:
    counter = counter + 1
    cumulative_sum=cumulative_sum+(counter**2)

print("The answer is", str(counter))
