# QuickNote V2

Download the dependencies first. 
`pip install -r requirements.txt` 

Use venv if necessary

### Usage:  
*flags: -a, -o, -h, -p*

To specify path to dropbox use the following template:  
`python quicknote.py --path C:\Path\to\Dropbox\Directory`

`qn --help` for more information

## Aliasing

UNIX  
`alias qnote="python main.py"` if you consider using it only in your script directory.  
`alias qnote='cd /your/path/to/script/directory; python main.py'` if you want to use it from anywhere.  

WIN  
*=TODO=*

To permanently store your alias:  
- if you are using **zsh** then:  
`echo -e "\nalias qn='cd /path/to/your/script/directory; python main.py'" >> ~/.zshrc`  
- if you need to specify python3  
`echo -e "\nalias qn='cd /path/to/your/script/directory; python3 main.py'" >> ~/.zshrc`  


