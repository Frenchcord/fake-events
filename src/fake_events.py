class fake_event:
  def __init__(self, *, errors: bool = True):
    self.errors: bool = errors
    self.co = self.events = []
    self.apply = apply_dec

  def execute(self, *args, event: str = None):
    from ..core import protr
    import asyncio
    liste: list = self.apply.co if event is None else self.apply.events[event]
    if self.errors is False:
      for i in liste:
        if i['async'] is True:
          def exe(arg):
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            loop.run_until_complete(i['func'](arg))
            loop.close()
          protr(exe, args)
        else:
          protr(i['func'], args)
    else:
      for i in liste:
        if i['async'] is True:
          def exe(arg):
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            loop.run_until_complete(i['func'](arg))
            loop.close()
          try:
            protr(exe, args)
          except Exception as e:
            print(e)
        else:
          try:
            protr(i['func'], args)
          except Exception as e:
            print(e)

  def appendfn(self, fonction, event: str = None, *, is_async: bool = False):
    if event is None:
      self.apply.co.append({"func": fonction, "async": is_async})
      return fonction
    else:
      if event not in self.apply.events: self.apply.events[event]: list = []
      self.apply.events[event].append({"func": fonction, "async": is_async})

class apply_dec:
  events: dict = {}
  co: list = []
  def __init__(self, event: str = None, *, is_async: bool = False):
    self.is_async: bool = is_async
    self.event: str = event
    
  def __call__(self, func):
    if self.event is None:
      self.co.append({"func": func, "async": self.is_async})
    else:
      if self.event not in self.events: self.events[self.event]: list = []
      self.events[self.event].append({"func": func, "async": self.is_async})
    return None
