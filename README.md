# Common CLI
Common is a tool that helps you deal with multiple node_modules directories, avoiding the black hole of super heavy files in every project you create.

# How It Works
Common works like an npm shell. So, you use the commands `common npm install`, and `common npm uninstall` to install or not a lib taking into account your global environment.

# How to use    
As soon as you run the installation command, a node_modules folder will be found in your project, and you can import your project from that folder.
Example: 
By default, you run `npm install uuid`, and import with `require('uuid')`;
Now you run `common npm install uuid` and use `require(uuid')` normally;

This will provide support on your machine, but remember, before running your project on another machine, run common build, which will install the dependencies in your local directory and modify common, so that the libs are imported from the project and not from the machine.

# How to build
Install python requirements then run `pyinstaller common.py`
Put the file in your 'global path' and start using!
(all directory, not just the executable or file will be necessary) 