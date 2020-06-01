# this script was used to connect to telegram peagle bot to get the currnet dynamic ip address of the server 
# so that could be written into a txt file.

# this script is no longer required as the server is now hosted on google app engine or locally and 
# server address is now static....

# import telepot
# import time
# import ipaddress
# import os,signal,sys


# receive_ip = False
# bot = telepot.Bot('1089525974:AAFxOxMt0mx5bV4ehlJC04XRVz_IY6L9i6I')

# def check_msg(message):
#     try:
#         ipaddress.ip_address(str(message))
        
#         return True

#     except:
#         return False

# def receive_msg(msg):
#     global receive_ip
#     chat_id = msg['chat']['id']
#     received_msg = msg['text']
#     is_msg_ip = check_msg(received_msg)
#     if (is_msg_ip and receive_ip):
#         bot.sendMessage(chat_id,"IP address received : "+str(received_msg))
#         ip_file = open("Desktop/client/ip_file.txt", "w")
#         ip_file.write(str(received_msg))
#         ip_file.close()
        
#         os.kill(os.getpid(),signal.SIGKILL)
        
#     else:
#         receive_ip = True
#         bot.sendMessage(chat_id,"Send IP address")
        
    

# bot.message_loop(receive_msg)

# while True:
#     time.sleep(10)
