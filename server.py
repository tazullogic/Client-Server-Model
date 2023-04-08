import threading
import socket
import report as rp
import bad_words as bw
import username_log as ul
import sending_warnings as sw

# list of brand names
brands_dict = rp.brands_dict

# localhost
host = "127.0.0.1"
# do not take any reserved or well known ports
port = 55595

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
nicknames = []
emails = []



def brand_name(message):
    new_message = message.decode('ascii')
    for brandname in brands_dict:
        if brandname.lower() in new_message.lower():
            brand_count = brands_dict[brandname]
            brand_count = brand_count + 1
            brands_dict[brandname] = brand_count
            print(brands_dict[brandname])


# broadcasting messages from the server to all the clients
def broadcast(message):
    # implement the brand analytics and tracking here
    brand_name(message)

    # implement the filtering of the messages here

    for client in clients:
        client.send(message)


def handle(client):
    # Running an infinite loop here
    while True:
        try:
            # receiving 1024 bytes
            message = client.recv(1024)
            print(message)
            for word in bw.abusing_words:
                if word in message.decode('ascii'):
                    client.send("This message can not send due to bad word used!!".encode('ascii'))
                    index = clients.index(client)
                    send_to = emails[index]
                    sw.send_warning_message(send_to)

                    break
            else:
                broadcast(message)







        except:
            # find out the index of the failed client frm the clients list
            index = clients.index(client)
            clients.remove(client)
            client.close()
            # we also remove the nickname of the removed client
            nickname = nicknames[index]
            broadcast(f"{nickname} has left the chat!".encode('ascii'))
            nicknames.remove(nickname)
            email = emails[index]
            emails.remove(email)
            break


# This is the method that runs first
def receive():
    # Accepting all the connections
    while True:
        print("receive function is running on the server!")
        # returns a tuple
        # returns the client and the address of the client
        client, address = server.accept()

        # you have cut down the address str type casting
        print(f"Connected with {str(address)}")

        # we need to ask the client for the nickname
        # made change here
        name = "NICK"
        client.send(name.encode('ascii'))

        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        ul.log_username(nickname)
        email_request = "EMAIL"
        client.send(email_request.encode('ascii'))
        email = client.recv(1024).decode('ascii')
        emails.append(email)
        clients.append(client)

        print(f"Nickname of the client is {nickname}")

        broadcast(f"{nickname} joined the chat".encode('ascii'))
        # letting know the specific client that it has connected to the server
        client.send("Connected to the server".encode('ascii'))

        # define and run a thread
        # because we want to be able to handle multi clients same time

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


# main method
print("Server is listening..........")
receive()
