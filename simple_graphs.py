import pyplot from matplotlib as plt
import math

# Function to define colormaps for palettes
def w2c_colormap(color_code, bins):
    return lsc.from_list(color_code.replace('#','C'), ['#FFFFFF', color_code], bins)

# Nested Pie Chart Function (pie_nest(df, inner_col, outer_col))
def pie_nest(df, inner_col, outer_col, color_palette=None):
    '''Note that each type outer col needs to be a subset 
    of the inner column.
    Requires pyplot imported as plt and LinearSegmentedColormap
    from matplotlib.colors as lsc and math'''
    inner_dist = df[inner_col].value_counts()
    full_freq = df.groupby([inner_col, outer_col]).size()

    inner_labels = []
    inner_freq = []
    outer_labels = []
    outer_freq = []
    label_dict = {}
    for i, v in full_freq.iteritems():
        if i[0] not in inner_labels:
            inner_labels.append(i[0])
            inner_freq.append(inner_dist[i[0]])
        outer_labels.append(i[1])
        outer_freq.append(v)
        if i[0] not in label_dict.keys():
            label_dict[i[0]] = {}
            label_dict[i[0]][i[1]] = v
        else:
            label_dict[i[0]][i[1]] = v
        
    # Set up colour scheme
    if color_palette:
        if len(inner_dist) >= len(color_palette):
            color_palette = color_palette[0:len(inner_dist)]
        else:
            color_palette = color_palette*math.ceil(len(inner_dist)/len(color_palette))[0:len(inner_dist)]
        color_maps = [w2c_colormap(c, 20) for c in color_palette]
        inner_colors = [cm(0.9) for cm in color_maps]
        outer_colors = []
        for in_lab in label_dict.keys():
            out_labs = label_dict[in_lab]
            in_len = len(out_labs)
            cm = color_maps[inner_labels.index(in_lab)]
            i = 0
            for out_lab in out_labs.keys():
                grad = i*0.6/(in_len-1) + 0.2 if in_len > 1 else 0.5
                outer_colors.append(cm(grad))
                i += 1
                
    # Outer Ring plot
    fig, ax = plt.subplots()
    ax.axis('equal')
    outer_pie, _ = ax.pie(outer_freq, radius=1.3,
                          labels=outer_labels,
                          colors=outer_colors)
    plt.setp(outer_pie, width=0.3, edgecolor='white')
    
    # Inner Ring Plot
    inner_pie, _ = ax.pie(inner_freq, radius=1.3-0.3,
                          labels=inner_labels, 
                          labeldistance=0.7,
                          colors=inner_colors)
    plt.setp(inner_pie, width =0.4, edgecolor='white')
    plt.margins(0,0)
    # Display Plot
    plt.show()    
