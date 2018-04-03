#!/usr/bin/python3
#
# Input file 'natinput.txt' is a list for each line.
# Each line then will be a dictionary {} of keys and values

import csv
#import sys


with open('natinput.txt', 'r') as infile:
    with open('pa_nat_out.txt', 'w') as outfile:

        reader = csv.reader(infile)
        output_list = list(reader)


        print("Skipping first line of Headers. \n")
        for line in range(len(output_list)):
            if line > 0:
                nat_rule_list = output_list[line]

     #           try:

# Initialise "set_cmd" string with initial syntax
                set_cmd = "set rulebase nat rules "

                for var in range(len(nat_rule_list)):
                    set_cmd += str(nat_rule_list[var])
                    set_cmd += " "

# Print cmds to file, then to screen
                print(set_cmd, "\n", file=outfile)
                print(set_cmd, "\n")

        print("# commit\n" + "# exit\n" + "> show running nat-policy\n")
        print("# commit\n" + "# exit\n" + "> show running nat-policy\n", file=outfile)
     #           except OSError as os_err:
     #             print("OS error: {0}".format(os_err))



