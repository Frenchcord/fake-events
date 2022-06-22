from frenchcord import fake_event
my_event = fake_event()
@my_event.apply(is_async=True)
async def hello(thing_str: str):
  print(thing_str)
 
@my_event.apply()
def hello(strthing: str):
  print(strthing)
 
my_event.execute('hello world!')
