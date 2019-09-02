import socket
import sys

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as error:
    print('It Broke Cuz')
    
host = input("Imput the IP or Hostname: ")
hostIP = socket.gethostbyname(host)

port_1 = input("Enter the First port: ")
port_1 = int(port_1)
port_2 = input("Enter the Last Port: ")
port_2 = int(port_2)
    
print(hostIP + " Is Your Target")

def pscan(port):
    try:
        s.connect((hostIP,port))
        s.shutdown(2)
        return(True)
    except:
        return(False)

def main():
    for x in range(port_1,port_2):
        if pscan(x):
            print("Port ",x," Is Open!")
        else:
            print("Port ",x, " Is Closed!")

main()
