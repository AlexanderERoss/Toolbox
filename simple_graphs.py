import pyplot from matplotlib as plt
import math

# Nested Pie Chart Function (pie_nest(df, inner_col, outer_col))
def pie_nest(df, inner_col, outer_col, color_palette=[]):
    '''Note that each type outer col needs to be a subset 
    of the inner column.
    Requires pyplot imported as plt'''
    inner_dist = df[inner_col].value_counts()
    full_freq = df.groupby([inner_col, outer_col]).size()
    inner_labels = []
    inner_freq = []
    outer_labels = []
    outer_freq = []
    for i, v in full_freq.iteritems():
        if i[0] not in inner_labels:
            inner_labels.append(i[0])
            inner_freq.append(inner_dist[i[0]])
        outer_labels.append(i[1])
        outer_freq.append(v)
    # Set up colour scheme
    if color_palette != []:
        palette_provided = True
        colors
    else:
        palette_provided = False
    # Outer Ring plot
    fig, ax = plt.subplots()
    ax.axis('equal')
    if palette_provided:
        outer_pie, _ = ax.pie(outer_freq, radius=1.3,
                              labels=outer_labels)#,
                              #colors=color_pallette)
    else:
        outer_pie, _ = ax.pie(outer_freq, radius=1.3,
                              labels=outer_labels)
    plt.setp(outer_pie, width=0.3, edgecolor='white')
    # Inner Ring Plot
    if palette_provided:
        inner_pie, _ = ax.pie(inner_freq, radius=1.3-0.3,
                              labels=inner_labels, 
                              labeldistance=0.7)
    else:
        inner_pie, _ = ax.pie(inner_freq, radius=1.3-0.3,
                              labels=inner_labels, 
                              labeldistance=0.7)
    plt.setp(inner_pie, width =0.4, edgecolor='white')
    plt.margins(0,0)
    # Display Plot
    plt.show() 
