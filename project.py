import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import style
style.use('ggplot')

var = pd.read_excel(r'D:\python\MyProject\project6\Excel.xlsx')


plt.plot(var['date'], var['time'], label=' Useful ', linewidth=1.5, color='deeppink')
plt.plot(var['date'], var['total'], label=' Total ', linewidth=1.5, color='slategrey')

plt.xlabel('Date')
plt.ylabel('Time(hour)')
plt.title('The report of my activity in 4 month ')
plt.legend()
plt.show()
