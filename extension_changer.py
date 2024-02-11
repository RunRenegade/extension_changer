#!/bin/python3

import sys
# sys.argv[1] will be the file we are working on
try:
	file = sys.argv[1]

except IndexError: 
	print('Please put a file and its extension as the only argument.')
	print('e.g. file1.php')
	sys.exit()
	
	
import subprocess
# This will allow us to run OS commands.


#########


# Arrays of alternate extensions that will be used for specific file types
# Taken from https://book.hacktricks.xyz/pentesting-web/file-upload

php_alts=[".php", ".php2", ".php3", ".php4", ".php5", ".php6", ".php7", ".phps", ".phps", ".pht", ".phtm", ".phtml", ".pgif", ".shtml", ".htaccess", ".phar", ".inc", ".hphp", ".ctp", ".module"]

php_alts_cap=[".pHp", ".pHp2", ".pHp3", ".pHp4", ".pHp5", ".pHp6", ".pHp7", ".pHps", ".pHps", ".pHt", ".pHtm", ".pHtml", ".pGif", ".shTml", ".hTaccess", ".pHar", ".iNc", ".hPhp", ".cTp", ".moDule"]

asp_alts=[".asp", ".aspx", ".config", ".ashx", ".asmx", ".aspq", ".axd", ".cshtm", ".cshtml", ".rem", ".soap", ".vbhtm", ".vbhtml", ".asa", ".cer", ".shtml"]

asp_alts_cap=[".aSp", ".aSpx", ".conFig", ".asHx", ".asMx", ".asPq", ".aXd", ".cShtm", ".cShtml", ".rEm", ".sOap", ".vBhtm", ".vBhtml", ".aSa", ".cEr", ".shTml"]

jsp_alts=[".jsp", ".jspx", ".jsw", ".jsv", ".jspf", ".wss", ".do", ".action"]

jsp_alts_cap=[".jSp", ".jsPx", ".jSw", ".jSv", ".jSpf", ".wSs", ".dO", ".acTion"]

cfm_alts=[".cfm", ".cfml", ".cfc", ".dbm"]

cfm_alts_cap=[".cFm", ".cfMl", ".cFc", ".dBm"]

flash_alts=[".swf", ".sWf"]

perl_alts=[".pl", ".cgi", ".Pl", ".cGi"]

erlang_alts=[".yaws", ".yaWs"]


# variable to track where the extension starts, so we know where to cut and replace etc.



extension_start = 0
try:
	if file != " ":
# Finds the index of the first ".", this will be used to figure out where to cut and replace from
		file_as_list=list(sys.argv[1])
		
		for i in file_as_list:
			if i == ".":
				extension_start = file_as_list.index(i)
				if extension_start != 0:
					break	
				 
			else:
				continue

except IndexError:
	print("You are missing a file as an input.")
	
except:
	print('Something went wrong...')
	sys.exit()

# Creates a variable of the file name without the extension on it.
file_no_extension = file[0:extension_start]

# Creates a variable which is just the extension, with the '.'. Will be looped through extensions arrays later,
file_extension_list = list(file[extension_start :])
file_extension = ''.join(file_extension_list)



# Checking if the file_extension variable is in any of our extension arrays at top of script. If so, use that array to create alternate files.

used_array = 'None'
used_array2 = 'None'
varying_capitals = 'n'

def array_check(extension):
	if extension in php_alts and varying_capitals != 'y':
		print('We will use the php list')
		print(' ')
		print( '-' * 50)
		return php_alts
		
	if extension in asp_alts and varying_capitals != 'y':
		print('We will use the asp list')
		print(' ')
		print( '-' * 50)
		return asp_alts		
		
		
	if extension in jsp_alts and varying_capitals != 'y':
		print('We will use the asp list')
		print(' ')
		print( '-' * 50)
		return jsp_alts
		
	if extension in cfm_alts and varying_capitals != 'y':
		print('We will use the cfm list')
		print(' ')
		print( '-' * 50)
		return cfm_alts
			
	if extension in flash_alts:
		print('We will use the flash list')
		print(' ')
		print( '-' * 50)
		return flash_alts
		
	if extension in perl_alts:
		print('We will use the perl list')
		print(' ')
		print( '-' * 50)
		return perl_alts

	if extension in erlang_alts:
		print('We will use the erland list')
		print(' ')
		print( '-' * 50)
		return erlang_alts
		
	# Still part of function, but below are for the varying capital arrays
		
	if extension in php_alts and varying_capitals == 'y':
		print('We will use the php list')
		print(' ')
		print( '-' * 50)
		return php_alts_cap
		
	if extension in asp_alts and varying_capitals == 'y':
		print('We will use the asp list')
		print(' ')
		print( '-' * 50)
		return asp_alts_cap	
		
		
	if extension in jsp_alts and varying_capitals == 'y':
		print('We will use the asp list')
		print(' ')
		print( '-' * 50)
		return jsp_alts_cap
		
	if extension in cfm_alts and varying_capitals == 'y':
		print('We will use the cfm list')
		print(' ')
		print( '-' * 50)
		return cfm_alts_cap
		
	
	else:
		return 'None'

# Checking the file extension we pulled from the file name

used_array = array_check(file_extension)


# Creates the folder for new files to go into
subprocess.run('mkdir' + ' ' + file_no_extension + '_collection', shell=True)  ###################################################### REACTIVE THIS CODE

if used_array == 'None':
	print('-' * 50)
	print('Cannot find matching extension used in your file.')
	print('')
	extension_inputted = input('Please confirm extension type to use, including full stop. eg; .php , .jsp etc: ')
	# Checking the extension the user gave us against the arrays
	used_array = array_check(extension_inputted)
	print(used_array)
	


# Creates the files with varying extensions



print(' ')
print(str(len(used_array)) + ' files are about to be created.')
create1 = input('Do you want to continue? y / n? ')

if create1 == 'y':
	for ext in used_array:
		new_file = file_no_extension + ext
		# Below code should use linux command 'cp' to copy existing file into new directory and rename it.
		subprocess.run('cp ' + file + ' ' + file_no_extension + '_collection/' + new_file, shell=True)
		


# See if user wants varying capitals in the extensions?

print('Would you like files with varying capitals in the extensions aswell? e.g. .pHp or .aSpx?')
varying_capitals = input('y / n? ')
used_array2 = array_check(file_extension)

if '.swf' in used_array2 or '.pl' in used_array2 or '.yaws' in used_array2 or varying_capitals == 'n':
	print('Files are created.')
	sys.exit()
	
else:
	print(str(len(used_array2)) + ' files are about to be created.')
	create2 = input('Do you want to continue? y / n? ')
	
	if create2 == 'y':
		print(used_array2)
		for ext in used_array2:
			new_file = file_no_extension + ext
			# Below code should use linux command 'cp' to copy existing file into new directory and rename it.
			subprocess.run('cp ' + file + ' ' + file_no_extension + '_collection/' + new_file, shell=True)
			
	
		
		
	else:
		print('Files not created.')
		print('End of Program')
		print('-' * 50)
		sys.exit()



