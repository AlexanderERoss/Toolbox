import pyplot from matplotlib as plt
import math
def freq_plot(X, range_list, range_max, XLabel, range_min=0, coloring='#5554aa'):
    n, bins, patches = plt.hist(x=X.apply(lambda x : max(range_min, min(range_max, x))), 
                                bins=range_list, color=coloring, alpha=0.7, rwidth=0.75)
    plt.grid(axis='y', alpha=0.75)
    plt.xlabel(XLabel)
    plt.ylabel('Frequency')
    plt.title('Frequency of ' + XLabel)
    maxfreq = n.max()
    # Set a clean upper y-axis limit.
    scale = 10**np.ceil(math.log(maxfreq, 10)-2)
    plt.ylim(ymax=np.ceil(maxfreq / scale) * scale if maxfreq % 10 else maxfreq + 10)
    plt.show
