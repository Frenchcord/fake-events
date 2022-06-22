class fake_event:
  def __init__(self, function, *, is_async: bool = False):
    self.fonction = function
    self.is_async: bool = is_async
    self.co: list = []

  def execute(self, *args):
    from ..core import protr
    import asyncio
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

  def apply(self, *, is_async: bool = False):
    def deco(func):
      self.co.append({"func": func, "async": is_async})
      return func

  def appendfn(self, fonction, *, is_async: bool = False):
    self.co.append({'func': fonction, "async": is_async})
