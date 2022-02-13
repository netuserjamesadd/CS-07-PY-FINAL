import datetime

def identify_ducplicates(a_tbl):

    print("\n\n<<-----Running ARP scan----->>\n\n")

    arp_tbl = {}
    for ip_mac_pair in a_tbl:
        (ip_a, mac_a) = ip_mac_pair.split()
        arp_tbl[ip_a] = mac_a
    #print(arp_tbl)
    spoof_threat = {}
    for ip_a, mac_a in arp_tbl.items():
        spoof_threat.setdefault(mac_a, set()).add(ip_a)
    arp_threat = [ip_a for ip_a, values in spoof_threat.items() if len(values) > 1]
    if len(arp_threat) >= 1:
        with open("./Logs/arp_attacks.txt", "a+") as attax:
            attax.write(f"{datetime.datetime.now()} <--> {ip_a}{arp_threat}\n")
        print("\033[1;33;41m !!! WARNING !!! WARNING !!! WARNING !!!")
        print("You may be a victim of an ARP Poisoning Attack. Call you IT Dept. immediately!")
        print(f"The following MAC Address appears to be duplicated: {arp_threat}")
    else:
        print(f"Scan concluded at: {datetime.datetime.now()}\nThere are no duplicate MAC addresses in your CAM table.")

if __name__ == "__main__":
    identify_ducplicates(a_tbl=open("./Logs/parsed_arp_table.txt", "r"))
