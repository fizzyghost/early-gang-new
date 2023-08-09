import codecs
import socket

def send_message(host, port, message):
    try:
        socket.socket.connect((host, port))
        encoded_message = codecs.encode(message, "rot13")
        socket.socket.send(encoded_message)
    except Exception as e:
        return "Error occurred: " + str(e)

def receive_message():
    try:
        data = socket.socket.recv(1024)
        decoded_message = codecs.decode(data, "rot13")
        return decoded_message
    except Exception as e:
        return "Error occurred: " + str(e)

host = "localhost"
port = 1234
message = "Hello, World!"

send_message(host, port, message)
received_message = receive_message()

print("Received Message:", received_message)
