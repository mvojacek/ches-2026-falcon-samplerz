import math
import random
import numpy as np
import json
import re
import struct

def float64_to_bitstring(f):
    packed = struct.pack('>d', f)
    unpacked = struct.unpack('>Q', packed)[0]
    bitstring = f'{unpacked:064b}'
    return bitstring

def float64_to_hex(f):
    packed = struct.pack('>d', f)
    unpacked = struct.unpack('>Q', packed)[0]
    hexstring = f'{unpacked:016X}'
    return hexstring

def bitstring_to_float64(bitstring):
    unpacked = int(bitstring, 2)
    packed = struct.pack('>Q', unpacked)
    f = struct.unpack('>d', packed)[0]
    return f

def hex_to_float64(h):
    unpacked = int(h, 16)
    packed = struct.pack('>Q', unpacked)
    f = struct.unpack('>d', packed)[0]
    return f

def parse_file(file_path):
    samplings = []

    with open(file_path, 'r') as file:
        lines = file.readlines()
        lines.reverse()
    atline = [0]

    def peek():
        return lines[-1]

    def pop():
        atline[0] += 1
        return lines.pop()

    def peekvar():
        return peek().split('=')[0].strip()

    def checkvar(var):
        if peekvar() != var:
            raise ValueError(f'At line [{atline[0]}] Expected variable {var}, got {peekvar()} on line {peek()}')

    def popval(name = None):
        if name:
            checkvar(name)
        return pop().split('=')[1].split('(')[0].strip()

    def popfloat(name = None):
        val = popval(name)
        # val is in C-style hexadecimal literal format and is 64bit
        return float.fromhex(val)

    def pophex(name = None):
        val = popval(name)
        return int(val, 16)

    def popdec(name = None):
        val = popval(name)
        return int(val)


    while lines:
        if peek().startswith('SamplerZ:'):
            pop()
            sampler = {}
            samplings.append(sampler)

            # SamplerZ:
            # mu      = +0x1.770D850D3A641p+4     (+2.344080071608755489e+01)
            # 1/sigma = +0x1.21A5FD8ACCC85p-1     (+5.657195312436590351e-01)
            # s       = 23
            # r       = +0x1.C361434E99040p-2     (+4.408007160875548891e-01)
            # ccs     = +0x1.780B796D7F861p-1     (+7.344625421681137967e-01)
            # BaseSampler: u = 0x2456D910A6D01FF847 -> z0 = 2
            # b       = 1  (from random byte: 0xE5)
            # z       = 3
            # x       = +0x1.780B796D7F861p-1     (+7.344625421681137967e-01)
            # BerExp:
            # x   = +0x1.C741A35494D08p-2     (+4.445863266348202281e-01)
            # ccs = +0x1.780B796D7F861p-1     (+7.344625421681137967e-01)
            # s   = 0
            # r   = +0x1.C741A35494D08p-2     (+4.445863266348202281e-01)
            # z   = 0x788A079F60384943 (8685763212432918851)
            # i = 56 -> w = 66  (from random byte: 0xBA)
            # ret: 0
            # BaseSampler: u = 0x9B3A192D03E66EF1B9 -> z0 = 1
            # b       = 0  (from random byte: 0x82)
            # z       = -1
            # x       = +0x1.780B796D7F861p-1     (+7.344625421681137967e-01)
            # BerExp:
            # x   = +0x1.7357F0AD0CC9Ep-3     (+1.813200762568145108e-01)
            # ccs = +0x1.780B796D7F861p-1     (+7.344625421681137967e-01)
            # s   = 0
            # r   = +0x1.7357F0AD0CC9Ep-3     (+1.813200762568145108e-01)
            # z   = 0x9CD7A37AC8721D2D (-7145062536055743187)
            # i = 56 -> w = 69  (from random byte: 0xE1)
            # ret: 0

            sampler['mu'] = popfloat("mu")
            sampler['1/sigma'] = popfloat("1/sigma")
            sampler['s'] = popdec("s")
            sampler['r'] = popfloat("r")
            sampler['ccs'] = popfloat("ccs")
            attempts = []
            sampler['attempts'] = attempts
            while peek().strip().startswith('BaseSampler:'):
                attempt = {}
                attempts.append(attempt)
                parts = pop().strip().split()
                attempt['u'] = int(parts[3], 16)
                attempt['z0'] = int(parts[-1])
                checkvar('b')
                parts = pop().strip().split()
                attempt['b'] = int(parts[2])
                attempt['b_fromrand'] = int(parts[-1].replace(')', ''), 16)
                attempt['z'] = popdec('z')
                attempt['x'] = popfloat('x')
                pop() # BerExp:
                berexp = {}
                attempt['berexp'] = berexp
                berexp['x'] = popfloat('x')
                berexp['ccs'] = popfloat('ccs')
                berexp['s'] = popdec('s')
                berexp['r'] = popfloat('r')
                berexp['z'] = pophex('z')
                ber_atts = []
                berexp['attempts'] = ber_atts
                while peekvar() == 'i':
                    ber_att = {}
                    ber_atts.append(ber_att)
                    parts = pop().strip().split()
                    ber_att['i'] = int(parts[2])
                    ber_att['w'] = int(parts[6])
                    ber_att['w_fromrand'] = int(parts[-1].replace(')', ''), 16)
                berexp['ret'] = pop().replace('ret:', '').strip() == '1'
            sampler['accepted'] = popdec('Accepted, ret')
        else:
            pop()

    return samplings

def load_samplerz_1024_json():
    with open("samplerz-1024.json", 'r') as file:
        samplerz = json.load(file)
    return samplerz

if __name__ == "__main__":
    file_path = 'test-vector-sampler-falcon1024.txt'
    samplerz = parse_file(file_path)
    print(len(samplerz))
    with open("samplerz-1024.json", 'w') as file:
        file.write(json.dumps(samplerz, indent=4))
