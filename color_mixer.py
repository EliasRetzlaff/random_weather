def random_data():
    import pandas as pd
    import random
    from datetime import datetime, timedelta

    # Define the date range
    start_date = datetime.strptime("5/1/23", "%m/%d/%y")
    end_date = datetime.strptime("10/22/23", "%m/%d/%y")
    date_range = pd.date_range(start=start_date, end=end_date)

    # Define weekdays
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    # Generate random weather and temperature data
    weather_conditions = ['Sunny', 'Partly Cloudy', 'Cloudy', 'Rain', 'Thunderstorm', 'Snow']
    temperatures = range(40, 91)  # Temperature range from 40°F to 90°F

    # Create a list to hold the data
    data = []

    # Generate random data for each date
    for date in date_range:
        weekday = weekdays[date.weekday()]
        weather = random.choice(weather_conditions)
        temperature = random.choice(temperatures)
        data.append([date.strftime("%m/%d/%y"), weekday, weather, temperature])

    # Create a DataFrame from the data
    df = pd.DataFrame(data, columns=['Date', 'Weekday', 'Weather', 'Temperature'])

    # Export the DataFrame to a CSV file
    df.to_csv('generated_data.csv', index=False)
