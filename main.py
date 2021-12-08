from discord.ext import commands
from keep_alive import KeepAlive
from os import environ

class ManfaceBot(commands.Bot):
  def __init__(self):
    self.adjectives = [
      "fat", "chunky", "poop4", "chungus", "amongus", "scarfmon", "obamacare", "fat",
      "ugly", "short", "skinny", "unpoggers", "unbased", "bluepilled", "sponchating",
      "genshinimpact playing", "political", "bad", "thirsty", "interesting", "lanky",
      "chucklesome", "old", "brave", "based", "epic", "super unpog", "ty-lee loving",
      "[redacted]", "nasty", "flushed emoji", "soup", "forgorfull", "lazy", "fast",
      "souplike", "extra", "juicy", "smelly", "YIIK-like"
    ]
    self.verbs = [
      "poop her pants", "got kicked out of apple bees", "went to prison", "failed elementary school",
      "walked under clock tower", "doctor pepper ", "played genshin impact", "did too much trolling",
      "ate chungus juice", "walks her dog upside down", "uefduweudwe28du2882du82u8de2uued poop4",
      "poop4","dropped out of high school to become a pro robloxer","vented in electrical", "made pilk",
      "didn't know it was about drive", "didn't stay hungry and devour", "ate toothpaste",
      "got kicked out of the dining hall for making pilk", "bought soup at the soup store", "forgor everything",
      "rember everything :D", "showers at planet fitness", "doesn't shower", "[redacted]",
      "shit their pants upon seeing the big chungus movie", "lost the big YIIK tournament", "Yiiked out",
      "became alex yiik", "violated one of the goku rules"
    ]
    self.verbs2 = [
      "poop his pants", "got kicked out of apple bees", "went to prison", "failed elementary school",
      "walked under clock tower", "doctor pepper ", "played genshin impact", "did too much trolling",
      "ate chungus juice", "walks his dog upside down", "uefduweudwe28du2882du82u8de2uued poop4", "poop4",
      "dropped out of high school to become a pro robloxer", "vented in electrical", "made pilk",
      "didn't know it was about drive", "didn't stay hungry and devour", "ate toothpaste",
      "got kicked out of the dining hall for making pilk", "bought soup at the soup store", "forgor everything",
      "rember everything :D", "showers at planet fitness", "doesn't shower", "[redacted]",
      "shit their pants upon seeing the big chungus movie", "lost the big YIIK tournament", "Yiiked out",
      "became alex yiik", "violated one of the goku rules"
    ]
    super().__init__(command_prefix='-')
    # Load commands
    self.load_extension('commands')
    
    # Start the aiohttp keepalive server
    self.keep_alive = KeepAlive()
    self.loop.create_task(self.keep_alive.run())

  async def on_ready(self):
    print(f'Logged in as {self.user.id}/{self.user}')

ManfaceBot().run(environ['token'])