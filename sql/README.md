# PyHawaii January 17, 2017


## SQL Alchemy
```python
from sqlalchemy import create_engine
engine = create_engine('sqlite:///:memory:', echo=True) # connection to sqlite database in memory

from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine, autocommit=True)
session = Session()

print(session, type(session))

# defining an object type
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

Base = declarative_base() # create a base class called Base by calling sqlalchemy.ext.declarative.declarative_base() once
                          # This will be the base class for all of our models

class Person(Base): # create a class Person that inherits from Base
  __tablename__ = 'person'

  id = Column(Integer, primary_key=True) # good practice to have an integer "primary" key, unique
  first_name = Column(String(25), nullable=False) # no more than 25 characters
  last_name = Column(String(25), nullable=False) # nullable means that these parameters are needed when committing
  alter_ego = Column(String) # no limit on string length

Person.__table__ # inspect Person class to see how SQL Alchemy understands it

Base.metadata.create_all(engine) # need to tell our database to create the table necessary to store Person objects

# creating an object
bruce_wayne = Person(first_name='Bruce', last_name='Wayne')
print(bruce_wayne.first_name)
print(bruce_wayne.id) # object exists only in python at this point


session.add(bruce_wayne) # queue commit
session.flush() # flush memory and pushes the object to database
print(bruce_wayne.id)

session.add(Person(first_name='Tony', last_name='Stark'))
session.add(Person(first_name='Tony', last_name='Stark'))
session.flush() # adds both new objects to the database

''' Example of flush() not working due to empty parameter
session.add(Person(first_name='Bob'))
session.flush() # will produce error because of the nullable aspect
'''

# retrieving objects
people = session.query(Person).filter(Person.first_name=='Bruce').all()
print(len(people))
bruce1 = people[0]
print(bruce1.last_name)


for name in session.query(Person.first_name).all():
  print(name)


# updating object
bruce1.alter_ego = 'Batman' # alter the value of Bruce1
print(session.dirty) # ask about queued objects that have not been pushed, difference between database and memory, doesn't specify difference
session.flush()
print(session.dirty)

# query for all unique alter egos that we have identified
for person in session.query(
  Person.alter_ego,
  Person.first_name,
  Person.last_name
  ).filter(Person.alter_ego != None).all():
  print(person) # return only the Person with an alter ego

# session.query(Person).filter(Person.first_name='Tony')[0].alter_ego='Ironman' # may be incomplete
# session.flush()


# deleting objects
print(session.query(Person).filter(Person.first_name=='Bruce').count())
session.delete(bruce1)
print(session.query(Person).filter(Person.first_name=='Bruce').count())


# other significant concepts
'''
- table relationships using foreign keys
- full transaction support
- persisting

'''


# saving database to disk
engine = create_engine('sqlite:///path/to/file', echo=True)


# template for sql alchemy to handle classes rather than building every time
1) models.py
2) main.py
```


### Basic program pattern
#### models.py

```python
import os

from sqlalchemy import create_engine
from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

BASE_DIR = os.path.basename(__name__)
FILENAME = 'database.sqlite'

db_name = os.path.join(BASE_DIR, FILENAME)

engine = create_engine('sqlite:///{}'.format(db_name))

Base = declarative_base()

#
# put your models here
#

# class MyModel...
```


#### main.py
```python
from sqlalchemy.orm import sessionmaker

from models import engine
from models import MyModel

with sessionmaker(bind=engine, autocommit=True)() as session:
    for person in session.query(Person).all():
        print(person)
    # put your fancy program stuff here
```





## Statistics (https://github.com/chalmerlowe/jarvis_II/blob/master/datasci_basics/01_statistics.ipynb)

#### Library
```python
from collections import Counter
```

#### Simple statistics
Built-in functions: len(), max(), min()

#### Mean
```python
def mean(values):
    '''Return the mean (or average) of a sequence of values.
    
    >>> mean([1, 2, 3, 4])
    2.5
    
    >>> mean([1, 2, 3, 4, 5])
    3.0
    
    '''
  return sum(values) / len(values)
```

#### Median
```python
def median(values):
    """Return the median value from a sequence of values
    
    >>> median([1, 3, 5])          # odd number of values
    3
    
    >>> median([1, 3, 5, 7])       # even number of values
    4.0
    """
    
    num = len(values)
    sorted_values = sorted(values)
    centerpoint = num // 2            # truncate any floats...
    
    if num % 2 == 1: 
        # return the center value if n is odd
        return sorted_values[centerpoint]
    
    else:
        # return the average of the two center-most values
        # if num is even
        c1 = centerpoint - 1
        c2 = centerpoint
        return (sorted_values[c1] + sorted_values[c2]) / 2
```

#### Mode
```python
from collections import Counter

def mode(values):
    """Returns a list of the most common (frequent) value(s) 
    
    If there is more than one element with the same maximum frequency, then
    return all such elements as a list
    """
    
    mode_values = {}
    counts = Counter(values)
    max_count = max(counts.values())
    
    return [value for value, count in counts.items() if count == max_count]
```

#### Frequency table
```python 
from collections import Counter

def freq_table(values):
    """Returns a series of values and counts in a frequency table 
    
    """
    
    frequencies = Counter(values)
    print('Value\tFrequency')
    
    for value, count in frequencies.most_common():
        print('{}\t{}'.format(value, count))
```

#### Range
```python
def data_range(x):
    '''Returns the range (i.e. the difference) between the 
    highest and lowest values
    '''
    
    return max(x) - min(x)
```


#### Quantiles and interquartile ranges
##### Quantiles
```python
def quantile(values, percentile):
    """Returns the pth-percentile value in a sequence of values
    """
    
    p_index = int(percentile * len(values)) # percentile 0-1
    return sorted(values)[p_index]
```
##### Interquartile
```python
def interquartile_range(values):
    '''Return the difference between the 75% and 25% percentiles.
    '''
    return quantile(values, 0.75) - quantile(values, 0.25)
```

#### Variance and standard deviation

##### Variance
```python
def variance(values):
    """Return the variance of a sequence of values.
    
    NOTE: this functions presumes that values has a minimum of TWO elements.
    """
    
    num = len(values)
    deviations = diff_mean(values)
    squared_diffs = [d**2 for d in deviations]
    sum_squared_diffs = sum(squared_diffs)
    
    return sum_squared_diffs / num
```

##### Standard Deviation
```python
def standard_deviation(values):
    """Return the standard deviation of a sequence of values
    """
    
    from math import sqrt
    return sqrt(variance(values))
```

#### Useful libraries for statistics
##### statistics
```python
import statistics as stats

print(stats.mean(num_defects))
print(stats.median(num_defects))
print(stats.variance(num_defects))
print(stats.stdev(num_defects))
```
##### numpy
```python
import numpy as np

defects = np.array(num_defects)

defects.mean()
defects.min()
defects.max()

print(defects.var())
print(defects.std())
```
##### scipy
```python
import scipy

print(scipy.mean(num_defects))
print(scipy.median(num_defects))
print(scipy.var(num_defects))
print(scipy.std(num_defects))
```
##### pandas
```python
import pandas as pd

defects_pd = pd.Series(num_defects)

print(defects_pd.mean())
print(defects_pd.median())
print(defects_pd.var())
print(defects_pd.std())
```






