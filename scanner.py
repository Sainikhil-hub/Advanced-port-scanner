import socket
import threading
import argparse

# Argument parser (CLI)
parser = argparse.ArgumentParser(description="Advanced Port Scanner")
parser.add_argument("-t", "--target", help="Target IP")
parser.add_argument("-sp", "--start-port", type=int, help="Start port")
parser.add_argument("-ep", "--end-port", type=int, help="End port")
parser.add_argument("-o", "--output", help="Save results to file")
args = parser.parse_args()

# Fallback to input if CLI not provided
target = args.target or input("Enter target IP: ")
start_port = args.start_port or int(input("Start port: "))
end_port = args.end_port or int(input("End port: "))
output_file = args.output

lock = threading.Lock()
open_ports = []

def scan(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)

        result = s.connect_ex((target, port))

        if result == 0:
            try:
                service = socket.getservbyport(port)
            except:
                service = "unknown"

            try:
                banner = s.recv(1024).decode().strip()
                if not banner:
                    banner = "No banner"
            except:
                banner = "No banner"

            result_text = f"[+] Port {port} OPEN ({service}) | {banner}"

            with lock:
                print(result_text)
                open_ports.append(result_text)

        s.close()
    except:
        pass


print("="*50)
print(f"Scanning Target: {target}")
print(f"Port Range: {start_port}-{end_port}")
print("="*50)

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

    if output_file:
        with open(output_file, "w") as f:
            for line in open_ports:
                f.write(line + "\n")
        print(f"Results saved to {output_file}")
else:
    print("No open ports found.")

print("="*50)
print("Scan Complete.")
