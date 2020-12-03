#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Task 1


# In[2]:


class Animal:
    
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        
    def feed(self, food):
        self.weight += food
        
    def sound(self):
        self.sound = input(f'What sound does {self.name} make? ')
        
        print(f'{self.sound}!')

class Goose(Animal):
    
    def __init__(self, name, weight):
        super().__init__(name, weight)
                 
    def collect_eggs(self, quantity):
        self.weight -= quantity * 0.144
    
class Cow(Animal):
    
    def __init__(self, name, weight):
        super().__init__(name, weight)
    
    def milk(self, litres):
        self.weight -= litres
        
class Sheep(Animal):
    
    def __init__(self, name, weight):
        super().__init__(name, weight)
        
    def shear(self, kg):
        self.weight -= kg
    
class Chicken(Animal):
    
    def __init__(self, name, weight):
        super().__init__(name, weight)
        
    def collect_eggs(self, quantity):
        self.weight -= quantity * 0.06
    
class Goat(Animal):
    
    def __init__(self, name, weight):
        super().__init__(name, weight)
        
    def milk(self, litres):
        self.weight -= litres

class Duck(Animal):
    
    def __init__(self, name, weight):
        super().__init__(name, weight)
        
    def collect_eggs(self, quantity):
        self.weight -= quantity * 0.07
        


# In[3]:


farm = []
grey = Goose('Grey', 5.45)
farm.append(grey)

white = Goose('White', 5.45)
farm.append(white)

manka = Cow('Manka', 545)
farm.append(manka)

rammy = Sheep('Rammy', 100)
farm.append(rammy)

curly = Sheep('Curly', 100)
farm.append(curly)

co_co = Chicken('Co-Co', 3)
farm.append(co_co)

cock_a_doodle_doo = Chicken('Cock-A-Doodle-Doo', 3)
farm.append(cock_a_doodle_doo)

horns = Goat('Horns', 25)
farm.append(horns)

hooves = Goat('Hooves', 25)
farm.append(hooves)

quacky = Duck('Quacky', 2.9)
farm.append(quacky)


# In[4]:


for animal in farm:
    
    if isinstance(animal, Animal):
        animal.feed(1)
        animal.sound()
        
    print(animal.weight)
       
    


# In[11]:


# Task 2


# In[12]:


class Track:
    
    def __init__(self, name, duration):
        self.name = name
        self.duration = int(duration)

    def __str__(self):
        string = f'{self.name}-{self.duration} min'
        
        return string
    
    def __gt__(self, other):
        if not isinstance(other, Track):
            print('Not a track!')
        else:
            return self.duration > other.duration
    
    def __eq__(self, other):
        if not isinstance(other, Track):
            print('Not a track!')
        else:
            return self.duration == other.duration
        
    def __lt__(self, other):
        if not isinstance(other, Track):
            print('Not a track!')
        else:
            return self.duration < other.duration
        


# In[13]:


track1 = Track('Atlas', 5)


# In[14]:


print(track1)


# In[15]:


track1 = Track('Bohemian rhapsody', 6)
track2 = Track('The show must go on', 4)

print(track1 > track2)
print(track1 == track2)
print(track1 < track2)


# In[446]:


class Album:
    
    def __init__(self, name, band):
        self.a_name = name
        self.band = band
        self.tracks = []
        
        
    def get_tracks(self):
        for track in self.tracks:
            Track.show(track)
    
    
    def add_track(self, name, duration, track):
            
        self.name = name
        self.duration = int(duration)
        self.track = track
        
        
        self.track = Track(self.name, self.duration)
        self.tracks.append(self.track)
        
    def get_duration(self):
        duration = 0
        for track in self.tracks:
            duration += track.duration
            
        return duration
    
    def __str__(self):
        print(f'Band name: {self.band}')
        print(f'Album name: {self.a_name}')
        print('Tracks:')
        
        for i in self.tracks:
            print('\t' + f'{i.name}-{i.duration} min')
        
   
         
       
            


# In[447]:


fallen_light = Album('Fallen Light', 'Phaeleh')


# In[448]:


fallen_light.add_track('Afterglow', 4, 'track_1')
fallen_light.add_track('Losing You', 6, 'track_2')
fallen_light.add_track('Lament', 5, 'track_3')


# In[449]:


print(fallen_light)


# In[ ]:





# In[ ]:




