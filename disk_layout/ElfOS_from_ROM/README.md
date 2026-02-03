# Disk Layout during installation of ElfOS from the PE2 ROM

This section documents the approximate bytes on
the disk that were changed during various stages
of installation from the PE2 ROM to a 128MB CF Card.

## Procedure

The CF card was initially set to all zero.
Then each step was performed and the disk was
dumped using the Linux "dd" command. The
dumped files were named:

 - Step_0_CF_Zero.dat
 - Step_1_HD_Init.dat
 - Step_2_HD_Gen_FS.dat
 - Step_3_Sys.dat
 - Step_4_Binaries.dat

The Linux "cmp" command was used to
compare each of these image dumps to
the dump from the previous step. A
final comparison was also made between
the empty image and the final image.
The differences show the approximate areas 
of the disk written in each phase of the
installation. The numbers are in bytes.
The ranges are approximate, and there may
be sections that were written with the
same values and don't show as changed
at each step. But they give a general
idea of the disk usage. Here are the
commands used:

 - cmp -l Step_0_CF_Zero.dat Step_1_HD_Init.dat > CMP_From0to1.txt
 - cmp -l Step_1_HD_Init.dat Step_2_HD_Gen_FS.dat > CMP_From1to2.txt
 - cmp -l Step_2_HD_Gen_FS.dat Step_3_Sys.dat > CMP_From2to3.txt
 - cmp -l Step_3_Sys.dat Step_4_Binaries.dat > CMP_From3to4.txt
 - cmp -l Step_0_CF_Zero.dat Step_4_Binaries.dat > CMP_From0to4.txt

Finally, a small Python program ("Make_XPM_512cols.py") was used to
convert the results of each comparison into an XPM file:

 - python Make_XPM_512cols.py CMP_From0to1.txt > CMP_0_1.xpm
 - python Make_XPM_512cols.py CMP_From1to2.txt > CMP_1_2.xpm
 - python Make_XPM_512cols.py CMP_From2to3.txt > CMP_2_3.xpm
 - python Make_XPM_512cols.py CMP_From3to4.txt > CMP_3_4.xpm
 - python Make_XPM_512cols.py CMP_From0to4.txt > CMP_0_4.xpm

Each of these XPM files was then converted to PNG format for this page.

Each image below shows black for areas that have not been changed during
that step and yellow for areas that were changed during that step. The
total of all changes (from a blank disk to the final system) was
also used to generate the final cumulative image. For easier comparison,
all of the images were expanded to 240 rows of 512 bytes per row for a
total of 122880 bytes even though there were no bytes changed above
111577. These images are shown below (open separately and zoom as needed).

## Results

After step 1, only the first 266 bytes or so of the disk had been changed:

![Step 1 Drive Initialization](CMP_0_1.png?raw=true "Step 1 Drive Initialization")

The changes in step 2 are a bit more extensive. There were quite a few changes to the first 512 bytes of the disk. Additionally there were many changes to the bytes from 8705 through 8742 and from 72449 through 73728:

![Step 2 Filesystem Generation](CMP_1_2.png?raw=true "Step 2 Filesystem Generation")

The changes in step 3 were limited to the first 8704 bytes of the disk. But nearly every byte in that range was changed:

![Step 3 System Installation (sys)](CMP_2_3.png?raw=true "Step 3 System Installation (sys)")

The changes in step 4 were mostly above 73732 bytes into the disk. There were a few changes (possibly directory entries?) to the lower sections between 306 and 309 and again between 8743 and 8760:

![Step 4 Binaries Initialization](CMP_3_4.png?raw=true "Step 4 Binaries Initialization")

The cumulative changes over all steps can be shown by comparing the dump of the final installation image with the originally blank (all zeros) image. This is shown here:

![All changes due to installation](CMP_0_4.png?raw=true "All changes due to installation")

