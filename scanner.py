import socket 
import sys

def scan_port(target, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1.0)
    result=s.connect_ex((target, port))
    if result==0:
        print(f"porta {port}: ABERTA")
        s.close()

def main():
    target = input("digite o endereco ip ou site (ex: 127.0.0.1 ou google.com): ")
    print(f"iniciando scan em {target}")
    print("aguarde...")
    for port in range(1, 101):
        scan_port(target, port)
if __name__ == "__main__":
    main()