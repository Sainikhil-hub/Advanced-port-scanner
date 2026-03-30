import socket
import threading

print("="*50)
print("        Advanced Port Scanner")
print("="*50)

target = input("Enter target IP: ")

start_port = int(input("Start port: "))
end_port = int(input("End port: "))

lock = threading.Lock()
open_ports = []

def scan(port):
    global open_ports
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)

        result = s.connect_ex((target, port))

        if result == 0:
            try:
                service = socket.getservbyport(port)
            except:
                service = "unknown"

            # Banner grabbing
            try:
                banner = s.recv(1024).decode().strip()
                if not banner:
                    banner = "No banner"
            except:
                banner = "No banner"

            with lock:
                print(f"[+] Port {port} OPEN ({service}) | {banner}")
                open_ports.append(port)

        s.close()

    except:
        pass


threads = []

for port in range(start_port, end_port + 1):
    t = threading.Thread(target=scan, args=(port,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()


print("\n" + "="*50)

if open_ports:
    print("Scan Summary:")
    print(f"Total Open Ports: {len(open_ports)}")
    print("Ports:", open_ports)
else:
    print("No open ports found.")

print("="*50)
print("Scan Complete.")
