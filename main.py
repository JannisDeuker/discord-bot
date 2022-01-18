from discord.ext import commands
TOKEN = "insertToken"

bot = commands.Bot(command_prefix="!")

@bot.event
# Login message
async def on_ready():
    print(f'{bot.user} succesfully logged in!')

@bot.event
async def on_message(message):
    # Make sure the Bot doesn't respond to it's own messages
    if message.author == bot.user: 
        return
    # Echo function
    if (message.content.startswith('/echo ')):
        await message.channel.send(message.content.replace(message.content[0:6],'',1))
        print(f'{bot.user} echoed following message: ' + message.content.replace(message.content[0:6],'',1))
    # Calc function
    try:
        if (message.content.startswith('/calc ')):
            remCalc = message.content.replace(message.content[0:6],'',1)
            await message.channel.send(eval(remCalc))

    except SyntaxError:
        await message.channel.send('Rechnung konnte nicht durchgeführt werden, bitte prüfe Eingabe')
    except NameError:
        await message.channel.send('Rechnung konnte nicht durchgeführt werden, bitte prüfe Eingabe')
    except ZeroDivisionError:
        await message.channel.send('Division durch 0 nicht möglich')
        '''
        # Addition
        if '+' in message.content:
            remCalc = message.content.replace(message.content[0:6],'',1)
            numList = remCalc.split('+')
            Komischer Versuch von mir, der alle Rechenarten vereinen sollte, aber '-' wollte nicht
            for i in range(0, len(numList),1):
                if '*' in numList[i]:
                    multList = numList[i].split('*')
                    for k in range(0, len(multList),1):
                        if '/' in multList[k]:
                            multDivList = multList[k].split('/')
                            multDivResult = int(multDivList[0])
                            print(int(multDivList[0]))
                            for l in range (1, len(multDivList),1):
                                multDivResult = multDivResult / int(multDivList[l])
                            multList[k] = multDivResult
                    multResult = 1
                    for j in range (0, len(multList),1):
                        multResult = multResult * int(multList[j])
                    numList[i] = multResult
            result = 0
            for i in range(0, len(numList),1):
                result = int(numList[i]) + result
            await message.channel.send(result)
        # Subtraktion
        elif '-' in message.content:
            remCalc = message.content.replace(message.content[0:6],'',1)
            numList = remCalc.split('-')
            result = int(numList[0])
            for i in range(1, len(numList),1):
                result = result - int(numList[i])
            await message.channel.send(result)
        # Multiplikation
        elif '*' in message.content:
            remCalc = message.content.replace(message.content[0:6],'',1)
            numList = remCalc.split('*')
            result = 1
            for i in range(0, len(numList),1):
                result = result * int(numList[i])
            await message.channel.send(result)
        # Division
        elif '/' in message.content:
            remCalc = message.content.replace(message.content[0:6],'',1)
            numList = remCalc.split('/')
            result = int(numList[0])
            for i in range(1, len(numList),1):
                if (numList[i] == 0):
                    await message.channel.send("Division durch 0 nicht möglich")
                    break
                result = result / int(numList[i])
            await message.channel.send(result)
        else:
            await message.channel.send("Fehlerhafte Eingabe")
            '''
    await bot.process_commands(message)

bot.run(TOKEN)