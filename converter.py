# Copyright 2018-2020, Pratik Mullick
#
# This file is part of ttycolor.
#
# ttycolor is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# ttycolor is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Foobar.  If not, see <https://www.gnu.org/licenses/>.

import yaml

class Converter:

    def __init__(self, hex_dict):
        self.hex_dict = hex_dict
        self.int_dict = self.hexdict2intdict()
        self.color_lines_tuple = self.col_lines()

    def hex2int_tuple(self,col_hex_string):
        col_hex_string = (col_hex_string.lower()).strip("#")
        r_dec = int('0x' + col_hex_string[:2], 16)
        g_dec = int('0x' + col_hex_string[2:4], 16)
        b_dec = int('0x' + col_hex_string[-2:], 16)

        return r_dec,g_dec,b_dec

    def hexdict2intdict(self):
        int_dict = {}
        data_dict = self.hex_dict
        for code,shade in data_dict.items():
            int_dict[code] = self.hex2int_tuple(shade)

        return int_dict

    def col_lines(self):
        red_arr = []
        grn_arr = []
        blu_arr = []

        for code,shade in self.int_dict.items():
            red_arr.append(shade[0])
            grn_arr.append(shade[1])
            blu_arr.append(shade[2])

        return red_arr,grn_arr,blu_arr

class Operations(Converter):

    def __init__(self, input_yaml):
        self.input_yaml = input_yaml
        self.yaml_dict = self.read_yaml()
        self.colors = self.yaml_dict["color"]
        self.metadata = self.yaml_dict["metadata"]

        super().__init__(self.colors)
        self.line_tuple = self.col_lines()

    def read_yaml(self):
        with open(self.input_yaml,'r') as filestream:
            yaml_dict = yaml.safe_load(filestream.read())

        return yaml_dict

    def dict2svr(self):
        line_arr = []
        for line in self.line_tuple:
            current_line = ""
            for pos,item in enumerate(line):
                if pos == len(line) - 1:
                    current_line += str(item) + '\n'
                else:
                    current_line += str(item) + ','
            line_arr.append(current_line)

        return line_arr
