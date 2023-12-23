#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Student Name: LAIBA ASIF

Student ID: R00201303

Cohort: SD3A

"""
"""Task 01"""

# Pandas for data manipulation and analysis.
import pandas as pd

# matplotlib.pyplot for data visualization.
import matplotlib.pyplot as plt

# Define a function named 'task1'
def task1():

    # Read the Movies.csv into pandas DataFrame named 'df'
    df = pd.read_csv(r'C:\Users\asifl\OneDrive\Desktop\python\Movies-1.csv')

    # Calculate unique number of values in 'main_Genre' column & assigns it to the 'uniqueMainGenres' variable.
    uniqueMainGenres = df['main_Genre'].nunique()
    # Find mode (most frequent value) in 'main_Genre' column & assigns it to the 'mostPopularGenre' variable.
    mostPopularGenre = df['main_Genre'].mode().values[0]
    # Creates Series(genreCounts) containing the counts of each unique value in 'main_Genre' column.
    genreCounts = df['main_Genre'].value_counts()
    # Find index (genre) with the minimum count in 'genreCounts' Series & assigns it to the 'leastPopularGenre' variable.
    leastPopularGenre = genreCounts.idxmin()

    # Display the Output
    print("The total number of unique main_Genres: ",uniqueMainGenres)
    print("The most popular main_genre: ",mostPopularGenre)
    print("The least popular main_genre: ",leastPopularGenre)

    # Select top 8 genres with the highest counts from genreCounts Series and assigns them to the topEight variable.
    topEight = genreCounts.head(8)

    # Create a bar plot using the topEight Series.
    topEight.plot(kind='bar')
    # The plot is displayed with the specified title and axis labels using matplotlib.pyplot.
    plt.title('Top 8 Popular Genres')
    plt.xlabel('Genre')
    plt.ylabel('Count')
    plt.xticks(rotation=45)  # Rotate the x-axis labels for better readability.
    # Display the generated bar plot.
    plt.show()


# Execute all the code within 'task1' function.
task1()

"""Task 02"""

# Pandas for data manipulation and analysis.
import pandas as pd

# Define a function named 'task2'
def task2():

    # Read the Movies.csv into pandas DataFrame named 'df'
    df = pd.read_csv(r'C:\Users\asifl\OneDrive\Desktop\python\Movies-1.csv')

    # Several operations on the 'Genre' column
    # 1.Split the values in the 'Genre' by commas, creating lists of genres.
    # 2.'explode' transform each element of a list-like to a row, duplicating the index values.
    # 3.Count the occurrences of each unique genre.
    # Result is a Series (genreCounts) containing the counts of individual genres.
    genreCounts = df['Genre'].str.split(',').explode().value_counts()

    # Find index (genre) with the maximum and minimum counts in genreCounts & assign them to mostCommon & leastCommon.
    mostCommon = genreCounts.idxmax()
    leastCommon = genreCounts.idxmin()

    # Display the most and least common genres
    print("The Most Common Genre: ",mostCommon)
    print("The Least Common Genre: ",leastCommon)


# Execute all the code within 'task6' function.
# task2()

"""Task 03"""

# Pandas for data manipulation and analysis.
import pandas as pd

# matplotlib.pyplot for data visualization.
import matplotlib.pyplot as plt

# Define a function named 'task3'
def task3():

    # Read the Movies.csv into pandas DataFrame named 'df'
    df = pd.read_csv(r'C:\Users\asifl\OneDrive\Desktop\python\Movies-1.csv')


    # Extract the numeric part from the 'Runtime' (assuming it contains some text and a numeric value) & convert it to numeric format.
    # Any non-numeric values are coerced to NaN (Not a Number).
    df['Runtime'] = pd.to_numeric(df['Runtime'].str.extract('(\d+)')[0], errors='coerce')
    # Remove NaN values 'Runtime' column.
    df = df.dropna(subset=['Runtime'])


    # Calculate 1st quartile (q1), 3rd quartile (q3) & the inter-quartile (iqr) range of the 'Runtime' column.
    q1 = df['Runtime'].quantile(0.25)
    q3 = df['Runtime'].quantile(0.75)
    iqr = q3 - q1
    # Then define lower and upper bounds for identifying outliers based on the IQR range.
    lowerBound = q1 - 1.5 * iqr
    upperBound = q3 + 1.5 * iqr

    # Identify outliers in the 'Runtime' column by filtering rows that fall outside the defined lower and upper bounds.
    outliers = df[(df['Runtime'] < lowerBound) | (df['Runtime'] > upperBound)]
    print(lowerBound,upperBound)
    # Titles of movies with runtime outliers are stored in the outlierMovies.
    outlierMovies = outliers['Title'].unique()

    # Create a boxplot to visualize the distribution of movie runtimes.
    plt.figure(figsize=(10, 6))
    plt.boxplot(df['Runtime'], vert=False, widths=0.5, patch_artist=True)
    plt.title('Outliers in Movie Runtime')
    plt.xlabel('Runtime (minutes)')
    plt.yticks([])
    plt.show()


    # loop prints the titles of movies with runtime outliers.
    for movie in outlierMovies:
        print(movie)

# Execute all the code within 'task6' function.
#task3()

"""Task 04"""

# Pandas for data manipulation and analysis.
import pandas as pd

# matplotlib.pyplot for data visualization.
import matplotlib.pyplot as plt

# Define a function named 'task4'
def task4():

    # Reads the "Movies-1.csv" & stores the data in a pandas DataFrame called df.
    df = pd.read_csv(r'C:\Users\asifl\OneDrive\Desktop\python\Movies-1.csv')

    # Calculate the number of null (missing) values in the 'Number of Votes' & 'Rating' columns.
    # Use isnull() method & sum the results.
    nullVotes = df['Number of Votes'].isnull().sum()
    nullRating = df['Rating'].isnull().sum()

    # scatter plot to visualize the relationship between the 'Number of Votes' and 'Rating' columns.
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Number of Votes'], df['Rating'], alpha=0.5)  # alpha=0.5 parameter makes points semi-transparent for better visibility.
    plt.title('Relationship between Number of Votes and Rating')
    plt.xlabel('Number of Votes')
    plt.ylabel('Rating')
    plt.show()

    # Print the counts of null values in the 'Number of Votes' and 'Rating' columns.
    print(f"Null values in 'Number of Votes': {nullVotes}")
    print(f"Null values in 'Rating': {nullRating}")

# Execute all the code within 'task4' function.
#task4()

""" COMMENTS FOR THE TASK """
"The existence of null values in these attributes/columns may result from mistakes in recording or from missing data during data collection."
"Null values must be handled carefully to prevent problems with data analysis and visualisation."

"""Task 05"""

# Pandas for data manipulation and analysis.
import pandas as pd

# 're' for regular expressions
import re

#  'Counter' from the 'collections' module for counting occurrences of elements.
from collections import Counter

# Define a function named 'task5'
def task5():


    # Read Movies.csv & main_genre.csv & store data in pandas DataFrames (mainDF and moviesDF).

    mainDF = pd.read_csv(r'C:\Users\asifl\OneDrive\Desktop\python\main_genre.csv',encoding='ISO-8859-1')
    moviesDF = pd.read_csv(r'C:\Users\asifl\OneDrive\Desktop\python\Movies-1.csv')

    # Process the terms in main_genre.csv
    # Convert the column names to lowercase
    mainGenreTerms = mainDF.columns.str.lower().tolist()
    # And remove characters like quotes, commas, periods, and hyphens from each term.
    mainGenreTerms = [re.sub(r"[',.\-]", '', term) for term in mainGenreTerms]

    # Process the synopsis column of 'Movies-1.csv'
    # Convert the synopsis text to lowercase.
    moviesDF['Synopsis'] = moviesDF['Synopsis'].str.lower()
    # And remove characters like quotes, commas, periods, and hyphens.
    moviesDF['Synopsis'] = moviesDF['Synopsis'].apply(lambda x: re.sub(r"[',.\-]", '', x))

    # Loop that iterate over each term in mainGenreTerms.
    for mainGenre in mainGenreTerms:
        # Create a list of related genres for the current mainGenre by excluding the term itself.
        relatedGenres = []
        for term in mainGenreTerms:
            if term != mainGenre:
                relatedGenres.append(term)
        # Filter the movies in moviesDF whose synopses contain any of the related genres.
        relatedMovies = moviesDF[moviesDF['Synopsis'].str.contains('|'.join(relatedGenres))]

        # use the 'Counter' class to count the occurrences of each related genre in the filtered movies.
        genreCounts = Counter(relatedMovies['main_Genre'])
        # Then identify the most frequent related genre.
        mostFreq = genreCounts.most_common(1)[0]

        # Prints main genre and its most frequent related genre.
        print("Main Genre: ", mainGenre, "\t\tMost Frequent: ", mostFreq[0])

# Execute all the code within 'task5' function.
#task5()

"""Task 6"""

# pandas for data manipulation and analysis.
import pandas as pd

# matplotlib.pyplot for data visualization.
import matplotlib.pyplot as plt

# seaborn for statistical data visualization.
import seaborn as sns

# Define a function named 'task6'
def task6():

    # Read the Movies.csv into pandas DataFrame named 'df'
    df = pd.read_csv(r'C:\Users\asifl\OneDrive\Desktop\python\Movies-1.csv')
    # Select only the 'Rating' and 'Gross Revenue' columns from the DataFrame in CSV file.
    df = df[['Rating', 'Gross Revenue']]

    # Convert the values in the 'Gross Revenue' column to numeric format.
    # Any non-numeric values are coerced to NaN (Not a Number), and rows with NaN values are then dropped from the DataFrame.
    df['Gross Revenue'] = pd.to_numeric(df['Gross Revenue'], errors='coerce')
    df = df.dropna()

    # Calculate the correlation between the 'Rating' and 'Gross Revenue' columns in the DataFrame using the 'corr' method.
    correlation = df['Rating'].corr(df['Gross Revenue'])

    # Print the calculated correlation coefficient between IMDb ratings and Box Office Gross with two decimal places.
    print(f"Correlation between IMDb ratings and Box Office Gross: {correlation:.2f}")

    # Visualize the correlation: create a scatter plot using Seaborn (sns.scatterplot).
    # The plot is displayed with the specified title and axis labels using matplotlib.pyplot.
    sns.scatterplot(data=df, x='Rating', y='Gross Revenue')
    plt.title('IMDb Ratings vs. Box Office Gross')
    plt.xlabel('IMDb Rating')
    plt.ylabel('Box Office Gross')
    plt.show()

# Execute all the code within 'task6' function.
task6()