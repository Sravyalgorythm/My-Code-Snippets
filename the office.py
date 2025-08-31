
#Plotting the number of Sales made per year by 5 employees in an office. 
import matplotlib.pyplot as plt
y=[25,26,36,42,100]
x=['Phyllis','Jim','Dwight','Michael', 'Creed']
plt.bar(x,y, color=['Darkslateblue','LightBlue','goldenrod','dimgrey','Black'], width=0.6)
plt.xlabel('Employees')
plt.ylabel('Sales per year')
plt.title('The Office')
plt.show()
