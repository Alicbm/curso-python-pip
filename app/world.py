import csv
import charts

def read_csv(path):
  with open(path, 'r') as file:
    reader = csv.reader(file, delimiter=',')
    header = next(reader)

    reader = list(reader)
    #result = []

    name_country = []
    population_porcent = []
    
    for row in reader:
      data = dict(zip(header, row))
      #data_transformed = { key: value for key, value in data }
      name_country.append(data['Country/Territory'])
      population_porcent.append(float(data['World Population Percentage']))
      
      #response = { name_country: population_porcent }
      #result.append(response)  
    charts.generate_pie_chart(population_porcent, labels=name_country)

if __name__ == '__main__':
  read_csv('./app/data.csv')