

#Main Config:#
token = "OTMxMjk2NDU1OTI5NTAzODI0.YeCXaQ.KuWX4-Iyi1B7CdyzoD559h-2gbE"                 
CommandPrefix = "7"    
activitytype = 'Playing'                        #Accepted Values are Watching, Listening, Playing, or Streaming.
botstatusmessage = '7 ON TOP' 

developerid = 000000000000000000                #Insert the userID here were the bot will send all error dms too. THE USER MUST BE IN THE SAME DISCORD SERVER THAT THE BOT IS IN!
guildID = 931266588588539965                    #Insert the guildID of the server that the bot will be running in here.
statscooldownamount = 30                        #As the bot checks for guild updates using loops, enter a loopcooldown time here, I reccomend 30 seconds as preset, anything under 15 seconds will most likely get you ratelimited by dsicord.
embedcolor = 0x00000



#Server Member Count#
ServerMembersCheckEnabled = True                            #True for enabled, False for disabled
IDofChannelForServerMembers = 000000000000000000            #ID of Voice channel to update with server member count
NameofStatsChannel1 = str("All Members: ")                  #Adjusts the name of the Voice channel, LEAVE THE SPACE!


#Role 1 Count #                                      
Role1CountCheckEnabled = True                              #True for enabled, False for disabled
IDofRole1 = 000000000000000000                             #ID of the server role to keep track of
IDofChannelForRole1Check = 000000000000000000              #ID of Voice channel to update with the Role1 count with the role specified above
NameofRole1Channel = str("Role 1: ")                       #Adjusts the name of the Voice channel, LEAVE THE SPACE!

#Role 2 Count #
Role2CountCheckEnabled = True                              #True for enabled, False for disabled
IDofRole2 = 000000000000000000                             #ID of the server role to keep track of
IDofChannelForRole2Check = 000000000000000000              #ID of Voice channel to update with the Role2 count with the role specified above
NameofRole2Channel = str("Role 2: ")                       #Adjusts the name of the Voice channel, LEAVE THE SPACE!

#Bot Count #
BotCountCheckEnabled = True                                #True for enabled, False for disabled
IDofChannelForBotCheck = 000000000000000000                #ID of Voice channel to update with the bot count
NameofBotChannel = str("Bots: ")                           #Adjusts the name of the Voice channel, LEAVE THE SPACE!

#Bans Count #                                     
BansCountCheckEnabled = True                               #True for enabled, False for disabled  
IDofChannelForBansCheck = 000000000000000000               #ID of Voice channel to update with the server ban count
NameofBansChannel = str("Bans: ")                          #Adjusts the name of the Voice channel, LEAVE THE SPACE!
