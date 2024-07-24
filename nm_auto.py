import argparse
import subprocess
import datetime
import threading
import os

NMAP_ARGS = "-A"

def run_nmap_scan(target, output_file):
    command = f"nmap {NMAP_ARGS} {target} -oN {output_file}"
    try:
        print(f"Starting Nmap scan for {target} with command: {command}")
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
        print(f"Nmap scan for {target} completed.")
    except subprocess.CalledProcessError as e:
        print(f"Error scanning host {target}: {e}")

def notify_progress(target):
    print(f"Scan in progress for {target}. Please wait...")

def main():
    parser = argparse.ArgumentParser(description="Automate Nmap scans with fixed arguments.")
    parser.add_argument('--target', required=True, help='Target IP(s), range(s), subnet(s), or URL')
    args = parser.parse_args()

    if not args.target:
        print("Error: No target specified.")
        return

    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    output_file = f"{args.target.replace('/', '_').replace(':', '_')}_{timestamp}.txt"

    progress_thread = threading.Thread(target=notify_progress, args=(args.target,))
    scan_thread = threading.Thread(target=run_nmap_scan, args=(args.target, output_file))

    progress_thread.start()
    scan_thread.start()

    progress_thread.join()
    scan_thread.join()

    print(f"Nmap scan completed for {args.target}. Results saved to {output_file}.")

if __name__ == "__main__":
    main()
