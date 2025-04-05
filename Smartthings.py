import SmartThings

token = '372563b7-09f8-485b-8c95-261793424ad9'
ST = SmartThings.Account(token)
# Reference the SmartThings API documentation for information regarding the
# format of capabilities, commands, and arguments

ST.CONTROL_DEVICE(ST.devices['Home']['Ashley1'], capability=switch, command=off(), arguments=None)

