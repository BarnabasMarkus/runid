# :sparkles:runid:sparkles:
runid is a simple utility, which allows basic run tracking.  
it is super handy if, for example, you want to know how many times a particular script or jupyter notebook has been run.


### Requirements

`pip install joblib`


### Installation

`pip install git+https://github.com/BarnabasMarkus/runid.git`


### API

**RunId.runid** _**(self, path='runid.stored', runid=None)**_

Parameter | Type | Default | Description
------------ | ------------- | ------------- | -------------
**path** | *str* | *'runid.stored'* | The path of the file which contains the Run ID
**runid** | *int* | *1* | Value of the currrent Run ID


### How To Use


Using Run ID is as simple as 
```python
>>> from runid import RunId
>>>
>>> my_runid = RunId()
>>> print(my_runid.runid)
1
>>> my_runid.step()
>>> print(my_runid.runid)
2
>>> 
>>> my_runid.step()
>>> my_runid.step()
>>> my_runid.step()
>>> print(my_runid.runid)
5
```


Next time you get the incremented value of the last saved Run ID
```python
>>> from runid import RunId
>>>
>>> x = RunId()
>>> print(x.runid)
6
```


How can I **change the default Run ID**, which is 1?
```python
>>> from runid import RunId
>>> 
>>> x = RunId(runid=9)
>>> print(x.runid)
9
```


If you want to **reset** the Run ID do this
```python
>>> from runid import RunId
>>>
>>> x = RunId()
>>> print(x.runid)
7
>>> x.reset()
>>> print(x.runid)
1
```


Run ID use the file `runid.stored` as a default **storage**. You can change it anytime you want.
```python
>>> from runid import RunId
>>>
>>> my_runid = RunId(path='file.storage')
```
DANGER! If for some reason you use two runids at the same time,  
never forget to change the default storage path, otherwise one variable will overwrite the other.


Show Run ID **object summary** for human beings...
```python
>>> from runid import RunId
>>> 
>>> x = RunId(path='file.runid', runid=13)
>>> print(x)
RunId (13) stored @ file.runid
```


... and machines
```python
>>> from runid import RunId
>>> 
>>> x = RunId(path='file.runid', runid=13)
>>> print(repr(x))
RunId(path='file.runid', runid=13)
```

