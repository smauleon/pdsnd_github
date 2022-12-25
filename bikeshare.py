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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = list(CITY_DATA.keys())
    while True:
        city = input('\nEnter a city (Chicago, New York City, or Wasington):\n').lower()
        try:
            if city not in cities:
                print("\nPlease enter a valid city from the list:\n")
            else:
                break
        except ValueError:
            print("\nPlease enter a valid city from the list:\n")

    # TO DO: get user input for month (all, january, february, ... , december)
    months = ['all','january','february','march','april','may','june','july','august','september','october','november','december'] 
    while True:
        month = input('\nEnter a month:\n').lower()
        if month not in months:
            month = input('\nPlease enter a valid month:\n').lower()
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday'] 
    while True:
        day = input('\nEnter a day:\n').lower()
        if day not in days:
            days = input('\nPlease enter a valid day:\n').lower()
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

    df = pd.read_csv(CITY_DATA[city])
    
    #start time to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    #filter data
    if month != 'all':
        months = ['january','february','march','april','may','june','july','august','september','october','november','december'] 
        month = months.index(month) + 1
        df = df[df['Start Time'].dt.month == month]
        
    if day != 'all':
        df = df[df['Start Time'].dt.weekday_name == day.title()]
  
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['Start Time'].dt.month.mode()[0]
    print('Most Common Month is: ', most_common_month)
    # TO DO: display the most common day of week
    most_common_day = df['Start Time'].dt.weekday_name.mode()[0]
    print('Most Common Day is: ', most_common_day)

    # TO DO: display the most common start hour
    most_common_hour = df['Start Time'].dt.hour.mode()[0]
    print('Most Common Hour is: ', most_common_hour, '(24h clock)')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print('Most Common Start Station: ', most_common_start_station)

    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print('Most Common End Station: ', most_common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    combo = df.groupby(['Start Station', 'End Station'])
    most_frequent_combo = combo.size().sort_values(ascending=False).head(1)
    print('Most Frequent Station Combo: \n',most_frequent_combo)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time: ', total_travel_time)

    # TO DO: display mean travel time
    avg_travel_time = df['Trip Duration'].mean()
    print('Average travel time: ', avg_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type_count = df['User Type'].value_counts()
    print('\nCount of User Types: \n', user_type_count)

    # TO DO: Display counts of gender
    if 'Gender' in df:
        gender_count = df['Gender'].value_counts()
        print('\nGender count: \n', gender_count)
    else:
        print('\nGender count cannot be displayed')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_dob = int(df['Birth Year'].min())
        print('\nEarliest DOB: ', earliest_dob)
    else:
        print('\nDOB cannot be determined')
        
    if 'Birth Year' in df:
        latest_dob = int(df['Birth Year'].max())
        print('\nLatest DOB: ', latest_dob)
    else:
        print('\nDOB cannot be determined')

    if 'Birth Year' in df:
        common_dob = int(df['Birth Year'].mode()[0])
        print('\nMost Common DOB: ', common_dob)
    else:
        print('\nDOB cannot be determined')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#Display first five rows
def display_data(df):
    row = 0
    while True:
        raw_data = input("\nWould like to see raw data: (yes or no): ").lower()
        if raw_data == "yes":
            print(df.iloc[row:row+6])
            row = row + 6
        elif raw_data == "no":
            break
        else:
            print("Please enter a valid answer")

    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        print(load_data('washington','may','all').shape[0] == load_data('washington','all','all').shape[0])
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
    
#references
#https://www.datainsightonline.com/post/exploring-us-bikeshare-data-project
#https://www.w3schools.com/python/pandas/pandas_csv.asp
