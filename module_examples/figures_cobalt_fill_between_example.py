# library
import matplotlib.pyplot as plt
import seaborn as sns

#create figure 
fig = plt.figure(1, figsize=(5,5))

countries =[ 'DR of the Congo','Australia', 'Botswana', 'Brazil',
            'Canada', 'China', 'Cuba', 'Finland', 'Indonesia', 
            'Kazakhstan', 'Madagascar', 'Morocco', 'New Caledonia',
            'Norway', 'Papua New Guinea', 'Phillippines', 'Russia',
            'South Africa', 'United States', 'Vietnam', 'Zambia',
            'Zimbabwe']
the_colors=sns.cubehelix_palette(22, start=0.5, rot=-.75)
year = [1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015]

y1=[14.16, 21.41, 29.02, 26.79, 27.97, 27.98, 33.50, 37.58, 38.71, 34.46, 40.43, 49.88, 54.55, 53.15, 49.52, 49.12, 50.00, 50.00]
y2=[9.35, 12.54, 14.78, 14.06, 13.03, 11.34, 9.29, 7.04, 7.33, 6.42, 5.99, 5.42, 3.50, 3.47, 5.59, 5.62, 4.90, 4.76]
y3=[0.95, 1.01, 0.81, 0.73, 0.52, 0.56, 0.37, 0.50, 0.43, 0.33, 0.42, 0.43, 0.25, 0.13, 0.19, 0.22, 0.16, 0.25]
y4 =[1.13, 2.14, 2.37, 2.24, 2.11, 2.46, 2.32, 2.15, 1.57, 3.70, 3.29, 2.59, 2.85, 3.26, 2.76, 3.07, 3.14, 3.02]
y5=[16.60, 16.28, 13.98, 11.89, 9.86, 8.18, 8.39, 8.85, 10.16, 11.79, 11.21, 4.89, 4.21, 6.16, 6.36, 6.29, 5.66, 5.48]
y6=[0.11, 0.76, 0.24, 0.33, 1.92, 1.32, 2.09, 3.22, 2.63, 8.28, 8.30, 7.48, 5.80, 6.13, 7.14, 6.32, 6.31, 6.11]
y7=[7.55, 7.76, 7.53, 7.65, 6.59, 6.19, 5.89, 7.36, 8.00, 6.16, 5.01, 5.74, 4.36, 4.59, 4.67, 3.68, 3.03, 3.41]
y8=[0, 0, 0, 0, 0, 0.19, 0.17, 0.15, 0.14, 0.16, 0.13, 0.03, 0.13, 0.45, 0.60, 0.66, 0.63, 0.35]
y9=[0, 0, 0, 0, 0, 0, 2.8, 2.45, 2.29, 2.17, 1.63, 1.50, 1.45, 1.44, 1.62, 1.49, 1.07, 1.03]
y10=[0.85, 0.92, 0.79, 0.67, 0.57,0,0,0,0,0,0,0,0,0,0,0,0,0]
y11=[0,0,0,0,0,0,0,0,0,0,0,0,0.15, 0.45, 0.60, 1.93, 2.54, 2.94]
y12=[0.81, 2.64, 2.55, 2.77, 2.78, 2.63, 2.65, 2.45, 3.71, 2.44, 2.13, 3.25,2.83, 1.95, 1.90, 1.75, 1.76, 2.06]
y13=[2.83, 3.36, 3.17, 3.13, 5.33, 4.92, 4.52, 2.71, 2.33, 3.05, 2.64, 2.49, 2.59, 2.79, 2.54, 2.80, 3.31, 2.92]
y14=[0, 0.31, 0.26, 0.22, 0.19, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,0]
y15=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.45, 0.89, 1.75, 1.99]
y16=[0, 0, 0, 0, 0, 0.19, 0.17, 0.46, 1.29, 1.36, 1.50, 1.75, 1.91, 1.80, 2.57, 2.46, 3.77, 3.41]
y17=[10.20, 11.93, 10.55, 10.27, 8.81, 11.53, 9.95, 9.66, 9.00, 8.55, 7.76, 7.61, 5.64, 5.50, 6.00, 5.53, 5.16, 4.92]
y18=[1.23, 1.38, 1.53, 1.25, 1.00, 0.91, 1.01, 0.95, 0.86, 0.81, 0.74, 0.76, 1.64, 1.44, 2.38, 2.63, 2.46, 2.38]
y19=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.1,0.6]
y20=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,.02,0.18,0.22]
y21=[33.71, 17.25, 12.14, 17.86, 19.16, 21.36, 16.58, 14.26, 11.43, 10.18, 8.76, 6.11, 7.86, 6.94, 5.18, 5.19, 3.77, 3.65]
y22 =[0.39, 0.37, 0.21, 0.21, 0.19, 0.25, 0.23, 0.15, 0.16, 0.14, 0.11, 0.09, 0.07, 0.16, 0.19, 0.28, 0.29, 0.29]

# Basic stacked area chart.
plt.stackplot(year,y1, y2, y3, y4, y5, y6, y7, y8, y9, y10, y11, y12, y13, y14, y15,y16,y17,y18,y19,y20,y21,y22, labels=countries, colors=the_colors)

#define axes limits
plt.xlim([1998,2015])
plt.ylim([0,100])

#define axes labels
plt.ylabel('market share of Co production %')
plt.xlabel('year')

#plot text and line on top of figure
plt.axvline(x=2003, linestyle='dotted', color='black')
plt.text(2006, 10, 'Democratic Republic \n      of the Congo')
plt.text(1999, 92, r'Zambia', color='white')
plt.text(2003.5, 15, r'End of Second Congo War', rotation=90)

#reverse legend order
current_handles, current_labels = plt.gca().get_legend_handles_labels()
plt.legend(list(reversed(current_handles)),list(reversed(current_labels)), 
           bbox_to_anchor=(1.51, 1.015), fontsize=9)

#save final image
plt.savefig('data_for_exercises/plotting/DRC.png', dpi=300,bbox_inches="tight")