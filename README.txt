Please see buildTools/BUILD.txt for build requirements and instructions.
Note especially the section BUILD SPECIFIC MODULES.

To build Analysis module, the command is:
MODULES=Analysis ./buildTools/build.sh

To build dbReports module, the command is:
MODULES=dbReports ./buildTools/build.sh


Tips:

- If you are building this software for the first time, it's suggested to use the Torrent Suite Virtual Machine as your Ubuntu 10.04 build environment.  That will reduce the chance of your being blocked by any environment dependencies.  Once you are familiar with the build process on Ubuntu 10.04, you'll have more confidence when getting creative with other operating systems.  You can find the virtual machine and helpful people on ionCommunity:

http://ioncommunity.lifetechnologies.com/welcome

- Note that the code that was formerly in the ion-alignment and tmap packages is now rolled into the ion-analysis packages

- For standalone Torrent Variant Caller, please see the below link for instructions.

http://updates.iontorrent.com/tvc_standalone/README.txt
