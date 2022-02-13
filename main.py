print("""
                                                                                            
888b      88     ,a8888a,        ,a8888a,     88888888ba                                        
8888b     88   ,8P"'  `"Y8,    ,8P"'  `"Y8,   88      "8b                                       
88 `8b    88  ,8P        Y8,  ,8P        Y8,  88      ,8P                                       
88  `8b   88  88          88  88          88  88aaaaaa8P'  ,adPPYYba,  8b,dPPYba,  8b,dPPYba,   
88   `8b  88  88          88  88          88  88""''""8b,  ""     `Y8  88P'   "Y8  88P'    "8a  
88    `8b 88  `8b        d8'  `8b        d8'  88      `8b  ,adPPPPP88  88          88       d8  
88     `8888   `8ba,  ,ad8'    `8ba,  ,ad8'   88      a8P  88,    ,88  88          88b,   ,a8"  
88      `888     "Y8888P"        "Y8888P"     88888888P"   `"8bbdP"Y8  88          88`YbbdP"'   
                                                                                   88           
                            JAMES' N00Barp Spoof Detector 1.0                      88           
                                            -PY-07-L1    
                                                                                            
Welcome to James' n00b lvl ARP Spoof Detector!
This program runs a quick scan to check for repeat MAC Addresses in you CAM Table, which could indicate a possible
ARP Poisoning attack.
If the system recognizes an abnormality, the IP and MAC address will be recorded to file named "arp_attacks.txt" 
in the "Logs" folder. Please contact your IT Dept. IMMEDIATELY!""")

def main() -> object:
    import extraction
    import identify
    try:
        start_scan = input("\nPress \"1\" to start ARP Scan or \"0\" to QUIT: ")
        if start_scan == "1":
            extraction.arpextraction()
        elif start_scan == "0":
            exit()
        else:
            print("You must enter an appropriate value.")

        with open("./Logs/parsed_arp_table.txt", "r") as prsd_tbl:
            identify.identify_ducplicates(prsd_tbl)
    except:
        print("A problem has occurred trying to run your scan. Please try again later.")

if __name__==main():
    main()
