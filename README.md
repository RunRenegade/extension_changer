# extension_changer
A small tool to automatically edit the extensions of files to assist in pentesting by bypassing file upload restrictions. 

The tool is written using Python

### Use

To use the tool simple run the script with the name of the file (and its extension) as the first and only argument. You will have to be in the same location as the file.

`./extension_changer reverse_shell.php`

The tool will then create a new folder within the location you have used the tool in and create a number of variations within the folder.

The script will also ask you if you wish to vary the capitilisation within your extensions, such as .pHp, in an attempt to bypass upload restrictions.

### Use cases

Currently the script works for the following file types;

- php
- asp
- jsp
- Coldfusion
- flash
- perl
- Erland

Variable extensions taken from https://book.hacktricks.xyz/pentesting-web/file-upload 
