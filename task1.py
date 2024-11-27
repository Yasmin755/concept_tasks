#Task_1 :
steps_input=input("input the steps : ")
steps=list(map(int,steps_input.split(  ) ))
highest_steps=max(steps)
lowest_steps=min(steps)
avr_steps=sum(steps)/len(steps)
sort_steps=sorted(steps,reverse=True)
print(f"the highest steps : {highest_steps}" )
print(f"the lowest steps : {lowest_steps}" )
print(f"the average of steps : {avr_steps}")
print(f"Sorted steps :{sort_steps}")








