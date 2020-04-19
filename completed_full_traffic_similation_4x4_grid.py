# -*- coding: utf-8 -*-

""" Traffic Simulation Code of a 4x4 grid based on stochastic kinetic theory model

array car1 holds properties of each car [x-position,y-position,velocity,lane,direction]
array gridp[] holds the arrays representing roads. Position of the array has or does not have a car
array count[] holds the number of hits at crossroads
each road is represented by an array where each cell is either 1 or 0 - has a car or doesnt have a car





direction representation                        0==UP    
                                 2==LEFT                3==RIGHT
                                               1==DOWN 
Lane arrays: 

   0=↑ 6=↓             1=↑ 7=↓                 2=↑  8=↓
    
    
                         9=←                                   
                         3=→


                        4=→
                        10=←
                        
                        
                        5=→
                        11=←
                        
                        
                        
                        
The motion of car is treated separately and as follows:

1. Each car wants to drive at the speed limit and so if velocity of car (V) is below the speed limit V max; V is increased by 1 

2. Cars drive in either positive/negative x−direction or positive/negative y−direction and they don’t want to hit the car in front. 
If a car is at position i and the car in front is at site i + d then if V ≥ d, V is set equal to d −1. 
This stops the cars from accelerating and hitting the car in front 

3. Unexpected events cause slowing down. This is a random component that is intended to model external inﬂuences, such as what is happening
 on the other carriageway, or just irrational behaviour by drivers. If V > 0 then, with a probability P, V is reduced to V −1. 
 There is also constant standing chance of a total car breakdown where V is set to 0, this has 1% of occurring. 
 All of this happens after V has been updated by the ﬁrst two rules. 4. Each vehicle is moved forward V places, using the new value of V
 
When approaching cross roads:
    
1. If a car has approached the crossroads,it has tos top (V = 0) at the ”trafﬁclightposition” a position just before the center of cross roads. 

2. When the car has stopped it has to decide where to go, this is done randomly
 
3. When the car has decided its direction and it is the cars turn to drive it will check if the position it wants to go to is occupied. If it is occupied the car waits at its current position and ends it turn of movement. If the position is unoccupied the car goes to that position.
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        

"""
from math import fabs
import random
import numpy as np
import matplotlib.pyplot as plt
import time

start_time = time.time()


""" 
#############################
############################
############################

SET OUR PARAMETERS

###########################
##########################
##########################
"""

length_of_road=100 
number_of_cars=192

Vmax=5  #Max Velocity of Cars

break_down_chance=25/100







num_per_lane=int(number_of_cars/4)
v=np.random.rand(number_of_cars) #generate random velocities
v2=np.round(v*Vmax,decimals=0)

count=np.zeros(5)
n=99


#DRIVING RIGHT START POSITIONS
x_positions0=random.sample(range(int(length_of_road)), num_per_lane)
x_positions0=np.negative(x_positions0)
y_positions0=np.zeros(num_per_lane)
y_positions0.fill(50)



#DRIVING LEFT START POSTIONS
x_positions1=random.sample(range(int(length_of_road)), num_per_lane)
#x_positions=np.negative(x_positions)
y_positions1=np.zeros(num_per_lane)
y_positions1.fill(49)


#DRIVING UP START POSITIONS
y_positions2=random.sample(range(int(length_of_road*0.5)), num_per_lane)
x_positions2=np.zeros(num_per_lane)
x_positions2.fill(0)



#DRIVING DOWN START POSITIONS
y_positions3=random.sample(range(51,int(length_of_road)), num_per_lane)
x_positions3=np.zeros(num_per_lane)
x_positions3.fill(1)



x=np.append(x_positions0,x_positions1)                 
x=np.append(x,x_positions2)
x=np.append(x,x_positions3)
y=np.append(y_positions0,y_positions1)
y=np.append(y,y_positions2)
y=np.append(y,y_positions3)

car1=np.vstack((x,y))

grid0=np.empty(length_of_road*2)
grid1=np.empty(length_of_road*2)
grid2=np.empty(length_of_road*2)
grid3=np.empty(length_of_road*2)
grid4=np.empty(length_of_road*2)
grid5=np.empty(length_of_road*2)
grid6=np.empty(length_of_road*2)
grid7=np.empty(length_of_road*2)
grid8=np.empty(length_of_road*2)
grid9=np.empty(length_of_road*2)
grid10=np.empty(length_of_road*2)
grid11=np.empty(length_of_road*2)

car1=np.vstack((car1,v2))


#Set Initial Lanes for all cars
lane=np.zeros(number_of_cars)
lane[[range(num_per_lane)]]=4
lane[[range(num_per_lane,num_per_lane*2)]]=10
lane[[range(num_per_lane*2,num_per_lane*3)]]=1
lane[[range(num_per_lane*3,num_per_lane*4)]]=7

#lane.fill(1)
car1=np.vstack((car1,lane))
direction=np.zeros(number_of_cars)


#Set Initial Direction for all cars
direction[[range(num_per_lane)]]=3
direction[[range(num_per_lane,num_per_lane*2)]]=2
direction[[range(num_per_lane*2,num_per_lane*3)]]=0
direction[[range(num_per_lane*3,num_per_lane*4)]]=1
car1=np.vstack((car1,direction))
distace_travelled=np.zeros(number_of_cars)
car1=np.vstack((car1,distace_travelled))
print(car1)    
data=np.transpose(car1)


ARRAY=np.column_stack((grid0,grid1,grid2,grid3,grid4,grid5,grid6,grid7,grid8,grid9,grid10,grid11))

with open(r"fulldata2.txt", "w") as f:
    np.savetxt(f, data)

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)


#Animation funciton 
def animate(h):


    graph_data = open(r"fulldata2.txt",'r').read()
    lines = graph_data.split('\n')
    xs = []
    ys = []
    vel=[]
    for line in lines:
        if len(line) > 1:
            x, y ,x_vel,y_vel,direc,dis = line.split(' ')
            xs.append(float(x))
            ys.append(float(y))
            vel.append(float(x_vel))
    ax1.clear()
    plt.ylim(0,length_of_road)
    plt.xlim(-length_of_road,length_of_road)
    plt.title("Time "+str(h) + " Number of cars " + str(number_of_cars)+ " Breakdown chance " +str(break_down_chance) + " Velocity " + str(Vmax))
    #ax1.set_yticks(np.arange(0,length_of_road,1))
    #ax1.set_xticks(np.arange(0,length_of_road,1))
    ax1.scatter(xs, ys, s=10, c=vel, linestyle='-', linewidth=1 )
    ax1.grid(b=True,axis='y',alpha=1)
    
    plt.pause(0.05)
    
    
    
""" 
FUNCTION : drive_y


Cars driving in the y-direction 
    array parametes: Car= car parameters, 
                     grid_lock=array of the road which the car is driving in
                     j,j1= seekers to see if there is a car infront 
                     i= which car
                     loop= when to cancel loop where there is a car infront or unobstructed drive
                     sign= drive positive or negative y

    j and j1 seeking logic: 
    j and j1 go 2 steps ahead to see if position is occupied upto 5 steps 
    i.e go j=1 j1=2   if position 1 is empty and position 2 is occupied go to position 1 and so on
                      if all positions are empty upto 1,2,3,4,5 it is an unobstructed drive so stop at position 5
""" 
def drive_y(car,grid_lock,j,i,j1,loop, sign):
    j=j*sign
    j1=j1*sign
    if car[1,i]+j1<length_of_road+10:
        
        if grid_lock[int(car[1,i])+j,int(car[3,i])] ==1 :
            #print("car in front ")
            car[2,i]=0
            loop=False
            return car,grid_lock,loop
        
        
        
        elif fabs(j1)>car[2,i] :
            #print("unobstructed drive")
            grid_lock[int(car[1,i]),int(car[3,i])]=0
            car[1,i]=car[1,i]+j    
                
            grid_lock[int(car[1,i]),int(car[3,i])]=1
            loop= False
            return car,grid_lock,loop
                                        
                                        
        elif grid_lock[int(car[1,i])+j,int(car[3,i])] !=1 and grid_lock[int(car[1,i])+j1,int(car[3,i])] !=1  : 
            #print(" we can keep driving")
            loop=True
            return car,grid_lock,loop
                
        elif grid_lock[int(car[1,i])+j,int(car[3,i])] !=1 and grid_lock[int(car[1,i])+j1,int(car[3,i])] ==1 :
            #print("Space occupied in front ")
            grid_lock[int(car[1,i]),int(car[3,i])]=0
            grid_lock[int(car[1,i])+j,int(car[3,i])]=1 
            car[2,i]=fabs(j)
            car[1,i]=car[1,i]+j

            return car,grid_lock,loop
    

""" 
FUNCTION : drive_x


Cars driving in the x-direction 
    array parametes: Car= car parameters, 
                     grid_lock=array of the road which the car is driving in
                     j,j1= seekers to see if there is a car infront 
                     i= which car
                     loop= when to cancel loop where there is a car infront or unobstructed drive
                     sign= drive positive or negative y

    j and j1 seeking logic: 
    j and j1 go 2 steps ahead to see if position is occupied upto 5 steps 
    i.e go j=1 j1=2   if position 1 is empty and position 2 is occupied go to position 1 and so on
                      if all positions are empty upto 1,2,3,4,5 it is an unobstructed drive so stop at position 5
""" 

    
def drive_x(car,grid_lock,j,i,j1,loop,sign):
    j=j*sign
    j1=j1*sign
    #print(grid_lock)
    #print(j)
    #print(j1)
    if car[0,i]+j1<length_of_road*2:
        
        if grid_lock[int(car[0,i])+n+j,int(car[3,i])] ==1:
            #print("car in front right ")
            car[2,i]=0
            loop=False
            return car,grid_lock,loop
        
        
        
        elif fabs(j1)>car[2,i] :
            #print("unobstructed drive right")
            grid_lock[int(car[0,i])+n,int(car[3,i])]=0
            car[0,i]=car[0,i]+j   
                
            grid_lock[int(car[0,i])+n,int(car[3,i])]=1
            loop=False
            return car,grid_lock,loop
                                        
                                        
        elif grid_lock[int(car[0,i])+j+n,int(car[3,i])] !=1 and grid_lock[int(car[0,i])+j1+n,int(car[3,i])] !=1 : 
            #print(" we can keep driving right")
            loop=True
            return car,grid_lock,loop
                
        elif grid_lock[int(car[0,i])+j+n,int(car[3,i])] !=1 and grid_lock[int(car[0,i])+j1+n,int(car[3,i])] ==1 :
            #print("Space occupied in front right ")
            grid_lock[int(car[0,i])+n,int(car[3,i])]=0
            grid_lock[int(car[0,i])+j+n,int(car[3,i])]=1 
            car[2,i]=fabs(j)
            car[0,i]=car[0,i]+j
            loop=False
            return car,grid_lock,loop
        
""" 
FUNCTION : drive

Driving Functions decides which function to call for the driving direction of the car positive/negative x or y
    the function to call depends on direction parameter of array car i.e. car[4,i]==direction of car i

"""

def drive(car,grid_lock,j,i,j1,loop):
        if car[4,i]==0:#forward
            drive_y(car,grid_lock,j,i,j1,loop,1)
        elif car[4,i]==1:#backward
            drive_y(car,grid_lock,j,i,j1,loop,-1)
        elif car[4,i]==2:#left
            drive_x(car,grid_lock,j,i,j1,loop,-1)
        elif car[4,i]==3:#right
            drive_x(car,grid_lock,j,i,j1,loop,1)
        return car,grid_lock,loop
    
    
"""
FUNCTION : central_crossroads


Logic for the motion of cars at the central cross roads 

    the motion of cars is random but the car cant return to direction it was driving from i.e. cant do a U-turn
    the logic for crossroads is primitive a better way would to find an algorith for relating all position where the car stops before the 
    red traffic light and all the positons the car goes to when there is a green light
    
new parameters added: 
    stop_position_x = the position at the cross-roads the car has to stop at if the disired driving location is occupied
                      the position is just before the red light
    stop_position_y = the position at the cross-roads the car has to stop at if the disired driving location is occupied
                      the position is just before the red light   
    block_road= which direction of road to block when choosing direction of drive i.e. coming from left side the car cant drive back to left side 

"""    

    
def central_crossroad(car,grid,j,i,j1,stop_position_x,stop_position_y,block_road):
    car[2,i]=0#car needs to stop at traffic light
    print("WE ARE AT CENTRAL CROSS ROADS")
    random1=list(range(0,4))
    random1.remove(block_road)
    which_way=random.choice(random1)
    print(which_way)
    count[0]=count[0]+1
    if which_way==0 and grid[51,1]==1: #driving forward

        print("FORWARD POSITION OCCUPIED")
        car[0,i]=stop_position_x
        car[1,i]=stop_position_y
        car[2,i]=0
        if int(car[3,i])==10 or int(car[3,i])==4:
            grid[int(car[0,i])+n,int(car[3,i])]=1
        elif int(car[3,i])==1 :
            grid[int(car[1,i]),int(car[3,i])]=1
        ARRAY=grid
    elif which_way==0 and grid[51,1]!=1 :
        print("POSITIVE Y")
        car[3,i]=1
        car[1,i]=51
        car[0,i]=0
        grid[51,1]=1
        car[4,i]=0
        ARRAY=grid
    if which_way==2 and grid[-1+n,10]==1: #driving left
        print("LEFT POSITION OCCUPIED")
        car[0,i]=stop_position_x
        car[1,i]=stop_position_y
        car[2,i]=0
        if int(car[3,i])==10:
            grid[int(car[0,i])+n,int(car[3,i])]=1
        elif int(car[3,i])==1 or int(car[3,i])==7:
            grid[int(car[1,i]),int(car[3,i])]=1
        ARRAY=grid
    elif which_way==2  and grid[-1+n,10]!=1:
        print("NEGATIVE X")
        car[3,i]=10
        car[1,i]=49
        car[0,i]=-1
        grid[-1+n,10]=1
        car[4,i]=2
        ARRAY=grid
    if which_way==3 and (grid[2+n,4]==1): #driving right
        print("RIGHT POSITION OCCUPIED")
        car[0,i]=stop_position_x
        car[1,i]=stop_position_y
        car[2,i]=0
        if int(car[3,i])==4:
            grid[int(car[0,i])+n,int(car[3,i])]=1
        elif int(car[3,i])==1 or int(car[3,i])==7:
            grid[int(car[1,i]),int(car[3,i])]=1
        ARRAY=grid
    elif which_way==3  and grid[2+n,4]!=1:
        print("POSITIVE X")
        car[3,i]=4
        car[1,i]=50
        car[0,i]=2
        grid[2+n,4]=1
        car[4,i]=3
        ARRAY=grid
    if which_way==1 and (grid[48,7]==1): #driving down
        print("DOWN POSITION OCCUPIED")
        car[0,i]=stop_position_x
        car[1,i]=stop_position_y
        car[2,i]=0
        if int(car[3,i])==4 or int(car[3,i])==10:
            grid[int(car[0,i])+n,int(car[3,i])]=1
        elif int(car[3,i])==7:
            grid[int(car[1,i]),int(car[3,i])]=1
        ARRAY=grid
    elif which_way==1  and grid[48,7]!=1:
        print("NEGATIVE Y")
        car[3,i]=7
        car[1,i]=48
        car[0,i]=1
        grid[48,7]=1
        car[4,i]=1
        ARRAY=grid
    return car,ARRAY


"""
FUNCTION : upper_crossroads


Logic for the motion of cars at the upper cross roads 

    the motion of cars is random but the car cant return to direction it was driving from i.e. cant do a U-turn
    the logic for crossroads is primitive a better way would to find an algorith for relating all position where the car stops before the 
    red traffic light and all the positons the car goes to when there is a greenligh
    
new parameters: 
    stop_position_x = the position at the cross-roads the car has to stop at if the disered driving location is occupied
                      the position is just before the red light
    stop_position_y = the position at the cross-roads the car has to stop at if the disered driving location is occupied
                      the position is just before the red light   
    block_road= which direction of road to block when choosing direction of drive i.e. coming from left side the car cant drive back to left side 

"""   
        
def upper_crossroads(car,grid,j,i,j1,stop_position_x,stop_position_y,block_road):
    car[2,i]=0#car needs to stop at traffic light
    print("WE ARE AT UPPER CROSS ROADS")
    random1=list(range(1,4))
    random1.remove(block_road)
    which_way=random.choice(random1)
    print(which_way)
    count[1]=count[1]+1
    if which_way==2 and (grid[-1+n,9]==1): #driving left
        print("FRONT LEFT POSITION OCCUPIED")
        car[0,i]=stop_position_x
        car[1,i]=stop_position_y
        car[2,i]=0
        if int(car[3,i])==9:
            grid[int(car[0,i])+n,int(car[3,i])]=1
        elif int(car[3,i])==1:
            grid[int(car[1,i]),int(car[3,i])]=1
        ARRAY=grid
    elif which_way==2 and grid[-1+n,9]!=1 :
        print("NEGATIVE X")
        car[3,i]=9
        car[1,i]=98
        car[0,i]=-1
        grid[-1+n,9]=1
        car[4,i]=2
        ARRAY=grid
    if which_way==3 and grid[2+n,3]==1: #driving right
        print("FRONT RIGHT POSITION OCCUPIED")
        car[0,i]=stop_position_x
        car[1,i]=stop_position_y
        car[2,i]=0
        if int(car[3,i])==3:
            grid[int(car[0,i])+n,int(car[3,i])]=1
        elif int(car[3,i])==1:
            grid[int(car[1,i]),int(car[3,i])]=1
        ARRAY=grid
    elif which_way==3 and grid[2+n,3]!=1 :
        print("POSITIVE X")
        car[3,i]=3
        car[1,i]=99
        car[0,i]=2
        grid[2+n,3]=1
        car[4,i]=3
        ARRAY=grid
    if which_way==1 and grid[97,7]==1:#driving down
        print("Top Bottom POSITION OCCUPIED")
        car[0,i]=stop_position_x
        car[1,i]=stop_position_y
        car[2,i]=0
        if int(car[3,i])==3 or int(car[3,i])==9 :
            grid[int(car[0,i])+n,int(car[3,i])]=1
        ARRAY=grid
    elif which_way==1 and grid[97,7]!=1 :
        print("Negative Y")
        car[3,i]=7
        car[1,i]=97
        car[0,i]=1
        grid[97,7]=1
        car[4,i]=1      
        ARRAY=grid
    return car,ARRAY


"""
FUNCTION : left_crossroads

Logic for the motion of cars at the Left cross roads 

    the motion of cars is random but the car cant return to direction it was driving from i.e. cant do a U-turn
    the logic for crossroads is primitive a better way would to find an algorith for relating all position where the car stops before the 
    red traffic light and all the positons the car goes to when there is a greenligh
    
new parameters: 
    stop_position_x = the position at the cross-roads the car has to stop at if the disered driving location is occupied
                      the position is just before the red light
    stop_position_y = the position at the cross-roads the car has to stop at if the disered driving location is occupied
                      the position is just before the red light   
    block_road= which direction of road to block when choosing direction of drive i.e. coming from left side the car cant drive back to left side 

"""   


def left_crossroads(car,grid,j,i,j1,stop_position_x,stop_position_y,block_road):
    count[3]=count[3]+1
    car[2,i]=0#car needs to stop at traffic light
    print("WE ARE AT LEFT CROSS ROADS")
    random1=list(range(0,4))
    random1.remove(block_road)
    random1.remove(2)
    which_way=random.choice(random1)
    print(which_way)
    if which_way==3 and (grid[-97+n,4]==1): #driving right
        print("MIDDLE RIGHT POSITION OCCUPIED")
        car[0,i]=stop_position_x
        car[1,i]=stop_position_y
        car[2,i]=0
        if int(car[3,i])==0 or int(car[3,i])==6 :
            grid[int(car[1,i]),int(car[3,i])]=1
        ARRAY=grid
    elif which_way==3 and (grid[-97+n,4]!=1) :
        print("POSITIVE X")
        car[3,i]=4
        car[1,i]=50
        car[0,i]=-97
        grid[-97+n,4]=1
        car[4,i]=3
        ARRAY=grid
    if which_way==1 and grid[48,6]==1 :#driving down
        print("MIDDLE BOTTOM POSITION OCCUPIED")
        car[0,i]=stop_position_x
        car[1,i]=stop_position_y
        car[2,i]=0
        if int(car[3,i])==10:
            grid[int(car[0,i])+n,int(car[3,i])]=1
        elif int(car[3,i])==6:
            grid[int(car[1,i]),int(car[3,i])]=1
        ARRAY=grid

    elif which_way==1 and grid[48,6]!=1  :
        print("Negative Y")
        car[3,i]=6
        car[1,i]=48
        car[0,i]=-98
        grid[48,6]=1
        car[4,i]=1      
        ARRAY=grid

    if which_way==0 and grid[51,0]==1:#driving up
        print("MIDDLE TOP POSITION OCCUPIED")
        car[0,i]=stop_position_x
        car[1,i]=stop_position_y
        car[2,i]=0
        if int(car[3,i])==10:
            grid[int(car[0,i])+n,int(car[3,i])]=1
        elif int(car[3,i])==0:
            grid[int(car[1,i]),int(car[3,i])]=1
        ARRAY=grid

    elif which_way==0 and grid[51,0]!=1 :
        print("POSITIVE Y")
        car[3,i]=0
        car[1,i]=51
        car[0,i]=-99
        grid[51,0]=1
        car[4,i]=0
        ARRAY=grid
    return car,ARRAY
        
"""
FUNCTION : lower_crossroads



Logic for the motion of cars at the Lower cross roads 

    the motion of cars is random but the car cant return to direction it was driving from i.e. cant do a U-turn
    the logic for crossroads is primitive a better way would to find an algorith for relating all position where the car stops before the 
    red traffic light and all the positons the car goes to when there is a greenligh
    
new parameters: 
    stop_position_x = the position at the cross-roads the car has to stop at if the disered driving location is occupied
                      the position is just before the red light
    stop_position_y = the position at the cross-roads the car has to stop at if the disered driving location is occupied
                      the position is just before the red light   
    block_road= which direction of road to block when choosing direction of drive i.e. coming from left side the car cant drive back to left side 

"""   

def lower_crossroads(car,grid,j,i,j1,stop_position_x,stop_position_y,block_road):
    count[2]=count[2]+1
    car[2,i]=0#car needs to stop at traffic light
    print("WE ARE AT LOWER CROSS ROADS")
    random1=list(range(0,4))
    random1.remove(block_road)
    random1.remove(1)
    which_way=random.choice(random1)
    print(which_way)
    if which_way==2 and (grid[-1+n,11]==1): #driving left
        print("BOTTOM LEFT POSITION OCCUPIED")
        car[0,i]=stop_position_x
        car[1,i]=stop_position_y
        car[2,i]=0
        if int(car[3,i])==11:
            grid[int(car[0,i])+n,int(car[3,i])]=1
        elif int(car[3,i])==7:
            grid[int(car[1,i]),int(car[3,i])]=1
        ARRAY=grid

    elif which_way==2 and (grid[-1+n,11]!=1) :
        print("NEGATIVE X")
        car[3,i]=11
        car[1,i]=0
        car[0,i]=-1
        grid[-1+n,11]=1
        car[4,i]=2
        ARRAY=grid
    if which_way==3 and grid[2+n,5]==1: #driving right
        print("BOTTOM RIGHT POSITION OCCUPIED")
        car[0,i]=stop_position_x
        car[1,i]=stop_position_y
        car[2,i]=0
        if int(car[3,i])==5:
            grid[int(car[0,i])+n,int(car[3,i])]=1
        elif int(car[3,i])==7:
            grid[int(car[1,i]),int(car[3,i])]=1
        ARRAY=grid
    elif which_way==3 and grid[2+n,5]!=1:
        print("POSITIVE X")
        car[3,i]=5
        car[1,i]=1
        car[0,i]=2
        grid[2+n,5]=1
        car[4,i]=3
        ARRAY=grid
    if which_way==0 and grid[2,1]==1: #driving up
        print("BOTTOM TOP POSITION OCCUPIED")

        car[0,i]=stop_position_x
        car[1,i]=stop_position_y
        car[2,i]=0
        if int(car[3,i])==5 or int(car[3,i])==11 :
            grid[int(car[0,i])+n,int(car[3,i])]=1
        ARRAY=grid
    elif which_way==0 and grid[2,1]!=1 :
        print("POSITVE Y")
        car[3,i]=1
        car[1,i]=2
        car[0,i]=0
        grid[2,1]=1
        car[4,i]=0
        ARRAY=grid
    return car,ARRAY

"""
FUNCTION : right_crossroads

Logic for the motion of cars at the Right cross roads 

    the motion of cars is random but the car cant return to direction it was driving from i.e. cant do a U-turn
    the logic for crossroads is primitive a better way would to find an algorith for relating all position where the car stops before the 
    red traffic light and all the positons the car goes to when there is a greenligh
    
new parameters: 
    stop_position_x = the position at the cross-roads the car has to stop at if the disered driving location is occupied
                      the position is just before the red light
    stop_position_y = the position at the cross-roads the car has to stop at if the disered driving location is occupied
                      the position is just before the red light   
    block_road= which direction of road to block when choosing direction of drive i.e. coming from left side the car cant drive back to left side 

"""   

def right_crossroads(car,grid,j,i,j1,stop_position_x,stop_position_y,block_road):
    count[4]=count[4]+1
    car[2,i]=0#car needs to stop at traffic light
    print("WE ARE AT RIGHT CROSS ROADS")
    random1=list(range(0,4))
    random1.remove(block_road)
    random1.remove(3)
    which_way=random.choice(random1)
    print(which_way)
    if which_way==0 and grid[51,2]==1: #driving up
        print("MIDDLE TOP POSITION OCCUPIED")
        car[0,i]=stop_position_x
        car[1,i]=stop_position_y
        car[2,i]=0
        if int(car[3,i])==4:
            grid[int(car[0,i])+n,int(car[3,i])]=1
        elif int(car[3,i])==2:
            grid[int(car[1,i]),int(car[3,i])]=1
        ARRAY=grid
        
    elif which_way==0 and grid[51,2]!=1 :
        print("POSITIVE Y")
        car[3,i]=2
        car[1,i]=51
        car[0,i]=99
        grid[51,2]=1
        car[4,i]=0
        ARRAY=grid
    if which_way==1 and grid[48,8]==1: #driving down
        print("MIDDLE BOTTOM POSITION OCCUPIED")
        car[0,i]=stop_position_x
        car[1,i]=stop_position_y
        car[2,i]=0
        if int(car[3,i])==4:
            grid[int(car[0,i])+n,int(car[3,i])]=1
        elif int(car[3,i])==8:
            grid[int(car[1,i]),int(car[3,i])]=1
        ARRAY=grid
    elif which_way==1 and grid[48,8]!=1 :
        print("NEGATIVE Y")
        car[3,i]=8
        car[1,i]=48
        car[0,i]=100
        grid[48,8]=1
        car[4,i]=1
        ARRAY=grid
    if which_way==2 and grid[98+n,10]==1: #driving left
        print("MIDDLE LEFT POSITION OCCUPIED")
        car[0,i]=stop_position_x
        car[1,i]=stop_position_y
        car[2,i]=0
        if int(car[3,i])==2 or int(car[3,i])==8 :
            grid[int(car[1,i]),int(car[3,i])]=1
        ARRAY=grid
    elif which_way==2 and grid[98+n,10]!=1:
        print("NEGATIVE X")
        car[3,i]=10
        car[1,i]=49
        car[0,i]=98
        grid[98+n,10]=1
        car[4,i]=2
        ARRAY=grid
    return car,ARRAY


""" 
    FUNCTION : catch_if_statements 

    If statements for then the car arrives at the crossrpads or the corners of the grid
    depending on the car origin the stop_position for x-y are fed into the appropriete cross road function
    the appropriete cross road function is found from the lane of the car in its parameter 

"""


def catch_if_statments(car,ARRAY,j,i,j1,loop):
    if (j+car[1,i]>=48 and car[4,i]==0 and car[1,i]<=48 and car[3,i]==1): #we are at the central cross road coming from downside
        ARRAY[int(car[1,i]),1]=0
        print(car)
        car,ARRAY=central_crossroad(car,ARRAY,j,i,j1,0,47,1)
    elif (-j+car[1,i]<=51 and car[4,i]==1 and car[1,i]>=51 and car[3,i]==7): #we are at the central cross road coming from upside
        ARRAY[int(car[1,i]),7]=0
        print(car)
        central_crossroad(car,ARRAY,j,i,j1,1,52,0)
    elif (j+car[0,i]>=-1 and car[4,i]==3 and car[0,i]<=-1 and car[3,i]==4): #we are at the central cross road coming from left side
        ARRAY[int(car[0,i])+n,4]=0
        print(car)
        car,ARRAY=central_crossroad(car,ARRAY,j,i,j1,-2,50,2)
    elif (-j+car[0,i]<=2 and car[4,i]==2 and car[0,i]>=2 and car[3,i]==10): #we are at the central cross road coming from right side
        ARRAY[int(car[0,i])+n,10]=0
        print(car)
        car,ARRAY=central_crossroad(car,ARRAY,j,i,j1,3,49,3)
    elif (j+car[1,i]>=97 and car[4,i]==0 and car[1,i]<=97 and car[3,i]==1):#we are at the upper crossroads coming from downside
        ARRAY[int(car[1,i]),1]=0
        print(car)
        car,ARRAY=upper_crossroads(car,ARRAY,j,i,j1,0,97,1)
    elif (-j+car[0,i]<=2 and car[4,i]==2 and car[0,i]>=2 and car[3,i]==9):#we are at the upper crossroads coming from right side
        ARRAY[int(car[0,i])+n,9]=0
        print(car)
        car,ARRAY=upper_crossroads(car,ARRAY,j,i,j1,3,98,3)
    elif (j+car[0,i]>=-1 and car[4,i]==3 and car[0,i]<=-1 and car[3,i]==3):#we are at the upper crossroads coming from left side
        ARRAY[int(car[0,i])+n,3]=0
        print(car)
        car,ARRAY=upper_crossroads(car,ARRAY,j,i,j1,-2,99,2)
    ####################################
    elif (j+car[1,i]>=48 and car[4,i]==0 and car[1,i]<=48 and car[3,i]==0):#we are at the left crossroads coming from downside
        ARRAY[int(car[1,i]),0]=0
        print(car)
        car,ARRAY=left_crossroads(car,ARRAY,j,i,j1,-99,47,1)
    elif (-j+car[0,i]<=-97 and car[4,i]==2 and car[0,i]>=-97 and car[3,i]==10):#we are at the left crossroads coming from right side
        ARRAY[int(car[0,i])+n,10]=0
        print(car)
        car,ARRAY=left_crossroads(car,ARRAY,j,i,j1,-96,49,3)
    elif (-j+car[1,i]<=51 and car[4,i]==1 and car[1,i]>=51 and car[3,i]==6):#we are at the left crossroads coming from upperside
        ARRAY[int(car[1,i]),6]=0
        print(car)
        car,ARRAY=left_crossroads(car,ARRAY,j,i,j1,-98,52,0)    
   ###############################    
                
    elif (-j+car[1,i]<=2 and car[4,i]==1 and car[1,i]>=2 and car[3,i]==7):#we are at the bottom crossroads coming from upper
        ARRAY[int(car[1,i]),7]=0
        print(car)
        car,ARRAY=lower_crossroads(car,ARRAY,j,i,j1,1,3,0)
    elif (-j+car[0,i]<=2 and car[4,i]==2 and car[0,i]>=2 and car[3,i]==11):#we are at the bottom crossroads coming from right side
        ARRAY[int(car[0,i])+n,11]=0
        print(car)
        car,ARRAY=lower_crossroads(car,ARRAY,j,i,j1,3,0,3)
    elif (j+car[0,i]>=-1 and car[4,i]==3 and car[0,i]<=-1 and car[3,i]==5):#we are at the bottom crossroads coming from left side
        ARRAY[int(car[0,i])+n,5]=0
        print(car)
        car,ARRAY=lower_crossroads(car,ARRAY,j,i,j1,-2,1,2)
    ##########################################
    elif (-j+car[1,i]<=51 and car[4,i]==1 and car[1,i]>=51 and car[3,i]==8):#we are at the right crossroads coming from upper side
        ARRAY[int(car[1,i]),8]=0
        print(car)
        car,ARRAY=right_crossroads(car,ARRAY,j,i,j1,100,52,0)
    elif (j+car[0,i]>=98 and car[4,i]==3 and car[0,i]<=98 and car[3,i]==4):#we are at the right crossroads coming from left side
        ARRAY[int(car[0,i])+n,4]=0
        print(car)
        car,ARRAY=right_crossroads(car,ARRAY,j,i,j1,97,50,2)
    elif (j+car[1,i]>=48 and car[4,i]==0 and car[1,i]<=48 and car[3,i]==2):#we are at the right crossroads coming from lower side
        ARRAY[int(car[1,i]),2]=0
        print(car)
        car,ARRAY=right_crossroads(car,ARRAY,j,i,j1,99,47,1)    
    elif (j1+car[1,i]>=98 and car[3,i]==2 and car[4,i]==0): #top right corner going up
        ARRAY[int(car[1,i]),2]=0
        car[1,i]=98
        car[0,i]=98
        car[4,i]=2
        car[3,i]=9
        #ARRAY[int(car[0,i]),3]=1
    elif (j1+car[0,i]>=99 and car[3,i]==3 and car[4,i]==3): #top right corner going right
        ARRAY[int(car[0,i])+n,3]=0
        car[1,i]=99
        car[0,i]=99
        car[4,i]=1
        car[3,i]=8
        #ARRAY[int(car[1,i]),2]=1
    elif (-j1+car[1,i]<=0 and car[3,i]==8) and car[4,i]==1: #bottom right corner going down
        ARRAY[int(car[1,i]),8]=0
        car[1,i]=0
        car[0,i]=99
        car[4,i]=2
        car[3,i]=11
        #ARRAY[int(car[0,i]),5]=1
    elif (j1+car[0,i]>=98 and car[3,i]==5 and car[4,i]==3): #bottom right corner going right
        ARRAY[int(car[0,i])+n,5]=0
        car[1,i]=1
        car[0,i]=98
        car[4,i]=0
        car[3,i]=2
        #ARRAY[int(car[1,i]),2]=1
    elif (-j1+car[0,i]<=-99 and car[3,i]==11 and car[4,i]==2): #bottom left corner going left
        ARRAY[int(car[0,i])+n,11]=0
        car[1,i]=0
        car[0,i]=-99
        car[4,i]=0
        car[3,i]=0
        #ARRAY[int(car[1,i]),0]=1
    elif (-j1+car[1,i]<=1 and car[3,i]==6 and car[4,i]==1): #bottom left corner going down
        ARRAY[int(car[1,i]),6]=0
        car[1,i]=1
        car[0,i]=-98
        car[4,i]=3
        car[3,i]=5
        #ARRAY[int(car[1,i]),5]=1
    elif (j1+car[1,i]>=99 and car[3,i]==0 and car[4,i]==0): #top left corner going up
        ARRAY[int(car[1,i]),0]=0
        car[1,i]=99
        car[0,i]=-99
        car[4,i]=3
        car[3,i]=3
        #ARRAY[int(car[1,i]),3]=1
    elif (-j1+car[0,i]<=-99 and car[3,i]==9 and car[4,i]==2): #top left corner going left
        ARRAY[int(car[0,i])+n,9]=0
        car[1,i]=98
        car[0,i]=-98
        car[4,i]=1
        car[3,i]=6
        #ARRAY[int(car[1,i]),0]=1
    else:
        car,ARRAY,loop=drive(car,ARRAY,j,i,j1,loop) 
        
    return car,ARRAY,loop


""" 
    FUNCTION : Breakdown function 

mimics random events while driving there is a breakdown_chance of reducing the speed to V-1
and a standing 1% chance to reduce to V=0
"""
def breakdown(car,i,break_down_chance1):
    p=np.random.rand(1)
    if p<break_down_chance1:
        print("CAR SLOWS DOWN")
        car[2,i]=car[2,i]-1
    elif p<0.01:
        print("BREAKDOWN")
        car[2,i]=0
    return car


"""
    FUNCTION : new_velocity 
    
    Function to drive all cars by one step
    
    finds new velocity and position for all cars
    
    calls other functions
    
    loops through all the cars

"""

def new_velocity(car,ARRAY,lenth_of_road,break_down_chance):
    for i in range(number_of_cars):
        
        if car[2,i]<Vmax:  #if Car driving below speed limit
            loop=True
            car[2,i]=car[2,i]+1
            j=1
            while loop==True and (j<int(car[2,i]+1) ) :
                j1=j+1
                car,ARRAY,loop=catch_if_statments(car,ARRAY,j,i,j1,loop)           
                j=j+1
            if car[2,i]>=1:
                car=breakdown(car,i,break_down_chance)  
            car[5,i]=car[5,i]+car[2,i]
        elif car[2,i]==Vmax:     #if car driving at speed limit
            loop=True
            j=1
            while loop==True and (j<int(car[2,i]+1)):
                j1=j+1
                car,ARRAY,loop=catch_if_statments(car,ARRAY,j,i,j1,loop)
                j=j+1
            if car[2,i]>=1:
                car=breakdown(car,i,break_down_chance)
            car[5,i]=car[5,i]+car[2,i]
    return car
 
"""
Run 10000 loops of simulations i.e 10000 steps of motion for all cars

"""
for h in range(10000):

    print(break_down_chance)
    z=new_velocity(car1,ARRAY,length_of_road, break_down_chance)      
    print(z)
    new_data=np.transpose(z)
    with open(r"fulldata2.txt", "w") as f:
        np.savetxt(f, data)
    animate(h)
plt.close()


""" SAVE RESULTS"""
average_distance=sum(z[5,:])/number_of_cars
print(average_distance)
with open(r"average distance.txt","a") as j:
    j.write(str(average_distance) +"\n")
with open(r"velocity.txt","a") as j:
    j.write(str(Vmax)+"\n")
  
print ("My program took", time.time() - start_time, "to run")
print(count)
