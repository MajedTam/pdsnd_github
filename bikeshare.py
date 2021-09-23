import time
import pandas as pd
import numpy as np
import datetime
import tabulate

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
    city = ''
    validCities = ['chicago', 'new york city', 'washington']
    #check thta the input is valid
    while(city not in validCities):
        city = input('Please enter name of the city to analyze (chicago, new york city, washington) \n').lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month = ''
    validMonths = ['january', 'february', 'march', 'april', 'may', 'june','all']
    while(month not in validMonths):
        month = input('Please enter the name of the month to filter by (january-june), or "all" to apply no month filter \n').lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = ''
    validDays = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday','saturday','all']
    while(day not in validDays):
        day = input('name of the day of week to filter by (sunday-saturday), or "all" to apply no day filter \n').lower()

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
    # load data file into a dataframe
    df = pd.read_csv(city+'.csv')
     # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) +1
    
        # filter by month to create the new dataframe
        df = df[df['month']==month]

    # filter by day of week if applicable
    if day != 'all':
      # filter by day of week to create the new dataframe
        day = day.title()
        df = df[df['day_of_week']==day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("the most common month: "+str(df['month'].mode().iloc[0])+"\n")

    # TO DO: display the most common day of week
    print("the most common day of week: "+str(df['day_of_week'].mode().iloc[0])+"\n")


    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print("the most common start hour: "+str(df['hour'].mode().iloc[0]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("the most commonly used start station: "+str(df['Start Station'].mode().iloc[0])+"\n")


    # TO DO: display most commonly used end station
    print("the most commonly used  end station: "+str(df['End Station'].mode().iloc[0])+"\n")


    # TO DO: display most frequent combination of start station and end station trip
    df['rout'] = df['Start Station'] + " to " + df['End Station']
    print("the most frequent combination of start station and end station trip: "+str(df['rout'].mode().iloc[0]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    totalTravelTime = int(df['Trip Duration'].sum())
    totalTravelTime = datetime.timedelta(seconds=totalTravelTime)
    print("The total travel time "+str(totalTravelTime)+' hours \n')

    # TO DO: display mean travel time
    averageTravelTime = int(df['Trip Duration'].mode().iloc[0])
    averageTravelTime = datetime.timedelta(seconds=averageTravelTime)
    print("The average travel time "+str(averageTravelTime)+" hours")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("The count of subscribers: "+str(df['User Type'].value_counts().iloc[0])+'\n')
    print("The count of customers: "+str(df['User Type'].value_counts().iloc[1])+'\n')


    # TO DO: Display counts of gender
    print("The count of males: "+str(df['Gender'].value_counts().iloc[0])+'\n')
    print("The count of females: "+str(df['Gender'].value_counts().iloc[1])+'\n')



    # TO DO: Display earliest, most recent, and most common year of birth
    print("The earliest year of birth: "+str(int(df['Birth Year'].min()))+'\n')
    print("The most recent year of birth: "+str(int(df['Birth Year'].max()))+'\n')
    print("The most common year of birth: "+str(int(df['Birth Year'].mode().iloc[0])))



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        #ask the user if he wants to see raw data
        rawData = input('\nWould you like to see raw data? Enter yes or no.\n')
        i=5
        while(rawData.lower() == 'yes'):
            print(tabulate(df.iloc[np.arange(0+i,5+i)], headers ="keys"))
            i+=5
            rawData = input('\nWould you like to see raw data? Enter yes or no.\n')
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
