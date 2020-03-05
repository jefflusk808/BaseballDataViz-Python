import pandas as pd
import matplotlib.pyplot as plt
from data import games


#filtering for only attendance data and then creating a new dataframe for only that.
attendance = games.loc[((games['type'] == 'info') & (games['multi2'] == 'attendance')), ['year', 'multi3']]
attendance.columns = ["year", "attendance"]


#converting the attendance numbers to numeric
attendance.loc[:, 'attendance'] = pd.to_numeric(attendance.loc[:, 'attendance'])

#configuring plot parameters
attendance.plot(x='year', y='attendance', figsize=(15, 7), kind='bar')

#updating axis labels
plt.xlabel('Year')
plt.ylabel('Attendance')

#adding in the mean
plt.axhline(y=attendance['attendance'].mean(), label='Mean', color='green', linestyle='--')

#shows the plot
plt.show()

print(attendance.head())