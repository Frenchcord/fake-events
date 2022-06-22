# creer un fake-event
```py
from frenchcord import fake_event
event = fake_event()
```
# appiquer une fonction a l'event
### Methode 1
```py
@event.apply()
def hello():
  print('hello, world!')
```
### methode 2
```py
def hi():
  print('hello, world!')
event.appendfn(hi)
```
## async
### Methode 1
```py
@event.apply(is_async=True)
async def hello():
  print('hello, world!')
```
### methode 2
```py
async def hi():
  print('hello, world!')
event.appendfn(hi, is_async=True)
```
## argument
(pareil pour async)
### Methode 1
```py
@event.apply()
def hello(thing: str):
  print(thing)
```
### methode 2
```py
def hi(thing: str):
  print(thing)
event.appendfn(hi)
```
# execute
## no args
```py
event.execute()
```
# args
```py
event.execute('Hello, world!')
```
