# discord-bot

## **simple discord-bot with echo and calculation function**

### **prerequisites**:
- administration rights on a discord-server
- discords discord.py api (https://discordpy.readthedocs.io/en/stable/)

### **setup**:
- install discord.py api with the command `pip install discord`
- create a bot on https://discord.com/developers/applications 
    <br>-> new application
    <br>-> name your bot
    <br>-> click on `bot` in the left menu and click `Add bot`
    <br>-> copy the created token and save it somewhere
    <br>-> click on `OAuth2` in the left menu and click on `URL-Generator`
    <br>-> select `bot`. This opens a menu in which you can decide which permissions the bot will get
    <br>-> following permissions are needed for the bot to work:

        - read messages/view channels
        - send messages
        - send messages in threads
    -> copy the created link into your browser and select the server you want your bot to operate on
    <br>-> the bot should now show as offline in the serverlist
- open the main.py script and add the token in the second line of the code
- run the code. The bot should appear as an online user on discord now

### **usage**:
- the bot reacts to two different commands:
    <br>-> `/echo "text"` lets the bot repeat everything you wrote after the command `/echo`
    <br>-> `/calc "math"` lets the bot do math tasks. It can use all arithmetic operations which are available in python, e.g.:
  
        - + addition, - subtraction, * multiplication, / division
        - ** potentation, & conjunction, ^ disjunction
