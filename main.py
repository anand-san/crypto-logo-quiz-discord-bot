#Author : cF
#Contact : gg.gg/cryptosurge
import discord
import sys

import quiz

client = discord.Client()
quiz = quiz.Quiz(client)

@client.event
async def on_ready():
    print('Logged in as: ' + client.user.name)
    print('User ID: ' + client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('$$$exitme'):
        await client.send_message(message.channel, 'Leaving server. BYE!')
        await client.close()
        exit()
        
    elif (message.content.startswith('!stop') or 
          message.content.startswith('$stop')):
        await quiz.stop()
    elif (message.content.startswith('$resetscore')):
        await quiz.reset()        
    elif (message.content.startswith('$start') or 
          message.content.startswith('!start')):
        await quiz.start(message.channel)      
    elif (message.content.startswith('$scores')):
        await quiz.print_scores()    
    elif (message.content.startswith('$next')):
        await quiz.next_question(message.channel)
    elif quiz is not None and quiz.started():
        await quiz.answer_question(message)

if __name__ == "__main__":
    
    if len(sys.argv) < 2:
        print('Usage: python bot.py APP_BOT_USER_TOKEN')
        exit()
        
client.run(sys.argv[1])
