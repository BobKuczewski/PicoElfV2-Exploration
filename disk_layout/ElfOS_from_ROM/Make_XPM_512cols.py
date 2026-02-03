import sys

def replaceall ( s, o, n ):
  while s.find(o) >= 0:
    s = s.replace ( o, n )
  return ( s )

# Check for a file name parameter
if len(sys.argv) != 2:
  print ( "Usage: python " + sys.argv[0] + " filename" )
  exit(1)

filename = sys.argv[1]

# Read the comparison file created with:
#   cmp -l f1.dat f2.dat > CMP_From0to4.txt
f = open ( filename )
d = f.read()

# Create an array of non-empty lines with single spaces between fields
lines = [ replaceall(l.strip(),'  ',' ') for l in d.split('\n') if len(l) > 0 ]

# Convert the lines into addresses where they differ
addresses = [ int(l.split(' ')[0]) for l in lines ]

# Find the largest address in the file
max_addr = max(addresses)

# Convert to number of rows and columns
num_cols = 512
num_rows = int((max_addr+num_cols-1)/num_cols)

# Create a minimum image height
if num_rows < 240: num_rows = 240

# Build the disk image
disk = []
for r in range(num_rows):
  disk.append ( num_cols * [0] )

# Fill the disk image with locations that have changed
for addr in addresses:
  r = int(addr / num_cols)
  c = int(addr % num_cols)
  disk[r][c] = 1

# Write the XPM header
print ( "/* XPM */" )
print ( "static char *dummy[]={" )
print ( "" )
print ( "\"" + str(num_cols) + " " + str(num_rows) + " 2 1\"," )  # num_cols num_rows num_colors chars_per_color
print ( "" )
print ( "\"0 c #000000\"" )
print ( "\"1 c #ffff88\"" )
print ( "" )

# Write the XPM data
for r in range(num_rows):
  s = str(disk[r]).replace(' ','').replace(',','').replace('[','').replace(']','')
  if r < (num_rows-1):
    print ( '"' + s + '",' )
  else:
    print ( '"' + s + '"};' )

# __import__('code').interact(local={k: v for ns in (globals(), locals()) for k, v in ns.items()})
