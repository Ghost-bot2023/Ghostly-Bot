from nextguild import Client, Events, Message, Embed
import logging
import config
from random import choice
token = config.TOKEN
bot = Client(token)
events = Events(bot)
logging.basicConfig(filename='errors.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

@events.on_ready
async def on_ready():
    try:
        print("I'm online!")
    except Exception as e:
        print(e)
        logging.exception(e)


@events.on_message
async def clearcommand(message):
   try:
    if message.content.startswith(f"{config.PREFIX}clear"):
        args = message.content.split(" ")
        if len(args) < 2:
            bot.send_message(message.channelId, "Please specify the amount of message you want cleared!")
            bot.delete_message(message.channelId, message.messageId)
            return
        amount = message.content[6:]
        amount = bot.purge(message.channelId,int(amount))
        bot.send_message(message.channelId, f"Cleared {amount} messages!")
        return
   except Exception as e:
       bot.send_message(message.channelId, content=f"{e}")
       bot.delete_message(message.channelId, message.messageId)
# Help Staff command
@events.on_message
async def helpstaffcommand(message):

    if message.content == f"{config.PREFIX}helpstaff":
        bot.send_message(message.channelId, embed=helpstaffembed)
        bot.delete_message(message.channelId, message.messageId)

helpstaffembed = Embed(
    title="🤖 Need help, human? 🤖",
    description="Staff commands are at your service!",
    color="#36393f",
    footer="Support Server: https://www.guilded.gg/Ghostly"
)
helpstaffembed.add_field(
    "👢 kick (staff)",
    "Kicks a member from the server (staff only)"
)
helpstaffembed.add_field(
    "🔨 ban (staff)",
    "Bans a member from the server (staff only)"
)
helpstaffembed.add_field(
    "🔓 unban (staff)",
    "Unbans a member from the server (staff only)"
)
helpstaffembed.add_field(
    "🧼 clear (staff)",
    "Clear messages from a channel(less than 100 messages)(staff only)"
)
helpstaffembed.add_field(
    "🤖 say (staff)",
    "Say something as the bot(staff only)"
)
helpstaffembed.add_field(
    "📇 haverole (staff)",
    "See if a member have a role(staff only)"
)
helpstaffembed.add_field(
    "✅ addrole (staff)",
    "Add a role to someone(staff only)"
)
helpstaffembed.add_field(
    "❌ removerole (staff)",
    "Remove a role from someone(staff only)"
)
helpstaffembed.add_field(
    "#️⃣ userid (staff)",
    "Get a user Id(staff only)"
)
# Help Fun command
@events.on_message
async def helpfuncommand(message):

    if message.content == f"{config.PREFIX}helpfun":
        bot.send_message(message.channelId, embed=helpfunembed)
        bot.delete_message(message.channelId, message.messageId)

helpfunembed = Embed(
    title="🤖 Need help, human? 🤖",
    description="Fun commands are at your service!",
    color="#36393f",
    footer="Support Server: https://www.guilded.gg/Ghostly"
)
helpfunembed.add_field(
    "🎲 dice (fun)",
    "Roll a dice to get it number from 0 to 20"
)
helpfunembed.add_field(
    "🃏 joke (fun)",
    "Get different joke every time"
)
# Help command
@events.on_message
async def helpcommand(message):

    if message.content == f"{config.PREFIX}help":
        bot.send_message(message.channelId, embed=helpembed)
        bot.delete_message(message.channelId, message.messageId)

helpembed = Embed(
    title="🤖 Need help, human? 🤖",
    description="My commands are at your service!",
    color="#36393f",
    footer="Support Server: https://www.guilded.gg/Ghostly"
)
helpembed.add_field(
    "🆘 help",
    "Displays this help menu"
)
helpembed.add_field(
    "🫂 about",
    "See the credits of people who work on the bot"
)
helpembed.add_field(
    "🪲 reportbug",
    "Report a bug about the bot to the bot devs"
)
helpembed.add_field(
    "🆘 helpstaff (staff)",
    "Get the help menu for staff(staff only)"
)
helpembed.add_field(
    "🆘 helpfun ",
    "Get the help menu for fun"
)
@events.on_message
async def bugreportcommand(message):
    try:
        if message.content.startswith(f"{config.PREFIX}reportbug"):
            args = message.content.split(" ")
            if len(args) < 2:
                bot.send_message(message.channelId, "Please specify the bug report!")
                return
            bugtext = message.content[11:]
            bot.send_message(channel_id="175e724e-0246-4b1f-9466-078a919ff8b1",content=f"The new bug is `{bugtext}` by {message.authorId}")
            bot.send_message(message.channelId,content="You bug report was sent to the bot dev give them time to fix it!")
            bot.delete_message(message.channelId,message.messageId)
    except Exception as e:
        bot.send_message(message.channelId, content=f"{e}")


@events.on_message
async def kickcommand(message):
        if message.content.startswith(f"{config.PREFIX}kick"):
            args = message.content.split(" ")
            if len(args) < 2:
                bot.send_message(message.channelId, "Please specify a user to kick!")
                return
            bot.kick_member(message.guildId,  message.mentions[0])
            bot.send_message(message.channelId, f"User have been kicked!")
            bot.delete_message(message.channelId, message.messageId)
            return

@events.on_message
async def bancommand(message):
    if message.content.startswith(f"{config.PREFIX}ban"):
        args = message.content.split(" ")
        if len(args) < 2:
            bot.send_message(message.channelId, "Please specify a user to ban!")
            return
        bot.ban_member(message.guildId, message.mentions[0])
        bot.send_message(message.channelId, f"User has been banned!")
        bot.delete_message(message.channelId, message.messageId)

@events.on_message
async def unbancommand(message):
    if message.content.startswith(f"{config.PREFIX}unban"):
        args = message.content.split(" ")
        if len(args) < 2:
            bot.send_message(message.channelId, "Please specify a user to unban!")
            return
        user_unban = message.content[7:]
        bot.unban_member(message.guildId, user_unban)
        bot.send_message(message.channelId, f"User has been unbanned!")
        bot.delete_message(message.channelId, message.messageId)

@events.on_message
async def cre(message):
    if message.content == f"{config.PREFIX}about":
        bot.send_message(message.channelId, embed=creditsembed)
        bot.delete_message(message.channelId, message.messageId)
creditsembed = Embed(title="Credits!!", color="#f8f8ff", footer="Made on the 3/25/23")
creditsembed.add_field("[@RaezDev](https://www.guilded.gg/Ghostly)", "Head Developer "),
creditsembed.add_field("[@Darkfoxy](https://www.guilded.gg/Ghostly)", "Head Developer "),
creditsembed.add_field("[@Arjun Sharda](https://www.guilded.gg/nextguild)", "Make the library(NextGuild)"),
creditsembed.add_field("[@Erik](https://www.guilded.gg/nextguild)", "Make the library(NextGuild)"),
creditsembed.add_field("About!!", ""),
creditsembed.add_field("Bot Invite:", " [Here](https://www.guilded.gg/b/711e240d-7b47-438b-af3a-af4f3cb39d6c)"),
creditsembed.add_field("Support Server:", "[Here](https://www.guilded.gg/Ghostly)"),
creditsembed.add_field("GitHub Repository:", "[Here](https://github.com/Ghost-bot2023/ghostlybot)"),
creditsembed.add_field("NextGuild:", "[Here](https://github.com/ArjunSharda/nextguild)"),
@events.on_message
async def saycommand(message):
    if message.content.startswith(f"{config.PREFIX}say"):
        args = message.content.split(" ")
        if len(args) < 2:
            bot.send_message(message.channelId, "Please specify what you want the bot to say!")
            return
        say = message.content[5:]
        bot.send_message(message.channelId,content=f"{say}")
        bot.delete_message(message.channelId, message.messageId)

@events.on_message
async def haverolecommand(message):
  botid = bot.get_bot_user_id()
  if botid == message.authorId:
    return
  if message.content.startswith(f"{config.PREFIX}haverole"):
    arg = message.content.split(" ")[2]
    truefalse = bot.member_has_role(message.guildId, message.mentions[0], arg)
    bot.send_message(message.channelId, f'{truefalse}')
@events.on_message
async def addrolecommand(message):
    try:
        botid = bot.get_bot_user_id()
        if botid == message.authorId:
            return
        if message.content.startswith(f"{config.PREFIX}addrole"):
                arg = message.content.split(" ")[2]
                bot.add_role(message.guildId, message.mentions[0],arg)
                bot.send_message(message.channelId,content=f"Role was added!")
                bot.delete_message(message.channelId,message.messageId)
    except Exception as e:
        bot.send_message(message.channelId, content=f"{e}")
@events.on_message
async def removerolecommand(message):
    try:
        botid = bot.get_bot_user_id()
        if botid == message.authorId:
            return
        if message.content.startswith(f"{config.PREFIX}removerole"):
                arg = message.content.split(" ")[2]
                bot.remove_role(message.guildId, message.mentions[0],arg)
                bot.send_message(message.channelId,content=f"Role was removed!")
                bot.delete_message(message.channelId,message.messageId)
    except Exception as e:
        bot.send_message(message.channelId, content=f"{e}")
@events.on_message
async def useridcommand(message):
    try:
        if message.content.startswith(f"{config.PREFIX}userid"):
            bot.send_message(message.channelId, content=f"{message.mentions[0]}")
    except Exception as e:
        bot.send_message(message.channelId, content=f"{e}")

@events.on_message
async def dicecommnad(message):
    try:
        dice = [1, 2, 3, 4, 5, 6,7,8,9,10,11,12,13,14,0,15,16,17,18,19,20,1,2, 3, 4, 5, 6,7,8,9,10,11,12,13,14,0,15,16,17,18,19,20]
        if message.content.startswith(f"{config.PREFIX}dice"):
            bot.send_message(message.channelId, content=f"The dice rolled and you got {choice(dice)}")
            bot.delete_message(message.channelId, message.messageId)
    except Exception as e:
        bot.send_message(message.channelId, content=f"{e}")
@events.on_message
async def jokecommand(message):
    joke = ["Why do we tell actors to “break a leg?” Because every play has a cast. ",
            "Yesterday I saw a guy spill all his Scrabble letters on the road. I asked him, “What’s the word on the street?”",
            "Hear about the new restaurant called Karma? There’s no menu: You get what you deserve.",
            "A woman in labor suddenly shouted, “Shouldn’t! Wouldn’t! Couldn’t! Didn’t! Can’t!” “Don’t worry,” said the doc. “Those are just contractions.”"]

    if message.content.startswith(f"{config.PREFIX}joke"):
        bot.send_message(message.channelId, content=f"The joke is: {choice(joke)}")
        bot.delete_message(message.channelId, message.messageId)



events.run()
