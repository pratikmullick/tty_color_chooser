import random
import os
import sys
import argparse
import tempfile

from string import digits, ascii_lowercase, ascii_uppercase

import converter

"""
DELETE THIS BLOCK!

Options:
    input_file [REQUIRED]: Has to be provided, otherwise help is invoked
    output_file (-o, --output) [OPTIONAL]: Output file
    list_colors (-l, --list) [OPTIONAL, exclusive]: Lists all inbuilt color files
    verbose (-V, --verbose) [OPTIONAL, not exclusive]: Shows all output to stdout
    version (-v, --version) [OPTIONAL, exclusive]: Shows program version
    help (-h, --help) [OPTIONAL
"""

class Program:

    def __init__(self):
        self.charset = digits + ascii_lowercase + ascii_uppercase

        self.name = "ttycolor"
        self.description = "A program to generate and change tty colors in Linux"
        self.tempdir = tempfile.gettempdir()

        self.parser = argparse.ArgumentParser(prog=self.name, description=self.description, allow_abbrev=False)
        self.parser.add_argument("-o", "--output", type=str, help="Output file name")
        self.parser.add_argument("-v", "--verbose", action="store_true", help="Prints details of output file")
        self.parser.add_argument("-s", "--setup", action="store_true", help="Sets up console colors")
        self.parser.add_argument("--version", action="version", version="%(prog)s 1.0")

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

        if not os.path.isfile(self.args.filename):
            print("File Not Found.")
            sys.exit()

        fileops = converter.FileOps(self.filename, self.outfile)
        
        fileops.write_svr(self.args.verbose)

# Running the program when invoked.

if __name__ == "__main__":
    prog = Program()
    prog.main()

