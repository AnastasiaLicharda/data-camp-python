import matplotlib.pyplot as plt

year = [1950, 1970, 1990, 2010]
pop = [2.519, 3.692, 5.263, 6.972]

year = [1800, 1850, 1900] + year
pop = [1.0, 1.262, 1.650] + pop

plt.plot(year, pop)
plt.xlabel('Year')
plt.ylabel('Population')
plt.title('World population grow')
plt.yticks([0,1,2,3,4,5,6,7], ['0', '1B', '2B', '3B', '4B', '5B', '6B', '7B'])
plt.show()

plt.scatter(year, pop)
plt.xlabel('Year')
plt.ylabel('Population')
plt.title('World population grow')
plt.yticks([0,1,2,3,4,5,6,7], ['0', '1B', '2B', '3B', '4B', '5B', '6B', '7B'])
plt.show()