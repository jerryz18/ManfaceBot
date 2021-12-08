from aiohttp import web

class KeepAlive():
  def __init__(self):
    self.app = web.Application()
    self.app.router.add_get('/', self.home)

  async def run(self):
    await web._run_app(
      self.app,
      host='0.0.0.0',
      port=8080
    )
    
  async def home(self, request):
    return web.Response(text='Hello. I am alive!')