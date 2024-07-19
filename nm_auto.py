import subprocess
import datetime
import argparse
import os

def run_nmap_scan(target, output_file):
    command = f"nmap -A -sS -sV -O -p 1-65535 -sU -T4 {target}"

    print("Starting comprehensive nmap scan...")
    print(f"Command: {command}")

    with open(output_file, 'w') as f:
        f.write(f"### Comprehensive Nmap Scan ###\n")
        try:
            result = subprocess.run(command, capture_output=True, text=True, shell=True, check=True)
            f.write(result.stdout + "\n")
            print("Comprehensive nmap scan completed successfully.\n")
        except subprocess.CalledProcessError as e:
            f.write(f"Error running nmap scan: {e}\n")
            print(f"Error running nmap scan: {e}\n")

def main():
    parser = argparse.ArgumentParser(description="Run a comprehensive nmap scan on a target and save the results to a text file.")
    parser.add_argument('--target', required=True, help='Target IP(s), range(s), subnet(s), or URL (e.g., 192.168.1.0/24, 10.0.0.1-10, example.com)')
    args = parser.parse_args()

    # Define the output file name with target and timestamp
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_target = args.target.replace("/", "_").replace(".", "_")
    output_file = f'{safe_target}_{timestamp}.txt'

    print(f"Starting comprehensive nmap scan on {args.target}. Results will be saved to {output_file}.\n")

    # Run nmap command and save results to the output file
    run_nmap_scan(args.target, output_file)

    # Notify the user
    if os.path.exists(output_file):
        print(f'Nmap comprehensive scan completed for {args.target}. Results saved to {output_file}.')
    else:
        print(f'Error: Nmap scan failed for {args.target}. No output file created.')

if __name__ == "__main__":
    main()
