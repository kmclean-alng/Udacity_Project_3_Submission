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
    choiceCity="0"
    validCity = 0
    while validCity !=1:
        choiceCity = input("Would you like to see information for chicago, new york city or washington\n")
        if (choiceCity.upper() == "CHICAGO") | (choiceCity.upper() == "WASHINGTON") | (choiceCity.upper() == "NEW YORK CITY"):
            validCity = 1
        else:
            print("Invalid choice , please re-enter below")
        #endif
    #endwhile         

    # TO DO: get user input for month (all, january, february, ... , june)
    
    choiceMonth = "0"
    validMonth = 0
    while validMonth !=1:
        choiceMonth = input("Plese select a month: All, January, February, March, April, May, June\n")
        if (choiceMonth.upper() in ["ALL", "JANUARY", "FEBRUARY", "MARCH", "APRIL", "MAY", "JUNE"]):
            validMonth = 1
        else:
            print("Invalid choice, please re-enter below")
        #endif
    #endwhile

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    
    choiceDay = "0"
    validDay = 0
    while validDay !=1:
        choiceDay = input("Plese select a day: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday\n")
        if (choiceDay.upper() in ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY", "ALL"]):
            validDay = 1
        else:
            print("Invalid choice, please re-enter below")
        #endif
    #endwhile

    city = choiceCity.lower()
    month = choiceMonth.lower()
    day = choiceDay.lower()

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

    df =pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    monthnum = {'january':1,'february':2, 'march':3, 'april':4, 'may':5, 'june':6}

    df['month']=df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name


    if month != 'all':
        monthN = monthnum[month]
        df = df[df['Start Time'].dt.month == monthN]

    if day != 'all':
        df = df[df['Start Time'].dt.weekday_name == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    mode_month=df['month'].mode()[0]
    print("The most common month was %s" %months[mode_month-1])

    # TO DO: display the most common day of week

    mode_day=df['day_of_week'].mode()[0]
    print("The most common day of the week was %s" %mode_day)

    # TO DO: display the most common start hour
    mode_hour=df['Start Time'].dt.hour.mode()[0]
    print("The most common hour was %s" %mode_hour )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    mode_sstation = df['Start Station'].mode()[0]
    print("The most common start station was %s" %mode_sstation )

    # TO DO: display most commonly used end station
    mode_estation = df['End Station'].mode()[0]
    print("The most common end station was %s" %mode_estation )

    # TO DO: display most frequent combination of start station and end station trip
    mode_sestation = (df['Start Station']+' to '+df['End Station']).mode()[0]
    print("The most common station combination was %s" %mode_sestation )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time  = df['Trip Duration'].sum()
    print("The total travel time was %s" %total_time )

    # TO DO: display mean travel time
    mean_time =df['Trip Duration'].mean()
    print("The mean travel time was %s" %mean_time )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    #Displays counts of user types
    user_type= df['User Type'].value_counts()
    print(user_type.to_string())
    print("\n")

    if ("Gender" in df):
        #do not run code if washington

        #Displays counts of gender
        gender_count = df['Gender'].value_counts()
        print(gender_count.to_string())

        # TO DO: Display earliest, most recent, and most common year of birth
        earliest_by = df['Birth Year'].min()
        print("The earliest birth year was %s" %int(earliest_by))

        recent_by = df['Birth Year'].max()
        print("The most recent birth year was %s" %int(recent_by))

        common_by = df['Birth Year'].mode()[0]
        print("The most common birth year was %s" %int(common_by))
        print("\n")



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def raw_data(df):
    """Allows user to request raw data"""

    #allows user to request as much data as wanted
    iterator = 0

    #controls looping
    want = True

    while (want):
        y=0
        wantdata=input("Do you want some raw data?\n")

        if (wantdata=="1")|(wantdata.lower() == "yes")|(wantdata=="y"):
            y = input("how many rows:  ")

            if y.isdigit():
                if (iterator+int(y)>len(df.index)):
                    print("More data requested than available try again")
                    y="0"
                #endif
                print(df.iloc[iterator:iterator+int(y)].to_string())
                #endfor
                iterator = iterator + int(y)
            else:
                print("\nNot a number so you don't want raw data :-( \n")
        else:
            want = False
        #endif

    #endwhile

    print('-'*40)



def main():
    #Main program
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        #comment to change in git
        #In fact, this line improves readability
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
            #end program


if __name__ == "__main__":
	main()
#additional comment