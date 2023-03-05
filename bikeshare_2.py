import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():

    MONTH_DATA = {'january':1,'february':2,'march':3,'april':4,'may':5,'june':6,'all':7}
    DAY_DATA = {'monday':1,'tuesday':2,'wednesday':3,'thursday':4,'friday':5,'saturday':6,'sunday':7,'all':8}

    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = ''
    while city not in CITY_DATA.keys():
        print("Would you like to see data for Chicago, New York or Washington? \nPlease enter 'chicago' or 'new york city' or 'washington':")
        city = input().lower()
        if city not in CITY_DATA.keys():
            print('invalid input, please input again.')
    print('The data is for {}.'.format(city.title()))


    # get user input for month (all, january, february, ... , june)

    month = ''
    while month not in MONTH_DATA.keys():
        print("Which month would you like to explore? \nPlease enter 'all','january','february','march','april','may','june':")
        month = input().lower()

        if month == 'all':
            print('The data is for all months.')
        elif month in MONTH_DATA.keys():
            print('The data is for {}.'.format(month.title()))
            break
        else:
            print('invalid input, please try again.')
            continue

    # get user input for day of week (all, monday, tuesday, ... sunday)

    day = ''
    while day not in DAY_DATA.keys():
        print("Which day would you like to explore? \nPlease enter 'all','monday','tuesday','wednesday','thursday','friday','saturday','sunday':")
        day = input().lower()

        if day == 'all':
            print('The data is for all days.')
        elif day in DAY_DATA.keys():
            print('The data is for {}.'.format(day.title()))
            break
        else:
            print('invalid input, please try again.')
            continue

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    #load csv into DataFrame

    df = pd.read_csv(CITY_DATA[city])

    # Convert the start time column to datetime

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extract month from start time

    df['Month'] = df['Start Time'].dt.month_name()

    # Extract day from start time

    df['Day'] = df['Start Time'].dt.day_name()

    # Extract hour from start time

    df['Hour'] = df['Start Time'].dt.hour

    #filter by month

    if month != 'all':
        month_df = df[(df['Month']==month.title())]
        return month_df

    #filter by day

    elif day != 'all' :
        day_df = df[(df['Day']==day.title())]
        return day_df

    #no filter

    else:
        return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month

    most_common_month = df['Month'].value_counts().idxmax()
    print('The most common month is {}.'.format(most_common_month))

    # display the most common day of week

    most_common_day = df['Day'].value_counts().idxmax()
    print('The most common day is {}.'.format(most_common_day))

    # display the most common start hour

    most_common_hour = df['Hour'].value_counts().idxmax()
    print('The most common start hour is {}.'.format(most_common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station

    start_station = df['Start Station'].value_counts().idxmax()
    print('The most commonly used start station is {}.'.format(start_station))

    # display most commonly used end station

    end_station = df['End Station'].value_counts().idxmax()
    print('The most commonly used end station is {}.'.format(end_station))

    # display most frequent combination of start station and end station trip

    combination_station = df.groupby(['Start Station','End Station']).count()
    print('The most frequent combination of start station and end station is {}.'.format(combination_station.idxmax()[0][0],combination_station.idxmax()[0][1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time

    time_sum = df['Trip Duration'].sum()
    print('The total travel time is {} seconds.'.format(time_sum))

    # display mean travel time

    time_mean = df['Trip Duration'].mean()
    print('The mean travel time is {} seconds.'.format(time_mean))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    # Calculate the counts of user type

    user_type = df['User Type'].value_counts()
    print('The counts of user types: \n')

    # Display the counts of each user type

    for ut, uc in user_type.iteritems():
        print('{:10}:{:,}'.format(ut,uc))

    # Display counts of gender

    # Only display gender when the city user inputs has the gender column

    if 'gender' in df.columns:

        # Calculate the counts of gender

        gender_count = df['Gender'].value_counts()
        print('The counts of gender: \n')

        # Display the counts of each gender

        for g, gc in gender_count.iteritems():
            print('{:7}:{:,}'.format(g,gc))

    # Display earliest, most recent, and most common year of birth

    # Only display birth year when the city user inputs has the birth city colunm

    if 'birth year' in df.columns:

        # Calculate the earliest year of birth

        earliest_year = df['Birth Year'].min()
        print('The earliest year of birth is {}.'.format(earliest_year))

        # Calculate the most recent year of birth

        recent_year = df['Birth Year'].max()
        print('The most recent year of birth is {}.'.format(recent_year))

        # Calculate the most common year of birth

        common_year = df['Birth Year'].value_counts().idxmax()
        print('The most common year of birth is {}.'.format(common_year))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

# Define a function to display raw data

def display_data(df):

    USER_CHOICE = ['yes','no']
    choice = ''

    counts = 0

    # Let user choose if they would like to see raw data

    while choice not in USER_CHOICE:
        print("Would you like to see raw data?\nPlease enter 'yes' or 'no':")
        choice = input().lower()

        # Display first 5 rows data if user input yes

        if choice == 'yes':
            print(df.head())

            # Let user choose if they would like to see more data

            print("\nWould you like to see 5 more rows data?\nPlease enter 'yes' or 'no':")
            choice = input().lower()
            counts += 5
            if choice == 'yes':
                print(df[counts:counts+5])
            elif choice == 'no':
                break

        elif choice not in USER_CHOICE:
            print('invalid input, please try again:')

    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)


        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
