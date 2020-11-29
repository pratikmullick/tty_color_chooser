#!/usr/bin/env python3
import random
import os
import sys
import subprocess
import argparse
import tempfile

from string import digits, ascii_lowercase, ascii_uppercase

import converter

class Program:

    def __init__(self):
        self.charset = digits + ascii_lowercase + ascii_uppercase
        self.tempdir = tempfile.gettempdir()
        
        self.name = "ttycolor"
        self.description = "A program to generate and change tty colors in Linux"

        self.parser = argparse.ArgumentParser(prog=self.name, description=self.description, allow_abbrev=False)
        self.parser.add_argument("-o", "--output", type=str, metavar="OUTFILE", help="Output file name")
        self.parser.add_argument("-v", "--verbose", action="store_true", help="Prints details of output file")
        self.parser.add_argument("-s", "--setup", action="store_true", help="Sets up console colors")
        self.parser.add_argument("--version", action="version", version="%(prog)s 0.6 beta")

        self.parser.add_argument("filename", metavar="FILE", type=str, help="Input file in YAML format")
        
        self.args = self.parser.parse_args()

        self.filename = self.args.filename
        self.outfile = self.output_filename()

    def print_version(self):
        print(self.prog_version)
        sys.exit()

    def output_filename(self):
        output_file = self.args.output
        if not self.args.output:
            randfile = None
            randfile = ''.join([random.choice(self.charset) for x in range(16)])
            output_file = os.path.join(self.tempdir, randfile + ".svr")

        return output_file

    def main(self):

        if not os.path.isfile(self.filename):
            print("File not found.")
            self.parser.print_usage()
            sys.exit()

        fileops = converter.FileOps(self.filename, self.outfile)
        fileops.write_svr(self.args.verbose)

        if self.args.setup:
            print("Setting up terminal colors")
            subprocess.run(["setvtrgb", self.outfile])
            subprocess.run(["clear"])

        if not self.args.output:
            print("Writing to {}".format(self.outfile))

# Running the program when invoked.

if __name__ == "__main__":
    prog = Program()
    prog.main()

