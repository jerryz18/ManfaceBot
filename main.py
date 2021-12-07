import os
import discord
import random

client = discord.Client()

@client.event
async def on_ready():
  print("Hello {0.user}".format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  adjective = ["fat", "chunky", "poop4", "chungus", "amongus","scarfmon","obamacare","fat","ugly","short","skinny","unpoggers", "unbased","bluepilled",
               "sponchating","genshinimpact playing", "down bad", "chungusified", "raw", "rude", "smart", "silly", "goofy", "cringe", "annoying", "poggywoggy", "sussy", "creepy",
              "political", "bad", "thirsty", "interesting", "lanky", "chucklesome", "old", "brave", "based", "epic", "super unpog", "ty-lee loving", "[redacted]", "nasty",
              "flushed emoji", "soup", "forgorfull", "lazy", "fast", "souplike", "extra", "juicy", "smelly", "YIIK-like"]

  verb = ["poop her pants", "got kicked out of apple bees", "went to prison", "failed elementary school",
  "walked under clock tower", "doctor pepper ", "played genshin impact", "did too much trolling",
  "ate chungus juice", "walks the dog upside down", "uefduweudwe28du2882du82u8de2uued poop4", "poop4", "complained about being single on reddit", "believed that 9 + 10 equals 19",
         "fell into the toilet", "drank newark sewage water", "played roblox", "argued about politics online", "became sponchbop", "got banned from the discord", "ordered a pizza",
         "helikopter helikopter", "knew nothing about rolling down in the deep", "had that mental freeze", "put that shit in slow motion", "felt like an astronaut in the ocean", 
         "dropped out of high school to become a pro robloxer", "vented in electrical", "made pilk", "didn't know it was about drive", "didn't stay hungry and devour", "ate toothpaste",
         "got kicked out of the dining hall for making pilk", "bought soup at the soup store", "forgor everything", "rember everything :D", "showers at planet fitness", "doesn't shower",
         "[redacted]", "shit their pants upon seeing the big chungus movie", "lost the big YIIK tournament", "Yiiked out", "became alex yiik", "violated one of the goku rules"]

  if message.content.startswith("-ym") or message.content.startswith("-yomama"):
    await message.channel.send("Yo mama is so " + random.choice(adjective) + " she " + random.choice(verb) + "!")
  if message.content.startswith("-yd") or message.content.startswith("-yodad"):
    await message.channel.send("Yo dad is so " + random.choice(adjective) + " he " + random.choice(verb) + "!")

my_secret = os.environ['token']
client.run(my_secret)

