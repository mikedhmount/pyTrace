from scapy.all import sniff, wrpcap
import time
from datetime import datetime



def capture_packets():
    while True:
        # Create a new filename with the current timestamp
        filename = f"PCAPS/{datetime.now().strftime('%Y%m%d_%H%M%S')}.pcap"
        
        # Capture packets for an hour (3600 seconds)
        print(f"Starting packet capture to file {filename}")
        packets = sniff(timeout=30)
        
        # Write packets to file
        wrpcap(filename, packets)
        print(f"Finished capturing to {filename}")
        

        # Wait for a short time before starting a new file
        time.sleep(1)


if __name__ == "__main__":
    capture_packets()

