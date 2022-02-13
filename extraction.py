# Imported os to extract arp table and regular expressions to extract strings of data
# Originally was going to use RegEx for both extracting lines with ip AND mac addresses and parsing my file,
# but split worked great for the parsing, and since we saw it class it seemed appropriate to use.
import os
import re

# Defining main function. Starting with a try, except statement to attempt to create a folder named logs
def arpextraction():
    try:
        os.mkdir("Logs")
    except:
        pass
    os.system(r"arp -a > ./Logs/raw_arp_data.txt")
    raw_arp_table = ("./Logs/raw_arp_data.txt")
    # Doing this next step because I wanted to clear my parsed_arp_table file every time.
    # I tried opening the file in w mode, but it would overwrite each line.
    # Obviously with append alone it would keep creating duplicates, my fix was to re-write an empty file every time.
    parsed_table = open("./Logs/parsed_arp_table.txt", "w+")
    parsed_table.close()

# Used RegEx to extract the lines that included an IP and MAC to filter out titles and interface lines
# When parsing the file with RegEx, output was nested tuple. Split out first two fields, and convert it to list
    # prints for POC.
# Creating empty dictionary to write those values into. Then printing those last values into another file in ./Logs
    # filtering out broadcasts with "ff-ff" line before print.
        # print for POC   rawtbl
    with open(raw_arp_table) as rawtbl:
        #for line not in
        for splt in re.findall("([-.0-9]+)\s+([-0-9a-f]{17})", rawtbl.read()):
            split_list = list(splt[0:2])
            #print(split_list)
            #print(type(split_list))
            arp_table_dict = {}
            for ipmac_pair in split_list:
                parsed_table = open("./Logs/parsed_arp_table.txt", "a+")
                arp_table_dict[split_list[0]]=split_list[1]
            for key, value in arp_table_dict.items():
                if "ff-ff" in value:
                    continue
                if "255.255.255.255" in key:
                    break
                parsed_table.write(f"{key} {value}\n")

            #print(arp_table_dict)

if __name__ == "__main__":
    arpextraction()
