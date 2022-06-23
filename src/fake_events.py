class fake_event:
  def __init__(self, *, errors: bool = True):
    self.errors: bool = errors
    self.co = self.events = []

  def execute(self, *args, event: str = None):
    from ..core import protr
    import asyncio
    liste: list = self.co if event is None else self.events[event]
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

  def apply(self, event: str = None, *, is_async: bool = False):
    def deco(func):
      if event is None:
        self.co.append({"func": func, "async": is_async})
        return func
      else:
        if event not in self.events: self.events[event]: list = []
        self.events[event].append({"func": func, "async": is_async})


  def appendfn(self, fonction, event: str = None, *, is_async: bool = False):
    if event is None:
      self.co.append({"func": fonction, "async": is_async})
      return fonction
    else:
      if event not in self.events: self.events[event]: list = []
      self.events[event].append({"func": fonction, "async": is_async})
