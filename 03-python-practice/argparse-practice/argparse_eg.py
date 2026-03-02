import argparse

def check_disk(threshold):
    print(f"Checking disk usage...alerting if above {threshold}%")

def check_cpu():
    print("Checking cpu usage...")

def main():
    #creare parser
    parser = argparse.ArgumentParser(description="Practice code for argparse")

    #add arguments
    parser.add_argument("--host", required=True, help="Server to monitor")
    parser.add_argument("--threshold", type=int, default=80, help="Alert threshold %")
    parser.add_argument("--check-disk", action="store_true", help="run disk check")
    parser.add_argument("--check-cpu", action="store_true", help="run cpu check")

    #parse
    args = parser.parse_args()

    #use the arguments
    print(f"Monitoring: {args.host}")

    if args.check_disk:
        check_disk(args.threshold)
    
    if args.check_cpu:
        check_cpu()

    if not args.check_disk and not args.check_cpu:
        print("No checks specified. Use --check-disk or --check-cpu")

if __name__ == "__main__":
    main()