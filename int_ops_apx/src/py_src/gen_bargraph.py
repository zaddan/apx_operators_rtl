import numpy as np
import matplotlib.pyplot as plt
 
# data to plot
n_groups = 3
#Traditional_delay = (1, 1, 1, 1)
duplicated = (0, 2, 4)
delay_profile = (1, 3, 5)
delay_profile_2 = (5, 6, 7)


# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.15
opacity = 0.8
 
#rects1 = plt.bar(index, Traditional, bar_width,
#                 alpha=opacity,
#                 color='b',
#                 label='Traditional')
 
rects2 = plt.bar(index , duplicated, bar_width,
                 alpha=opacity,
                 color='b',
                 label='Duplicated')
 
rects3 = plt.bar(index + bar_width, delay_profile, bar_width,
                 alpha=opacity,
                 color='g',
                 label='Delay Profile 1')
 
rects3 = plt.bar(index + 2*bar_width, delay_profile_2, bar_width,
                 alpha=opacity,
                 color='y',
                 label='Delay Profile 2')
 


plt.xlabel('Hardware Module')
plt.ylabel('Speed-up')
plt.title('Different Guardbanding Method Speed-ups')
plt.xticks(index + bar_width, ('Add', 'Mul', 'IDCT'))
plt.legend()
 
plt.tight_layout()
plt.savefig("./results_for_paper/config_performance.png")
plt.show()
