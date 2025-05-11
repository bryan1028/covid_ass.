# COVID-19 Analysis - Complete Working Script
import pandas as pd
import matplotlib.pyplot as plt

# 1. Load Data
print("🌍 Loading COVID-19 data...")
url = "https://covid.ourworldindata.org/data/owid-covid-data.csv"
df = pd.read_csv(url)

# 2. Process Data
countries = ['Kenya', 'United States', 'India', 'Germany']
df = df[df['location'].isin(countries)][['date','location','total_cases','total_deaths']]
df['date'] = pd.to_datetime(df['date'])

# 3. Generate Plot
plt.figure(figsize=(10,5))
for country in countries:
    country_data = df[df['location'] == country]
    plt.plot(country_data['date'], country_data['total_cases'], label=country)
plt.title('COVID-19 Cases by Country')
plt.legend()
plt.tight_layout()
plt.savefig('covid_results.png')  # Saves the plot
print("✅ Analysis complete! Check covid_results.png")