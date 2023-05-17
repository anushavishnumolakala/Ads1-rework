# importing library
import matplotlib.pyplot as plt
import pandas as pd

# read the csv file of Forigen Direct Investment as F_D_I


def read_F_D_I():
    """
   Define a function to read the data from a CSV file and clean it up
"""


F_D_I = pd.read_csv(r"C:\Users\mouli\Downloads\Forigen direct Investment.csv")
F_D_I = F_D_I.drop(columns=['Series Name', 'Series Code',
                            'Country Code'])
# dropna function helps delete the rows of NULL values
F_D_I = F_D_I.dropna()
# Use rename() to change the name of column Country Name as Country
F_D_I = F_D_I.rename(columns={'Country Name': 'Country'})
print(F_D_I)

# line plot
# creating data on which line plot will be plot


def line_plot_visualization(F_D_I):
    """
   Define a function to create a line plot with the Forigen Direct Investment data
"""


year = ['2003', '2004', '2005', '2006', '2007',
        '2008', '2009', '2010', '2011', '2012', '2013', '2014',
        '2015', '2016', '2017', '2018', '2019', '2020']
# setting figure size by using figure() function
plt.figure(figsize=(10, 8))
# making the line plot of different countries on the taken data
plt.plot(year, F_D_I.iloc[0, 1:19], label='Australia')
plt.plot(year, F_D_I.iloc[1, 1:19], label='Canada')
plt.plot(year, F_D_I.iloc[2, 1:19], label='China')
plt.plot(year, F_D_I.iloc[3, 1:19], label='India')
plt.plot(year, F_D_I.iloc[4, 1:19], label='Russia')
plt.plot(year, F_D_I.iloc[5, 1:19], label='UAE')
plt.plot(year, F_D_I.iloc[6, 1:19], label='USA')
plt.plot(year, F_D_I.iloc[7, 1:19], label='UK')

# giving labels to x-axis and y-axis
plt.xlabel('Year')
plt.ylabel('Foreign direct investment, net inflows (% of GDP)')

# giving title to graph
plt.title('Foreign direct investment, net inflows (% of GDP)')

# creating legend will  helps to describe all the elements in the graph
plt.legend()
plt.show()

# bar graph of year 2008
# creating data on which bar chart will be plot


def bar_plot_visualization(F_D_I):
    """
   Define a function to create a bar chart with the Forigen Direct Investment data
"""


x = F_D_I['Country']
y = F_D_I['2008 [YR2008]']
# setting figure size by using figure() function
plt.figure(figsize=(16, 6))
# function to add value labels


def addlabels(x, y):
    """ giving the values on the bar """
    for i in range(len(x)):
        plt.text(i, y[i], y[i], ha='center')


# making the bar chart on the taken data
plt.bar(x, y, label='Foreign direct investment, net inflows (% of GDP)',
        color='darkblue')
# calling the function to add value labels
addlabels(x, y)
plt.xlabel('Country')
plt.ylabel('Foreign direct investment, net inflows (% of GDP)')
# rotating the xlable to 45 degrees
plt.xticks(rotation=45)
plt.title('Foreign direct investment, net inflows (% of GDP) in year 2008')
plt.legend()
plt.show()

# pie chart of year 2003
# setting figure size by using figure() function


def pie_plot_visualization(F_D_I, year):
    """
   Define a function to create a pie chart with the Foreign direct investment data
"""


plt.figure(figsize=(8, 5))
# making the pie chart on the taken data
plt.pie(F_D_I['2003 [YR2003]'], labels=F_D_I['Country'],
        autopct='%1.2f%%', pctdistance=1.1, labeldistance=1.25)
plt.title(
    'pie chart of Foreign direct investment, net inflows (% of GDP) in year 2003')
plt.show()

# pie chart of year 2020
# setting figure size by using figure() function
plt.figure(figsize=(8, 5))
# making the pie chart on the taken data
plt.pie(F_D_I['2020 [YR2020]'], labels=F_D_I['Country'],
        autopct='%1.2f%%',  pctdistance=1.1, labeldistance=1.25)
plt.title(
    'pie chart of Foreign direct investment, net inflows (% of GDP) in year 2020')
plt.show()


def main():
    F_D_I = read_F_D_I()
    line_plot_visualization(F_D_I)
    bar_plot_visualization(F_D_I)
    pie_plot_visualization(F_D_I, '2003')
    pie_plot_visualization(F_D_I, '2020')


if __name__ == '__main__':
    main()
