#!/usr/bin/env python
# coding: utf-8

# # Maze Solver 
# ## Using Depth Per Search following basic Image Processing
# 
# ### Contact: singhjashandeep2332@gmail.com
# ### Github: @ijashandeepsingh
# 
# 
# 

# In[1]:


#libraries



import numpy as np

#pillow 
import PIL.Image as processor

import random


# In[2]:


image = processor.open("Maze.png") 
pixel = image.load() #loading, given the image is single frame 


# In[3]:


#resizing the image for singularity 

def resize(image):
    imgResized = image.resize((600, 600))
    imgResized.show()
      


# In[4]:


#funtion to find the start and end of the maze based upon colour code 

def start_end(image): 
    
    array = np.array(image)
    
    start = (254, 0, 0) #red 
    end = (0, 9, 254) #blue
    
    y_start, x_start = np.where(np.all(array == start, axis =2))
    y_end, x_end = np.where(np.all(array == end, axis =2))
    
    loc_start = (int(x_start[0]), int(y_start[0]))
    loc_end = (int(x_end[0]), int(y_end[0]))
    
    return loc_start, loc_end

#defining the start, end
start, end = start_end(image)

print("The starting point is:", str(start))
print("The ending point is:", str(end))


# 
# ** Note **
# 
#    It doesnt really matters which is the starting point or ending point as our code specifies to find a solution
#    towards the route to solve the maze.
# 
# 

# In[5]:


def search_engine(start, end, img, pix):
    isFound = False 
    current = start
    array = np.array(img)
    path = []
    intersects = []
    
    while not isFound:
        possible = []
        surroundings = [(current[0]-1, current[1]),
                        (current[0]+1, current[1]),
                        (current[0], current[1]-1),
                        (current[0], current[1]+1)]
        
        for move in surroundings:
            if end == move: 
                isFound = True 
            if ((pix[move] >= (200,200,200)) and pix[move] != (255,255,0) and move != start) : 
                possible.append(move)
                
        if len(possible) >= 2:   
            if current not in intersects: 
                intersects.append(current)
                
        if len(possible) == 0:
            intersects_reversed = intersects[::-1]
            for i in intersects_reversed:
                if i != current: 
                    current = i 
                    
                    intersects.pop(intersects.index(i))
                    break
                    
            path = path[:path.index(current)]
            
        else: 
            
            current = random.choice(possible)
            
        path.append(current)
        
        array[current[1], current[0]] = (255,255,0)
        
        
        img = processor.fromarray(array)
        pix = img.load()
        
    for p in path: 
        
        array[p[1], p[0]] = (0, 255, 0)
        
    img = processor.fromarray(array)
    img.save("solved.png")
        
        


# In[6]:


#call the function 
search_engine(start, end, image, pixel)



# visual comparison block

#reviewing the input maze 
resize(image)


#solved maze review
solved_image = processor.open("solved.png")
resize(solved_image)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




