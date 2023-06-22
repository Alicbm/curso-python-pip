import matplotlib.pyplot as plt

def generate_bar_chart(name, labels, values):
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  plt.savefig(f'{name}.png')
  plt.close()

def generate_pie_chart(values, labels):  
  fig, ax = plt.subplots()
  ax.pie(values, labels=labels)
  ax.axis('equal')
  plt.savefig('pie.png')
  plt.close()

if __name__ == '__main__':
  a = ['a', 'b', 'c']
  b = [100, 200, 80]
  generate_bar_chart(a, b)
