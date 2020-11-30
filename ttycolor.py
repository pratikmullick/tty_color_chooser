#!/usr/bin/env python3

# Copyright 2018-2020, Pratik Mullick.
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import random
import os
import sys
import subprocess
import argparse
import tempfile

import converter

class Program:

    def __init__(self):
        self.name = "ttycolor"
        self.description = "A program to change colors for TTY console in Linux."

        self.parser = argparse.ArgumentParser(prog=self.name, description=self.description, allow_abbrev=False)
        self.parser.add_argument("-s", "--setup", action="store_true", help="Sets up console colors")
        self.parser.add_argument("-v", "--version", action="version", version="%(prog)s 0.6 beta")
        self.parser.add_argument("-o", "--output", type=str, metavar="OUTFILE", help="Output file name")
        self.parser.add_argument("filename", metavar="FILE", type=str, help="Input file in YAML format")
        
        self.args = self.parser.parse_args()

        self.filename = self.args.filename

    def main(self):

        if not os.path.isfile(self.filename):
            print("File not found.")
            self.parser.print_usage()
            sys.exit()

        line_array = converter.Operations(self.filename).dict2svr()

        if self.args.setup:
            with tempfile.NamedTemporaryFile(mode="w+t") as dummy:
                for line in line_array:
                    dummy.write(line)
                dummy.seek(0)
                subprocess.run(["setvtrgb", dummy.name])
                subprocess.run(["clear"])

        if self.args.output:
            with open(self.args.output,"w") as outfile:
                for line in line_array:
                    outfile.write(line)
            print("You can use setvtrgb command on {}".format(self.args.output))
        else:
            for line in line_array:
                line = line.strip('\n')
                print(line)

# Running the program when invoked.
if __name__ == "__main__":
    prog = Program()
    prog.main()

