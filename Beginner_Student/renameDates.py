#! python3
# renameDates.py - renames file names with American MM-DD-YYYY or M-D-YYYY date formats -> Euro DD-MM-YYYY date format
# Requirements: must isolate target file for renaming with American dates in the file name
import shutil, os, re
# create regex that matches files with the American date format 'M-D-YYYY', 'MM-DD-YYYY' or variations there of
datePattern = re.compile(r"""^(.*?) # all text before the date
    ((0|1)?\d)-                     # one or two digits for the month
    ((0|1|2|3)?\d)-                 # one or two digits for the day
    ((19|20)\d\d)                   # four digits for the year
    (.*?)$                          # all text after the date
    """, re.VERBOSE)
# loop over the files in the working directory
for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)
# skip files without a date in the file name
    if mo == None:
        continue
# get and breakdown the different parts of a qualified filename
    beforePart = mo.group(1)
    monthPart  = mo.group(2)
    dayPart    = mo.group(4)
    yearPart   = mo.group(6)
    afterPart  = mo.group(8)
# form/realign 'layout' with cat style to the European-style filename
    euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart
# get the full, absolute file paths
    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)
# rename the files from American date style in the file name to the European date in the filename
print('Renaming "%s" to "%s"...' % (amerFilename, euroFilename))
# uncomment below after testing, as this will move, not copy
shutil.move(amerFilename, euroFilename)