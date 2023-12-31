import charts
import pandas as pd

def run():
  df = pd.read_csv('./data.csv')
  df = df[df['Continent'] == 'South America']

  countries = df['Country/Territory'].values
  percentages = df['World Population Percentage'].values
  charts.generate_pie_chart(percentages, labels=countries)

if __name__ == '__main__':
  run()