 ## Ticket commands
## Claim command
@events.on_message
async def claimcommand(message):
    if message.content == f"{config.PREFIX}claim":
        bot.send_message(message.channelId, embed=claimembed)
claimembed = Embed(title="CLAIMED",description=f"This ticket is now claimed by  ")
## New command
@events.on_message
async def newcommand(message):
    if message.content == f"{config.PREFIX}new":
        bot.create_channel(serverid=message.guildId,name=f"Ticket",type="chat", ispublic=False)
        ## Close command
@events.on_message
async def closeticket(message):
    if message.content == f"{config.PREFIX}close":
        bot.delete_channel(channelid=message.channelId)

## rename ticket 
@events.on_message
async def renameticket(message):
    if message.content == f"{config.PREFIX}rename":
        new_name= message.content[8:]
        bot.update_channel(channelid=message.channelId,name=new_name)