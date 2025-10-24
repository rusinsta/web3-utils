from eth_utils import to_checksum_address

def main():
    addr = input("Enter Ethereum address: ")
    print("Checksum:", to_checksum_address(addr))

if __name__ == "__main__":
    main()
