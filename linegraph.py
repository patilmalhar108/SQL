import matplotlib.pyplot as plt
x = [0,5,10,15,20,25,30]
y1 = [10,15,20,20,13,15,0]
y2 = [10,12,15,12,20,10,0]
plt.plot(x,y1,linestyle = "dashed",marker = "D")
plt.plot(x,y2,linestyle = "dashed", marker = "D")
plt.title('Velocity time graph')
plt.xlabel('Velocity m/s')
plt.ylabel('Time(s)')
plt.xlim(5,25)
plt.ylim(5,25)
plt.legend()
plt.show()