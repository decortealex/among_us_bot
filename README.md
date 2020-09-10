# among_us_bot

Simple Discord bot programmed in Python that adds chat commands to mute and unmute an entire channel at once.

**COMMANDS** </br>
```$mutechannel``` - Server mutes the entire channel that the user of the command is currently in. </br>
                     ONLY works when user has permissions ```mute-members``` and when the user is in a channel. </br>
               
```$unmutechannel``` - Unmutes the entire channel that the user of the command is currently in. </br>
                       ONLY works when user has permissions ```mute-members``` and when the user is in a channel. </br>
                       
The among_us.ahk script is a AutoHotKey script that binds ```CTRL+ALT+INS``` to send ```$mutechannel``` into the text channel currently open in Discord. </br>
```CTRL+ALT+HOME``` is bound to send ```$unmutechannel``` into the text channel currently open in Discord.

**INSTRUCTIONS** </br>
1. Make a bot on the Discord Developer Portal. </br>

2. Install discord.py from pip </br>
   ```pip install discord``` </br>
3. Install dotenv from pip </br>
   ```pip install python-dotenv``` </br>
4. In the root directory of the repository, create a .env file with the following lines: </br>
   ```DISCORD_TOKEN={your-bot-token}``` 
5. Run ```bot.py``` to start the bot, run ```bot.pyw``` to hide the console window while the bot is running.
