class fake_event:
  def __init__(self, *, errors: bool = True):
    self.errors: bool = errors
    self.co: list = []

  def execute(self, *args):
    from ..core import protr
    import asyncio
    if self.errors is False:
      for i in self.co:
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
      for i in self.co:
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

  def apply(self, *, is_async: bool = False):
    def deco(func):
      self.co.append({"func": func, "async": is_async})
      return func

  def appendfn(self, fonction, *, is_async: bool = False):
    self.co.append({'func': fonction, "async": is_async})
