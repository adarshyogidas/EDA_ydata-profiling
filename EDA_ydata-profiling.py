# Install the ydata-profiling package 
!pip install ydata_profiling

# Import necessary libraries
import pandas as pd
import seaborn as sns
from ydata_profiling import ProfileReport

# Load the Titanic dataset from Seaborn
data = sns.load_dataset('titanic')

# Create a profile report using ydata-profiling
profile = ProfileReport(data, title="Titanic Dataset Report", explorative=True)

# Save the report to an HTML file
profile.to_file("titanic_report.html")