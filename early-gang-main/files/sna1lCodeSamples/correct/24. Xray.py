import codecs
import socket

def send_message(host, port, message):
    try:
        client_socket = socket.socket()
        client_socket.connect((host, port))
        encoded_message = codecs.encode(message, "rot_13")
        client_socket.send(encoded_message)
    except Exception as e:
        return "Error occurred: " + str(e)

def receive_message():
    try:
        client_socket = socket.socket()
        client_socket.connect(("localhost", 1234))
        data = client_socket.recv(1024)
        decoded_message = codecs.decode(data, "rot_13")
        return decoded_message
    except Exception as e:
        return "Error occurred: " + str(e)

host = "localhost"
port = 1234
message = "Hello, World!"

send_message(host, port, message)
received_message = receive_message()

print("Received Message:", received_message)
