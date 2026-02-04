import sys

bytes_per_sec = 512

'''
Searching for mkdir and other command names around 0130
$ od -A x -a Step4_128K.dat | grep 0130
013000 nul nul nul dc4 bel  bs dc2   b   1 nul nul nul   d   i   r nul  <<-- dir
013010   Z   w   l   _   v   e   {  nl   L   m dc3   ^   m   E   ?   S
013020 nul nul nul nak nul   & dc2   b   1 nul nul nul   m   k   d   i  <<-- mkdir
013030   r nul   l   _   v   e   {  nl   L   m dc3   ^   m   E   ?   S
013040 nul nul nul syn nul   $ dc2   b   1 nul nul nul   c   h   d   i  <<-- chdir
013050   r nul   l   _   v   e   {  nl   L   m dc3   ^   m   E   ?   S
013060 nul nul nul etb soh   4 dc2   b   1 nul nul nul   i   n   s   t  <<-- install
013070   a   l   l nul   v   e   {  nl   L   m dc3   ^   m   E   ?   S
013080 nul nul nul can soh  us dc2   b   1 nul nul nul   c   r   c nul  <<-- crc
013090   a   l   l nul   v   e   {  nl   L   m dc3   ^   m   E   ?   S
0130a0 nul nul nul  em soh   ` dc2   b   1 nul nul nul   c   o   p   y  <<-- copy
0130b0 nul   l   l nul   v   e   {  nl   L   m dc3   ^   m   E   ?   S
0130c0 nul nul nul sub etx   v dc2   b   1 nul nul nul   l   b   r nul  <<-- lbr
0130d0 nul   l   l nul   v   e   {  nl   L   m dc3   ^   m   E   ?   S
0130e0 nul nul nul esc etx   Y dc2   b   1 nul nul nul   x   r nul nul  <<-- xr
0130f0 nul   l   l nul   v   e   {  nl   L   m dc3   ^   m   E   ?   S
'''
'''
[chr(l) for l in d.data[77830:77950]]
['\x12', 'b', '1', '\x00', '\x00', '\x00', 'd', 'i', 'r', '\x00', '\xda', 'w', '\xec', '\xdf', '\xf6', 'e', '\xfb', '\n', '\xcc', '\xed', '\x13', '\xde', '\xed', 'E', '\xbf', '\xd3', '\x00', '\x00', '\x00', '\x15', '\x00', '\xa6', '\x12', 'b', '1', '\x00', '\x00', '\x00', 'm', 'k', 'd', 'i', 'r', '\x00', '\xec', '\xdf', '\xf6', 'e', '\xfb', '\n', '\xcc', '\xed', '\x13', '\xde', '\xed', 'E', '\xbf', '\xd3', '\x00', '\x00', '\x00', '\x16', '\x00', '\xa4', '\x12', 'b', '1', '\x00', '\x00', '\x00', 'c', 'h', 'd', 'i', 'r', '\x00', '\xec', '\xdf', '\xf6', 'e', '\xfb', '\n', '\xcc', '\xed', '\x13', '\xde', '\xed', 'E', '\xbf', '\xd3', '\x00', '\x00', '\x00', '\x17', '\x01', '4', '\x12', 'b', '1', '\x00', '\x00', '\x00', 'i', 'n', 's', 't', 'a', 'l', 'l', '\x00', '\xf6', 'e', '\xfb', '\n', '\xcc', '\xed', '\x13', '\xde', '\xed', 'E']
'''
'''
[chr(l) for l in d.data[77830:77950]]
'12' 'b' '1' '00' '00' '00' 'd' 'i' 'r' '00'

'da'  'w' 'ec' 'df' 'f6'  'e' 'fb' '\n' 'cc' 'ed' '13' 'de' 'ed'  'E'
'bf' 'd3' '00' '00' '00' '15' '00' 'a6' '12'  'b'  '1' '00' '00' '00' 'm' 'k' 'd' 'i' 'r' '00'

'ec' 'df' 'f6'  'e' 'fb' '\n' 'cc' 'ed' '13' 'de' 'ed'  'E' 'bf' 'd3'
'00' '00' '00' '16' '00' 'a4' '12'  'b'  '1' '00' '00' '00'  'c' 'h' 'd' 'i' 'r' '00'

'ec' 'df' 'f6'  'e' 'fb' '\n' 'cc' 'ed' '13' 'de' 'ed'  'E' 'bf' 'd3'
'00' '00' '00' '17' '01'  '4' '12'  'b'  '1' '00' '00' '00'  'i' 'n' 's' 't' 'a' 'l' 'l' '00'

'f6' 'e' 'fb''\n' 'cc' 'ed' '13' 'de' 'ed' 'E'
'''


'''
DIRENT Entries:

[chr(l) for l in d.data[77830:77950]]
06:    '12'
07-08: 'b' '1'
09-0A: '00' '00'
0B:    '00'
0C-1F: 'dir\0' 'da'w'ec'df'f6'e'fb'\n'cc'ed'13'de'ed'E'bf'd3'  File name (up to 19 chars + \0)

00-03: '00' '00' '00' '15'                       lump number of first allocation unit for this file
04-05: '00' 'a6'                                 which byte in the final lump the end of file is located
06:    '12'                                      flags
07-08: 'b'  '1'                                  date that the file was last written
09-0A  '00' '00'                                 time that the file was last written
0B:    '00'                                      Supplementary flags.  None currenty defined.
0C-1F: 'mkdir\0' 'ec'df'f6'e'fb'\n'cc'ed'13'de'ed'E'bf'd3'  File name (up to 19 chars + \0)

00-03: '00' '00' '00' '16'                       lump number of first allocation unit for this file
04-05: '00' 'a4'                                 which byte in the final lump the end of file is located
06:    '12'                                      flags
07-08: 'b'  '1'                                  date that the file was last written
09-0A: '00' '00'                                 time that the file was last written
0B:    '00'                                      Supplementary flags.  None currenty defined.
0C-1F: 'chdir\0' 'ec'df'f6'e'fb'\n'cc'ed'13'de'ed'E'bf'd3'  File name (up to 19 chars + \0)

00-03: '00' '00' '00' '17'                       lump number of first allocation unit for this file
04-05: '01'  '4'                                 which byte in the final lump the end of file is located
06:    '12'                                      flags
07-08: 'b'  '1'                                  date that the file was last written
09-0A: '00' '00'                                 time that the file was last written
0B:    '00'                                      Supplementary flags.  None currenty defined.
0C-1F: 'install\0' 'f6'e'fb'\n'cc'ed'13'de'ed'E' File name (up to 19 chars + \0)
'''


class ElfDisk:
  def __init__ ( self, fname ):
    self.fname = fname
    f = open ( self.fname, 'rb' )
    self.data = bytearray(f.read())
    self.bkindex = 0
  def get_sector ( self, n ):
    addr = bytes_per_sec*n
    return ( self.data[addr:addr+bytes_per_sec] )
  def hex ( self, ba, sep='' ):
    return ( sep.join(['{:02x}'.format(x) for x in ba]) )
  def find ( self, s ):
    return ( self.data.find ( s ) )

  def dump_major_divisions ( self ):
    print ( "Major divisions" )
    print ( "  === System Data Sector ===" )
    # print ( "    Boot Loader:" + d.hex(d.get_sector(0)[0:256]) )
    print ( "    Boot Loader:" )
    sds = d.get_sector(0)
    for i in range(8):
      o = 32*i
      print ( "      " + d.hex(sds[o:o+32]) )
    print ( "    Disk Data:" )
    for i in range(8):
      o = 256 + (32*i)
      print ( "      " + d.hex(sds[o:o+32]) )
    total_drive_sectors = ((((((sds[0x100]<<8)+sds[0x101])<<8)+sds[0x102])<<8)+sds[0x103])
    total_drive_bytes = bytes_per_sec * total_drive_sectors
    print ( "    Disk contains " + str(total_drive_sectors) + " sectors and " + str(total_drive_bytes) + " bytes" )
    print ( "    Filesystem type = " + str(sds[0x104]) )
    if sds[0x104] != 1: print ( "!!!!!!!! Warning: Filesystem type is NOT 1 !!!!!!!!" )
    master_dir_sector = (sds[0x105]<<8) + sds[0x106]
    print ( "    Master Directory Sector is " + str(master_dir_sector) )
    sectors_per_lump = sds[0x10A]
    print ( "    Each lump contains " + str(sectors_per_lump) + " sectors" )
    bytes_per_lump = bytes_per_sec * sectors_per_lump
    print ( "    Each lump contains " + str(bytes_per_lump) + " bytes" )
    total_drive_lumps = total_drive_bytes / bytes_per_lump
    print ( "    Disk contains " + str(total_drive_lumps) + " lumps" )
    total_allocation_units = (sds[0x10B]<<8) + sds[0x10C]
    print ( "    Disk contains " + str(total_allocation_units) + " allocation units" )
    total_lat_sectors = total_drive_lumps / (bytes_per_sec/2)
    partial_lat_sectors = total_drive_lumps % (bytes_per_sec/2)
    if partial_lat_sectors > 0: total_lat_sectors += 1
    print ( "    Lump Allocation Table uses " + str(total_lat_sectors) + " sectors" )

    print ( "  === Kernel Image Block ===" )
    for i in range(16):
      kib = d.get_sector(1+i)
      print ( "    " + d.hex(kib[0:32]) + "..." )

    print ( "  === Lump Allocation Table ===" )
    for l in range(total_lat_sectors):
      lat = d.get_sector(1+16+l)
      for r in range(4):
        rdata = "    "
        for c in range(64):
          o = 2 * ((r*64) + c)
          v = (lat[o] << 8) + lat[o+1]
          if v == 0x0000:    # Unallocated
            rdata += '.'
          elif v == 0xFEFE:  # Allocated with EOF
            rdata += 'E'
          elif v == 0xFFFF:  # Nonexistant or non-allocatable
            rdata += '_'
          else:              # Next lump in the chain of a long file
            rdata += '^'
        print ( rdata )
      print ( "" )

    print ( "  === Common Data Area ===" )
    cda_sector = (total_drive_lumps / 256) + 17
    cda_offset = 2 * (total_drive_lumps % 256)

    for s in range(100):
      sec = d.get_sector(cda_sector+s)
      print ( "" )
      for i in range(16):
        o = 32*i
        print ( "    " + d.hex(sec[o:o+32]) )

# Check for a file name parameter
if len(sys.argv) != 2:
  print ( "Usage: python " + sys.argv[0] + " filename" )
  exit(1)
filename = sys.argv[1]

# Read the file into a disk object
d = ElfDisk ( filename )

d.dump_major_divisions()

d.find ( 'dir' )

# Read the binary image as one block
#f = open ( filename )
#d = f.read()
#f.close()


__import__('code').interact(local={k: v for ns in (globals(), locals()) for k, v in ns.items()})
