import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# gas = pd.read_csv('gas price.csv')

# plt.title('Gas prices overtime(in USD)', fontdict={'fontweight': 'bold', 'fontsize': 18})

# plt.plot(gas.Year, gas.USA, 'b.-', label='United State')
# plt.plot(gas.Year,gas.Canada,'g.-', label='Canada')
# plt.plot(gas['Year'], gas['South Korea'], 'r.-', label= 'South Korea')
# plt.plot(gas.Year, gas.Australia, 'y.-', label='Australia')

# # either go with . or [] but when use []dont use .


# # Another way 1
# # for country in gas:
# #     if country != 'Year':
# #         plt.plot(gas.Year, gas[country], marker='.')

# # Another way 2
# # countries_to_look_at= ['Australia', 'USA', 'Canada', 'South Korea']
# # for country in gas:
# #     if country in countries_to_look_at:
# #         plt.plot(gas.Year, gas[country])


# plt.xlabel('Year')
# plt.ylabel('US Doller')



# plt.xticks(gas.Year[::3].tolist()+[2011])

# plt.legend()
# plt.savefig('Gas_price_figure.png', dpi=300)

# plt.show()

# FIFA

fifa= pd.read_csv('fifa_data.csv')
## Histogram
# bins= [40,50,60,70,80,90, 100]
# plt.hist(fifa.Overall, bins=bins, color='#1a278a')

# plt.xlabel('Skill Level')
# plt.ylabel('Number of Player')
# plt.title('Distribution of Player Skills in FIFA 2018')

# plt.xticks(bins)
# plt.show()

# Pie chart

# left=fifa.loc[fifa['Preferred Foot']=='Left'].count()[0]
# right=fifa.loc[fifa['Preferred Foot']=='Right'].count()[0]

# label=['Left','Right']
# colors=['#fa9005', '#072ded']
# plt.pie([left, right], labels= label, colors=colors, autopct='%.2f %%')
# plt.title('Foot Preference of FIFA Players')

# plt.show()

##Pie Chart

# fifa.Weight=[int(x.strip('lbs')) if type(x)==str else x for x in fifa.Weight]

# plt.style.use ('ggplot')

# light= fifa.loc[fifa.Weight < 125].count()[0]
# light_medium= fifa.loc[(fifa.Weight >=125) & (fifa.Weight <150)].count()[0]
# medium=fifa.loc[(fifa.Weight >=150) & (fifa.Weight <175)].count()[0]
# medium_heavy=fifa.loc[(fifa.Weight>= 175)& (fifa.Weight <200)].count()[0]
# heavy= fifa.loc[(fifa.Weight >= 200)].count()[0]


# # colors=['blue','green', 'red', 'gray', 'yellow']
# weights=[light, light_medium, medium, medium_heavy,  heavy]

# labels=['Under 125', '125-150', '150-175', '175-200', 'Over 200']

# explode=[0.4,0.2,0,0,0.4]

# plt.pie(weights, labels=labels,autopct='%0.2f %%', pctdistance=0.8, explode=explode )
# plt.show()

##Whisker chart

Barcelona=fifa.loc[fifa.Club=='FC Barcelona','Overall']
Madrid=fifa.loc[fifa.Club=='Real Madrid','Overall']
Revo= fifa.loc[fifa.Club=='New England Revolution', 'Overall']
Napoli=fifa.loc[fifa.Club=='Napoli','Overall']

plt.figure(figsize=(6,7))

Team=[Barcelona, Madrid, Revo, Napoli]
Labels=['FC Barcelona', 'Real Madrid', 'NE Revolution', 'Nepoli']


boxes= plt.boxplot(Team, labels=Labels, patch_artist=True, medianprops=dict(linewidth=2, linestyle= '--', color='black'))
for box in boxes['boxes']:
    #set edge color
    box.set(linewidth=2, color='#1f07f2')

    #Change Fill color

    box.set(facecolor= '#e0e0d3')

plt.title('Professional Football Team Comparison')
plt.ylabel('FIFA Overall Rating')



plt.show()
