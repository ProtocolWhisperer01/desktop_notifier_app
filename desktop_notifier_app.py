#############################################################################
## 									   ##
##	Title : Desktop Notifier App					   ## 	
##									   ##
##	Author : Ernest Odhiambo Elnino					   ##
##									   ##
##	Github : https://github.com/ProtocolWhisperer01 		   ##
#############################################################################

import requests
from plyer import notification

not_title = 'GREETINGS SIR! HOW IS YOUR MORNING ?'
not_message = 'From my side everything is well, Hope you have a wonderful day!.'

notification.notify(
    title = notification_title,  
    message = notification_message,  
    app_icon = None,  
    timeout = 10,  
    toast = False
    )
