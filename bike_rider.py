import datetime
import pandas as pd
import calendar
import sys
import matplotlib.pyplot as plt
import numpy as np


def plot_bar_day(rides):
    label = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    index = np.arange(len(label))
    plt.bar(index, rides, align='center', color = 'orange')
    plt.xlabel('Days', fontsize=10)
    plt.ylabel('No of Rides', fontsize=10)
    plt.xticks(index, label, fontsize=10, rotation=0) 
    plt.title('Analysis by Day')
    plt.show()
    return

def plot_bar_month(rides):
    label = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
    index = np.arange(len(label))
    plt.bar(index, rides, align='center', color = 'cyan')
    plt.xlabel('Days', fontsize=10)
    plt.ylabel('No of Rides', fontsize=10)
    plt.xticks(index, label, fontsize=10, rotation=0)
    plt.title('Analysis by Month')
    plt.show()
    return

def plot_graph(graph_values):
    #print(graph_values[3])
    
    label0 = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    index0 = np.arange(len(label0))
    plt.bar(index0, graph_values[0], align='center', color = 'orange')
    plt.xlabel('Days', fontsize=10)
    plt.ylabel('No of Rides', fontsize=10)
    plt.xticks(index0, label0, fontsize=10, rotation=0) 
    plt.title('Analysis by Day')

    plt.figure()
    label1 = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
    index1 = np.arange(len(label1))
    plt.bar(index1, graph_values[1], align='center', color = 'cyan')
    plt.xlabel('Months', fontsize=10)
    plt.ylabel('No of Rides', fontsize=10)
    plt.xticks(index1, label1, fontsize=10, rotation=0) 
    plt.title('Analysis by Month')
    
    plt.figure()
    label4 = ['Male', 'Female']
    index4 = np.arange(len(label4))
    plt.bar(index4, graph_values[4], align='center', color = 'green')
    plt.xlabel('Gender', fontsize=10)
    plt.ylabel('No of Rides', fontsize=10)
    plt.xticks(index4, label4, fontsize=10, rotation=0) 
    plt.title('Analysis by Gender')

    plt.figure()
    label5 = ['I Year', 'II Year', 'III Year', 'IV Year']
    index5 = np.arange(len(label5))
    plt.bar(index5, graph_values[5], align='center', color = 'magenta')
    plt.xlabel('Years', fontsize=10)
    plt.ylabel('No of Rides', fontsize=10)
    plt.xticks(index5, label5, fontsize=10, rotation=0) 
    plt.title('Analysis by Year')



    plt.figure()
    label2 = ['A-Block', 'B-Block', 'D-Block', 'E-Block', 'F-Block', 'Foodies', 'G-Block', 'GDN', 'K-Block', 'L-Block', 'Library', 'MB', 'SJT', 'SMV', 'TT']
    index2 = np.arange(len(label2))
    plt.bar(index2, graph_values[2], align='center', color = 'red')
    plt.xlabel('Start Stations', fontsize=10)
    plt.ylabel('No of Rides', fontsize=10)
    plt.xticks(index2, label2, fontsize=10, rotation=0) 
    plt.title('Analysis by Start Station')
  
    plt.figure()
    label3 = ['A-Block', 'B-Block', 'D-Block', 'E-Block', 'F_Block', 'Foodies', 'G-Block', 'GDN', 'K-Block', 'L-Block', 'Library', 'MB', 'SJT', 'SMV', 'TT']
    index3 = np.arange(len(label3))
    plt.bar(index3, graph_values[3], align='center', color = 'blue')
    plt.xlabel('End Stations', fontsize=10)
    plt.ylabel('No of Rides', fontsize=10)
    plt.xticks(index3, label3, fontsize=10, rotation=0) 
    plt.title('Analysis by End Station')



    plt.show()
    
    return


def input_campus():
  
    campus = input('\nWelcome to VIT Bike Rider!\n\n'
                 'Select Campus\n1.Vellore \n2.Chennai\n3.Bhopal\n4.Exit\n\nEnter your choice : ')
    if campus == 1:
        return 'vellore.csv'
    elif campus == 2:
        return 'chennai.csv'
    elif campus == 3:
        return 'bhopal.csv'
    elif campus == 4:
	print("\n\nThanks for using BIKE RIDER!!\n\n")
	sys.exit()
    else:
        print("\nInvalid Choice! Please try again.")
        return input_campus()


def input_time_period():
    
    time_period = input('\nFilter by\n1.Month\n2.Day\n3.None\n\nEnter your choice : ')
    if time_period == 1:
        return ['month', input_month()]
    elif time_period == 2:
        return ['day', input_day()]
    elif time_period == 3:
        return ['none', 'no filter']
    else:
        print("\nInvalid Choice! Please try again.")
        return input_time_period()


def input_month():
    
    month = input('\nSelect month\n1.January\n2.February\n3.March\n4.April\n5.May\n6.June\n\nEnter your choice : ')
    if month == 1:
        return '01'
    elif month == 2:
        return '02'
    elif month == 3:
        return '03'
    elif month == 4:
        return '04'
    elif month == 5:
        return '05'
    elif month == 6:
        return '06'
    else:
        print("\nInvalid Choice! Please try again.")
        return input_month()

def input_day():
    
    day_of_week = input('\nSelect Day\n1.Monday\n2.Tuesday\n3.Wednesday\n4.Thursday\n5.Friday\n6.Saturday\n7.Sunday\n\nEnter your choice : ')
    if day_of_week == 1:
        return 0
    elif day_of_week == 2:
        return 1
    elif day_of_week == 3:
        return 2
    elif day_of_week == 4:
        return 3
    elif day_of_week == 5:
        return 4
    elif day_of_week == 6:
        return 5
    elif day_of_week == 7:
        return 6
    else:
        print("\nInvalid Choice! Please try again.")
        return input_day()

def max_month(df):
    
    total_trips = df['Month'].count()
    trips_by_month = df.groupby('Month')['Start Time'].count()
    max_month_val = float(trips_by_month.sort_values(ascending=False).index[0])
    max_trips = list(trips_by_month.sort_values(ascending=False))
    #print(trips_by_month)
    trips_by_month = dict(trips_by_month)
    #print(trips_by_month)
    for i in range (1,7):
	cmp_val = '0' + str(i)
	if cmp_val in trips_by_month.keys():
		graph_values[1][i-1]=trips_by_month[cmp_val]
    
    #print(graph_values[1])
    max_trips = max_trips[0]
    
    return "Most popular month for start time: " + calendar.month_name[int(max_month_val)] + " (" + str(int(max_trips)) + " trips, " + '{0:.2f}%'.format(((float(max_trips)/total_trips) * 100)) + " of trips)"

def max_day(df):
    
    total_trips = df['Start Time'].count()
    trips_by_day_of_week = df.groupby('Day of Week')['Start Time'].count()
    max_day_val = float(trips_by_day_of_week.sort_values(ascending=False).index[0]) 
    max_trips = list(trips_by_day_of_week.sort_values(ascending=False))
    trips_by_day_of_week = (dict(trips_by_day_of_week))
    for i in range (7):
	if i in trips_by_day_of_week.keys():
		graph_values[0][i]=trips_by_day_of_week[i]
    
    #print(graph_values[0])
    max_trips = max_trips[0]
    
    return "Most popular day of the week for start time: " + calendar.day_name[int(max_day_val)] + " (" + str(int(max_trips)) + " trips, " + '{0:.2f}%'.format(((float(max_trips)/total_trips) * 100)) + " of trips)"


def max_hour(df):
  
    trips_by_hour_of_day = df.groupby('Hour of Day')['Start Time'].count()
    
    most_pop_hour_int = trips_by_hour_of_day.sort_values(ascending=False).index[0]
    d = datetime.datetime.strptime(most_pop_hour_int, "%H")
    max_trips = d.strftime("%I %p")
    return "Most popular hour of the day for start time: " + d.strftime("%I %p") 

def trip_duration(df):
    
    total_trip_duration = df['Trip Duration'].sum()
    avg_trip_duration = df['Trip Duration'].mean()
    m, s = divmod(total_trip_duration, 60)
    h, m = divmod(m, 60)
    d, h = divmod(h, 24)
    total_trip_duration = "\nTotal trip duration: %02d days %02d hrs %02d min %02d sec" % (d, h, m, s)
    m, s = divmod(avg_trip_duration, 60)
    h, m = divmod(m, 60)
    avg_trip_duration = "Average trip duration: %d hrs %02d min %02d sec" % (h, m, s)
    return [total_trip_duration, avg_trip_duration]

def max_stations(df):
   
    start_station_counts = df.groupby('Start Station')['Start Station'].count()
    end_station_counts = df.groupby('End Station')['End Station'].count()
    sorted_start_stations = start_station_counts.sort_values(ascending=False)
    sorted_end_stations = end_station_counts.sort_values(ascending=False)
    total_trips = df['Start Station'].count()
    most_popular_start_station = "\nMost popular start station: " + sorted_start_stations.index[0] + " (" + str(sorted_start_stations[0]) + " trips, " + '{0:.2f}%'.format(((float(sorted_start_stations[0])/total_trips) * 100)) + " of trips)"
    most_popular_end_station = "Most popular end station: " + sorted_end_stations.index[0] + " (" + str(sorted_end_stations[0]) + " trips, " + '{0:.2f}%'.format(((float(sorted_end_stations[0])/total_trips) * 100)) + " of trips)"
    

    labels = ['A - Block', 'B - Block', 'D - Block', 'E - Block', 'F - Block', 'Foodies', 'G - Block', 'GDN', 'K - Block', 'L - Block', 'Library', 'MB', 'SJT', 'SMV', 'TT']


    start_station_counts = dict(start_station_counts)
    end_station_counts = dict(end_station_counts)
   

    for i in range (len(labels)):
	if labels[i] in start_station_counts.keys():
		graph_values[2][i]=start_station_counts[labels[i]]
		
	if labels[i] in end_station_counts.keys():
		graph_values[3][i]=end_station_counts[labels[i]]


    return [most_popular_start_station, most_popular_end_station]


def max_trip(df):
    
    trip_counts = df.groupby(['Start Station', 'End Station'])['Start Time'].count()
    sorted_trip_stations = trip_counts.sort_values(ascending=False)
    total_trips = df['Start Station'].count()
    return "Most popular trip: " + "\n    Start station: " + str(sorted_trip_stations.index[0][0]) + "\n    End station: " + str(sorted_trip_stations.index[0][1]) + "\n    (" + str(sorted_trip_stations[0]) +  " trips, " + '{0:.2f}%'.format(((float(sorted_trip_stations[0])/total_trips) * 100)) + " of trips)"




def gender(df):
    
    gender_counts = df.groupby('Gender')['Gender'].count()
    try:
	gender_counts["Female"]
	flag1=1
    except:
	flag1=0
    try:
	gender_counts["Male"]
	flag2=1
    except:
	flag2=0

    if(flag1==1 and flag2==1):
	return_string = "Female: " + str(gender_counts["Female"]) + "\nMale: " + str(gender_counts["Male"])
	graph_values[4]=[gender_counts["Male"],gender_counts["Female"]]
    elif(flag1):
	return_string = "Female: " + str(gender_counts["Female"])
	graph_values[4]=[0,gender_counts["Female"]]
    elif(flag2):
	return_string ="Male: " + str(gender_counts["Male"])	
	graph_values[4]=[gender_counts["Male"],0]    

    return return_string


def year(df):
    
    least_year = "Youngest of year: " + str(int(df['Year'].min()))
    max_year = "Oldest of year: " + str(int(df['Year'].max()))
    year_counts = df.groupby('Year')['Year'].count()
    sorted_year = year_counts.sort_values(ascending=False)
    total_trips = df['Year'].count()
    graph_values[5]=list(year_counts)
    most_common_year = "Most common year: " + str(int(sorted_year.index[0])) + " (" + str(sorted_year.iloc[0]) + " trips, " + '{0:.2f}%'.format(((float(sorted_year.iloc[0])/total_trips) * 100)) + " of trips)"
    return [least_year, max_year, most_common_year]


def display_data(df, current_line):
    
    display = raw_input('\nWould you like to view individual trip data?'
                    ' Type \'yes\' or \'no\'.\n')
    display = display.lower()
    if display == 'yes' or display == 'y':
        print(df.iloc[current_line:current_line+5])
        current_line += 5
        return display_data(df, current_line)
    if display == 'no' or display == 'n':
        return
    else:
        print("\nI'm sorry, I'm not sure if you wanted to see more data or not. Let's try again.")
        return display_data(df, current_line)


def main_func():
    
    campus = input_campus()
    campus_df = pd.read_csv(campus)

    def day_of_week(str_date):
        
        date_obj = datetime.date(int(str_date[0:4]), int(str_date[5:7]), int(str_date[8:10]))
        return date_obj.weekday() 
    
    campus_df['Day of Week'] = campus_df['Start Time'].apply(day_of_week)
    campus_df['Month'] = campus_df['Start Time'].str[5:7]
    campus_df['Hour of Day'] = campus_df['Start Time'].str[11:13]

    time_period = input_time_period()
    filter_period = time_period[0]
    filter_period_value = time_period[1]
    filter_period_label = 'No filter'

    if filter_period == 'none':
        filtered_df = campus_df
    elif filter_period == 'month':
        filtered_df = campus_df.loc[campus_df['Month'] == filter_period_value]
        filter_period_label = calendar.month_name[int(filter_period_value)]
    elif filter_period == 'day':
        filtered_df = campus_df.loc[campus_df['Day of Week'] == filter_period_value]
        filter_period_label = calendar.day_name[int(filter_period_value)]

    print('\n')
    print(campus[:-4].upper().replace("_", " ") + ' -- ' + filter_period_label.upper())
    print('-------------------------------------')

    print('Total trips: ' + "{:,}".format(filtered_df['Start Time'].count()))

    if filter_period == 'none' or filter_period == 'day':
        print(max_month(filtered_df))

    if filter_period == 'none' or filter_period == 'month':
        print(max_day(filtered_df))

    print(max_hour(filtered_df))

    trip_duration_stats = trip_duration(filtered_df)
    print(trip_duration_stats[0])
    print(trip_duration_stats[1])

    most_max_stations = max_stations(filtered_df)
    print(most_max_stations[0])
    print(most_max_stations[1])

    print(max_trip(filtered_df))

    print('')
    print(gender(filtered_df))

    year_data = year(filtered_df)
    print('')
    print(year_data[0])
    print(year_data[1])
    print(year_data[2])

    display_data(filtered_df, 0)
    graphs = raw_input('\nWould you like Graphs? Type \'yes\' or \'no\'.\n')
    if graphs.lower() == 'yes' or graphs.lower() == 'y':
	plot_graph(graph_values)

    def restart():
        
        restart = raw_input('\nWould you like to restart? Type \'yes\' or \'no\'.\n')
        if restart.lower() == 'yes' or restart.lower() == 'y':
            main_func()
        elif restart.lower() == 'no' or restart.lower() == 'n':
            print("\n\nThanks for using BIKE RIDER!!\n\n")
	    return
        else:
            print("\nInvalid Choice! Please try again.")
            return restart()

    restart()


if __name__ == "__main__":
    graph_values=[[0]*7, [0]*6, [0]*15, [0]*15, [0]*2, [0]*4]
    main_func()
