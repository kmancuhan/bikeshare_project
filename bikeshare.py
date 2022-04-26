import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('\nPlease type the name of the city to analyze (Chicago, New York City or Washington): ').lower()
        if city not in ['chicago', 'new york city', 'washington']:
            print('Please type a valid city name! Only available options are Chicago, New York City and Washington.')
        else:
            break
    # get user input for month (all, january, february, ... , june)
    while True:
        month = input('\nPlease type the name of the month, January through June, to filter by (Type "all" for no filter): ').lower()
        if month not in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
            print('Please type a valid month name! Only available options are months from January until June; or, "all" for no filter.' )
        else:
            break
    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('\nPlease type the name of the day of a week, Monday through Sunday; or, "all" for no filter: ').lower()
        if day not in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
            print('Please type a valid day name! Only available options are days from Monday until Sunday; or, "all" for no filter.')
        else:
            break
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
    try:
        file_name = CITY_DATA[city]
        df = pd.read_csv(file_name)
        if month != 'all':
            month = ['january', 'february', 'march', 'april', 'may', 'june'].index(month) + 1
            df = df[pd.to_datetime(df['Start Time']).dt.month == month]
        if day != 'all':
            df = df[pd.to_datetime(df['Start Time']).dt.day_name().apply(lambda x: x.lower()) == day]
    except FileNotFoundError:
        print('Couldn\'t open the file! Please verify the correctness of the file name')
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    try:
        # display the most common month
        month = pd.to_datetime(df['Start Time']).dt.month.mode()[0]
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        print(f"Most common month is {months[month-1].title()}.")

        # display the most common day of week
        most_common_day = pd.to_datetime(df['Start Time']).dt.day_name().mode()[0]
        print(f"Most common day of the week is {most_common_day.title()}.")

        # display the most common start hour
        most_common_start_hour = pd.to_datetime(df['Start Time']).dt.hour.mode()[0]
        print(f"Most common start hour is {most_common_start_hour}.")
    except KeyError:
        print("An attempt to access an invalid column or row label in time stats! Verify column and row labels.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    try:
        # display most commonly used start station
        print(f"Most commonly used start station is {df['Start Station'].mode()[0]}.")

        # display most commonly used end station
        print(f"Most commonly used end station is {df['End Station'].mode()[0]}.")

        # display most frequent combination of start station and end station trip
        most_frequent_trip = (df['Start Station'] + ' to ' + df['End Station']).mode()[0]
        print(f"Most frequent combination of start station and end station trip: {most_frequent_trip}.")
    except KeyError:
        print("An attempt to access an invalid column or row label in station stats! Verify column and row labels.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    try:
        # display total travel time
        print(f"Total travel time is {df['Trip Duration'].sum()}")

        # display mean travel time
        print(f"Mean travel time is {df['Trip Duration'].mean()}")
    except KeyError:
        print("An attempt to access an invalid column or row label in trip duration stats! Verify column and row labels.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    try:
        # Display counts of user types
        print(df['User Type'].value_counts(), '\n')

        # Display counts of gender
        if 'Gender' in df.columns:
            print(df['Gender'].value_counts(), '\n')

        # Display earliest, most recent, and most common year of birth
        if 'Birth Year' in df.columns:
            print(f"Earliest birth year is {df['Birth Year'].min()}")
            print(f"Most recent birth year is {df['Birth Year'].max()}")
            print(f"Most common birth year is {df['Birth Year'].mode()[0]}")
    except KeyError:
        print("An attempt to access an invalid column or row label in time stats! Verify column and row labels.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    """
        Displays raw data depending on the user's choice,
        a window of 5 rows at a time.
    """
    num_rows, _ = df.shape
    # Current window of 5 rows to display.
    window, window_length = 1, 5
    # Compute the number of windows of length 5, each window displayed at a time.
    windows = num_rows // 5 if num_rows % 5 == 0 else num_rows // 5 + 1
    # Iterates through each window of 5 rows at a time.
    while window <= windows:
        # Gets the user input whether they want to display any raw data.
        while True:
            display = input("\nWould you like to display 5 rows of raw data (yes or no)? ").lower()
            if display not in ['yes', 'no']:
                print("Please type a valid option for displaying raw data! Options are yes or no.")
            else:
                break
        # Breaks the loop if the user doesn't want to display data.
        if display == "no":
            break
        # Print out five rows if the user wants to display data, based on
        # the integer row label.
        if window == windows:
            # Print the trailing rows in the last window
            print(df.iloc[(window - 1)*window_length:])
        else:
            # Print 5 rows at a time.
            print(df.iloc[(window - 1)*window_length:(window)*window_length])

        window += 1

    print("\nDisplaying the raw data terminated.")
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
