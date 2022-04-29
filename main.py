import os
import discord

my_secret = os.environ['TOKEN']
client = discord.Client()




# testing block

# def check_hello():
#     is_hello = random.choice(hello.hello_check)
#     print(is_hello)
#     print(type(is_hello))
#     return is_hello

# end testing block

@client.event
async def on_ready():
    print('We have logged in a {0.user}.  Suggest-bot is active'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

   

    # /suggest begin
    if message.content.startswith("/suggest"):
        await message.channel.send("a suggestion has been made")



client.run(my_secret)
