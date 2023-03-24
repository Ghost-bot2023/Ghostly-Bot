import config
from nextguild import Client, Events, Embed
token = config.TOKEN

bot = Client(token)
events = Events(bot)
@events.on_ready
async def on_ready_example():
 print("Bot is ready!")

@events.on_member_join
async def member_joined(member):
    bot.send_message("f9cbb9fc-f175-4e5e-b6f6-b9e8823ce926", f" has joined the server!")
@events.on_member_leave
async def member_leave(member):
    bot.send_message("f9cbb9fc-f175-4e5e-b6f6-b9e8823ce926", f" has leaved the server!")
@events.on_message
async def clearcommand(message):
    if message.content == f"{config.PREFIX}clear":
        bot.purge(message.channelId, amount="100")
        bot.send_message(message.channelId, f"Cleared")
## Help command
@events.on_message
async def helpcommand(message):
    if message.content == f"{config.PREFIX}help":
        bot.send_message(message.channelId, embed=helpembed)

helpembed = Embed(
    title="🤖 Need help, human? 🤖",
    description="My commands are at your service!",
    color="#36393f"
)
helpembed.add_field(
    "🆘 help",
    "Displays this help menu"
)
helpembed.add_field(
    "🫂 credits",
    "See the credits of people who work on the bot"
)
helpembed.add_field(
    "👢 kick (staff)",
    "Kicks a member from the server (staff only)"
)
helpembed.add_field(
    "🔨 ban (staff)",
    "Bans a member from the server (staff only)"
)
helpembed.add_field(
    "🔓 unban (staff)",
    "Unbans a member from the server (staff only)"
)
@events.on_message
async def bugreportcommand(message):

    if message.content == f"{config.PREFIX}reportbug":
        bot.send_message(channel_id="175e724e-0246-4b1f-9466-078a919ff8b1", embed=bugreportembed)
bug = "COMING SOON"
bugreportembed = Embed(title="NEW BUG REPORT ",description=f"There is a new bug report! The bug report is {bug}")

@events.on_message
async def kickcommand(message):
    if message.content.startswith(f"{config.PREFIX}kick"):
        args = message.content.split(" ")
        if len(args) < 2:
            bot.send_message(message.channelId, "Please specify a user to kick!")
            return
        user_to_kick =  message.content[6:]
        bot.kick_member(message.guildId, user_to_kick)
        bot.send_message(message.channelId, f"User  has been kicked!")
@events.on_message
async def bancommand(message):
    if message.content.startswith(f"{config.PREFIX}ban"):
        args = message.content.split(" ")
        if len(args) < 2:
            bot.send_message(message.channelId, "Please specify a user to ban!")
            return
        user_ban = message.content[5:]
        bot.ban_member(message.guildId,user_ban)
        bot.send_message(message.channelId, f"User has been banned!")
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

@events.on_message
async def cre(message):
    if message.content == f"{config.PREFIX}credits":
        bot.send_message(message.channelId, embed=creditsembed)

creditsembed = Embed(title="Credits!!",color="#f8f8ff", footer="Made on the 3/23/23")
creditsembed.add_field("@RaezDev", "Head Developer "),
creditsembed.add_field("@Darkfoxy", "Head Developer "),
creditsembed.add_field("@Arjun Sharda" , "Make the library(NextGuild)"),
creditsembed.add_field("@erik" , "Make the library(NextGuild)"),

events.run()