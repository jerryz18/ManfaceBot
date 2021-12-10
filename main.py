import os
import discord
import random
from keep_alive import keep_alive

client = discord.Client()

@client.event
async def on_ready():
  print("Hello {0.user}".format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  adjective = ["fat", "chunky", "poop4", "chungus", "amongus","scarfmon","obamacare","fat","ugly","short","skinny","unpoggers", "unbased","bluepilled","sponchating","genshinimpact playing",               "political", "bad", "thirsty", "interesting", "lanky", "chucklesome", "old", "brave", "based", "epic", "super unpog", "ty-lee loving", "[redacted]", "nasty",
  "flushed emoji", "soup", "forgorfull", "lazy", "fast","souplike", "extra", "juicy", "smelly", "YIIK-like", "round", "chungolian", "p̶̨̮͉̗̮̭̮͓̘̪̗̺͙̈́o̵̢̳̰̘̱͐̈́̉̋̐̾̽̈́̽́͋͂̈́̌͗ở̴̡̡̧̡̳̠͙͚̗͙̩͉̅́̊̋̾̀̎͝ͅp̴̜̣͛̎̿4̸̨̛̟͔̘̼̲̙̳̏̂̈́͋͋̎͊̍̀͘͝", "offensive", "swag", "hot", "sweaty",
              "yucky"]

  verb = ["poop her pants", "got kicked out of apple bees", "went to prison", "failed elementary school",
  "walked under clock tower", "doctor pepper ", "played genshin impact", "did too much trolling",
  "ate chungus juice", "walks her dog upside down", "uefduweudwe28du2882du82u8de2uued poop4", "poop4","dropped out of high school to become a pro robloxer","vented in electrical", "made pilk", "didn't know it was about drive", "didn't stay hungry and devour", "ate toothpaste",
  "got kicked out of the dining hall for making pilk", "bought soup at the soup store", "forgor everything", "rember everything :D", "showers at planet fitness", "doesn't shower",
  "[redacted]", "shit their pants upon seeing the big chungus movie", "lost the big YIIK tournament", "Yiiked out", "became alex yiik", "violated one of the goku rules",
         "urinated on fellow passenger for not being allowed to smoke", "ate mac pizza and mac spaghetti", "turned their back on family", "got impeached as a discord admin",
         "spent all their time playing arsenal on ROBLOX", "knew nothing about rolling down in the deep", "damn daniel AR AR AR AR AR", "tried to schedule an appointment with doctor pepper",
         "thought justin beeber was justin beavverr LOOL", "causes the stock to drop upon missing a meal", "stared at a cup of orange juice for 12 hours because it said concentrate", "genshin"
         , "became a vtuber", "t̸̗͕̗̩͛̓̕͠ͅr̶̩̖̗̽͌í̷̞͕͖̂̃ę̷͚̣͕͖̮̮̿̓̕d̸̛̺̟͍̾̔͑̎̕ ̸̛̲͍̗̰͋͆́̕t̸̹̰̩̝̃̐͒͋̚o̸͖̱͍͑̈͆̇̾̀ ̸̩̜̤̌́̋͋̓̅͌ś̵͈͙͇͍̿̋̿͋͐̽c̷̪̹̲͇̾͝ḩ̵̫̘͇͛̆̀͛͆̕͜͝ḙ̴̪͙̙͚͙̐̾͑́̃͛d̶̬̙̤̥͐͗͛̈́͜u̷̖̭̞̦͔̥̦̐͑̎͘ḷ̵̌e̵̜͔̭̖͑̓̀ ̵̭̙̯̒́̃͗̈́̇͝a̶̧̮͔͙̺͊̌͛͘̕͝n̸̟̝̩̄̌̀̾͗͊̍ ̵̨̛̫̭̮̞̏͌̑ą̶̩̰̦̝͓̞͆p̶̢̰͙̠̜̗̻͑̊̍̂͗p̵̡̡̦̬̣̃̅̀̀̒͘ǫ̵̙͈͈̻͆ị̷͉̮͓͛̑̒̊̊͊̈́͜n̸̙͎̞̻͂̄͗̀t̴̅͋͐ͅm̷͎̠̰̋̀͂̂ͅe̶̺̽̈́̽̈n̵̩͋͂͂́̋̀ț̶̻̹͓͚́́͐̍̎͠ ̷̪̏͝w̵̡̦͙̣͒͌ḭ̴̝̞̜̟̖̈́̑̀̈̈́̂ţ̸̀̎̽̓͂̈́h̵̡͗́̀̊̅͝ ̷̪̻̪̣̼͑̑͒͒̃ḋ̸͇̙̞̻͔͂̋̏͊o̶͓̼̟̗͒̐̏̉̒̉̂c̶̦͈̬̤͚͖͂t̴̟̪̖̣̆̎̊ō̵̙̙̂̏́̈́͆ŕ̸̨̛͇̲̬̣̦̄͛̈́͒ ̷̼̘͈̮͆̓̄̂̅͒̕p̴̗͙̀̏̒ė̶̢̫̘̋̑̔p̸̧̢̯̲̪̝̈́͑̈͒̂p̴̨̾́ë̷̢̥̥͈͔̟͒̾̓̚͠r̵̬͍̖̭̙̖̔͊͌͛̅̇"]
  
  verb2 = ["poop his pants", "got kicked out of apple bees", "went to prison", "failed elementary school",
  "walked under clock tower", "doctor pepper ", "played genshin impact", "did too much trolling",
  "ate chungus juice", "walks his dog upside down", "uefduweudwe28du2882du82u8de2uued poop4", "poop4","dropped out of high school to become a pro robloxer", "vented in electrical", "made pilk", "didn't know it was about drive", "didn't stay hungry and devour", "ate toothpaste",
  "got kicked out of the dining hall for making pilk", "bought soup at the soup store", "forgor everything", "rember everything :D", "showers at planet fitness", "doesn't shower",
  "[redacted]", "shit their pants upon seeing the big chungus movie", "lost the big YIIK tournament", "Yiiked out", "became alex yiik", "violated one of the goku rules",
         "urinated on fellow passenger for not being allowed to smoke", "ate mac pizza and mac spaghetti", "turned their back on family", "got impeached as a discord admin",
         "spent all their time playing arsenal on ROBLOX", "knew nothing about rolling down in the deep", "damn daniel AR AR AR AR AR", "tried to schedule an appointment with doctor pepper",
         "thought justin beeber was justin beavverr LOOL", "causes the stock to drop upon missing a meal", "stared at a cup of orange juice for 12 hours because it said concentrate", "genshin"
         , "became a vtuber", "t̸̗͕̗̩͛̓̕͠ͅr̶̩̖̗̽͌í̷̞͕͖̂̃ę̷͚̣͕͖̮̮̿̓̕d̸̛̺̟͍̾̔͑̎̕ ̸̛̲͍̗̰͋͆́̕t̸̹̰̩̝̃̐͒͋̚o̸͖̱͍͑̈͆̇̾̀ ̸̩̜̤̌́̋͋̓̅͌ś̵͈͙͇͍̿̋̿͋͐̽c̷̪̹̲͇̾͝ḩ̵̫̘͇͛̆̀͛͆̕͜͝ḙ̴̪͙̙͚͙̐̾͑́̃͛d̶̬̙̤̥͐͗͛̈́͜u̷̖̭̞̦͔̥̦̐͑̎͘ḷ̵̌e̵̜͔̭̖͑̓̀ ̵̭̙̯̒́̃͗̈́̇͝a̶̧̮͔͙̺͊̌͛͘̕͝n̸̟̝̩̄̌̀̾͗͊̍ ̵̨̛̫̭̮̞̏͌̑ą̶̩̰̦̝͓̞͆p̶̢̰͙̠̜̗̻͑̊̍̂͗p̵̡̡̦̬̣̃̅̀̀̒͘ǫ̵̙͈͈̻͆ị̷͉̮͓͛̑̒̊̊͊̈́͜n̸̙͎̞̻͂̄͗̀t̴̅͋͐ͅm̷͎̠̰̋̀͂̂ͅe̶̺̽̈́̽̈n̵̩͋͂͂́̋̀ț̶̻̹͓͚́́͐̍̎͠ ̷̪̏͝w̵̡̦͙̣͒͌ḭ̴̝̞̜̟̖̈́̑̀̈̈́̂ţ̸̀̎̽̓͂̈́h̵̡͗́̀̊̅͝ ̷̪̻̪̣̼͑̑͒͒̃ḋ̸͇̙̞̻͔͂̋̏͊o̶͓̼̟̗͒̐̏̉̒̉̂c̶̦͈̬̤͚͖͂t̴̟̪̖̣̆̎̊ō̵̙̙̂̏́̈́͆ŕ̸̨̛͇̲̬̣̦̄͛̈́͒ ̷̼̘͈̮͆̓̄̂̅͒̕p̴̗͙̀̏̒ė̶̢̫̘̋̑̔p̸̧̢̯̲̪̝̈́͑̈͒̂p̴̨̾́ë̷̢̥̥͈͔̟͒̾̓̚͠r̵̬͍̖̭̙̖̔͊͌͛̅̇"]

  if message.content.startswith("-ym") or message.content.startswith("-yomama"):
    await message.channel.send("Yo mama is so " + random.choice(adjective) + " she " + random.choice(verb) + "!")
  if message.content.startswith("-yd") or message.content.startswith("-yodad"):
    await message.channel.send("Yo dad is so " + random.choice(adjective) + " he " + random.choice(verb2) + "!")
  if message.content.startswith("-dn") or message.content.startswith("-deeznuts"):
    await message.channel.send("DEEZ NUTS IN YO MOUTH. GOTEEEEM")

keep_alive()
my_secret = os.environ['token']
client.run(my_secret)
