# Common CLI
Common is a tool that helps you deal with multiple node_modules directories, avoiding the black hole of super heavy files in every project you create.

# How It Works
Common works like an npm shell. So, you use the commands `common npm install`, `common npm uninstall` and `common npm install` to install or not a lib  into your global environment.

# How to use    
As soon as you run the installation command, a node_modules folder will be found in your project, and you can import your project from that folder.
Example: 
By default, you run `npm install uuid`, and import with `require('uuid')`;
Now you run `common npm install uuid` and use `require(uuid')` normally;

By default, common does not affect npm packages, so in a project you can use common or npm, this way a repository does not need to be modified to accept common, just as a client does not need to modify it to use npm

# How to build
Install python requirements then run `pyinstaller common.py`
Put the file in your 'global path' and start using!
(all directory, not just the executable or file will be necessary) 