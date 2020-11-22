import numpy as np
import scipy as sp

import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

score_input_1=np.random.lognormal(mean=0,size=100000)
score_input_2=np.random.lognormal(mean=0,size=100000)

print("First 5 samples from the array of the first input:{}".format(score_input_1[0:5]))
print("First 5 samples from the array of the first input:{}".format(score_input_2[0:5]))

total_score_independent_sampling=score_input_1+score_input_2
print("First 5 samples from the array of the total array,independent sampling:{}".format(total_score_independent_sampling[0:5]))

total_score_dependent_sampling = score_input_1 + score_input_1
print("First 5 results from the total array, dependent sampling: {}".format(total_score_dependent_sampling[0:5]))

sns.set_style ('whitegrid')

plt.hist(score_input_1,
         bins=1000,
         density=True,
         label="standard lognormal disribution",
         histtype='step',
         lw=1)
plt.hist(total_score_dependent_sampling,
         bins=1000,
         density=True,
         label='Sum of two standard lognormal distribution -\nDependent sampling',
         histtype='step',
         lw=2,
         linestyle='--'
         )
plt.hist(total_score_independent_sampling,
         bins=1000,
         density=True,
         label='Sum of two standard lognormal distribution -\nIndependent sampling',
         histtype='step',
         lw=2,
         linestyle=':'
         )
plt.legend(frameon=True)
plt.gca().set_xlim([-2,20])
plt.show()

print(sp.stats.describe(score_input_1),'median=',np.median(score_input_1))
print(sp.stats.describe(score_input_2),'median=',np.median(score_input_2))

print(sp.stats.describe(total_score_independent_sampling),'median=',np.median(total_score_independent_sampling))
print(sp.stats.describe(total_score_dependent_sampling),'median=',np.median(total_score_dependent_sampling))


def ovl_two_random_arr(arr1,arr2,number_bins="Silvermans rule"):
    assert number_bins=="Silvermans rule" or isinstance(number_bins,int),'number_bins is not proprely defined'
    min_value=np.min((arr1.min(),arr2.min()))
    max_value=np.min((arr1.max(),arr2.max()))

    if number_bins =="Silvermans rule":
        if len(arr1)>=len(arr2):
            arr=arr1
        else:
            arr=arr2
        bin_width=1.06*len(arr)**-0.2*np.std(arr)
        number_bins=int((max_value-min_value)//bin_width)
    else:
        bin_width=(max_value-min_value)/number_bins

    lower_bound=min_value
    min_arr=np.empty(number_bins)
    for b in range(number_bins):
        higher_bound=lower_bound+bin_width
        freq_arr1 = np.ma.masked_where((arr1 < lower_bound) | (arr1 >= higher_bound), arr1).count() / len(arr1)
        freq_arr2 = np.ma.masked_where((arr2 < lower_bound) | (arr2 >= higher_bound), arr2).count() / len(arr2)
        # Conserve the lower frequency
        min_arr[b] = np.min((freq_arr1, freq_arr2))
        lower_bound = higher_bound  # To move to the next range
    return min_arr.sum()


ovl = ovl_two_random_arr(total_score_dependent_sampling, total_score_independent_sampling)
print("The two distributions share {:.1%} of their surface".format(ovl))
