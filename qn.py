#syslibs
import argparse
import subprocess
import datetime
import configparser
import pickle
import os

#3rd party
from fpdf import FPDF



def addNote(args, config):
    today = datetime.date.today().strftime("%B_%d%Y.pdf")
    datestamp = datetime.date.today().strftime("%d%B%Y")
    timestamp = datetime.datetime.now().strftime("%H:%M:%S")
    filepath = config['APPDATA']['path'] + "\\" + today
    
    try:
        data = pickle.load(open('./data.pickle', 'rb'))
        data[datestamp][timestamp] = args.add

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", "B", size = 12)
        pdf.cell(200, 10, txt = datetime.date.today().strftime("%d %B %Y"), ln = 1)

        for stamp in data[datestamp]:
            pdf.set_font("Arial", size = 10)
            pdf.cell(200, 10, txt = stamp, ln=2)
            pdf.cell(200, 10, txt = data[datestamp][stamp], ln=3)
        
        if args.verbose:
            print(f"{datetime.date.today().strftime('%d %B %Y')} updated >> \"{args.add}\"")

        pdf.output(filepath)   

        pickle.dump(data, open('data.pickle', 'wb')) 

    except:
        sample = {datestamp : { timestamp: args.add } }
        pickle.dump(sample, open('data.pickle', 'wb'))    
    

def openDate(args, config):
    filepath = config['APPDATA']['path'] + "\\" + datetime.date.today().strftime("%B_%d%Y.pdf")
    if args.verbose:
        print(f"Opening {filepath}")
    subprocess.Popen([filepath], shell=True)


def main():

    env = os.environ
    parser = argparse.ArgumentParser(description='Quicknote')
    parser.add_argument("-a", "--add", type=str,  help="Add note")
    parser.add_argument("-o", "--open", type=str, help="Open notes for the specified date. Ex: [ April_092022 ]")
    parser.add_argument("-p", "--path", type=str, help="Specify directory to save files")

    qvb = parser.add_mutually_exclusive_group()
    qvb.add_argument("-q", "--quiet", action="store_true", help="quiet mode")
    qvb.add_argument("-v", "--verbose", action="store_true", help="verbose mode")

    args = parser.parse_args()
    config = configparser.ConfigParser()
    config.read('config.ini')

    
    # --path flag
    # adding path to config.ini for the later use
    if args.path:
        config['APPDATA'] = {'path': args.path}
        if args.verbose:
            print(f"PATH={args.path}")
        with open('config.ini', 'w') as configfile:
            config.write(configfile)
        return

    if('path' not in config['APPDATA']):
        print("Indicate path using --path [PATH]\nUse -h, --help for help")
        return
    
    # -o flag
    # opens notes for specified date
    if args.open:
        openDate(args, config)
        return

    # -a [TXT] flag
    # adds notes for today.
    if args.add:
        addNote(args, config)
        return

    #if no flag specified open todays notes
    filepath = config['APPDATA']['path'] + "\\" + datetime.date.today().strftime("%B_%d%Y.pdf")
    subprocess.Popen(filepath, shell=True, env=env)
    

if __name__ == "__main__":
    main()
    
