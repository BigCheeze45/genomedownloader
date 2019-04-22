# Genome Downloader
`genomedownload.py` is a python script that can be use to download anything but was written specifically to download 
genome data files from [EMBL-EBI](https://www.ebi.ac.uk/) FTP. It can take a single URL or a list of them (via file) to
download.

**Note:** This script is written for Python 3 or later. This was cowboyed together and has no tests. It 
is intended as both a starting point for future development and a useful example.

# Setup
The following instructions assume you're on a Unix like system with Python 3 or later.

1. Clone the repository: `git clone https://github.com/BigCheeze45/genomedownloader.git`
1. Create and activate a [Python virtual environment](https://tinyurl.com/y6gac52u)
	1. `python3 -m venv env`
	1. `source /path/to/env/bin/activate`
1. Installed the required packages: `pip install -r /path/to/genomedownloader/requirements.txt`

Once installation is complete the script is ready to use!

# Using genomedownload.py
`genomedownload.py` takes a single URL or a list of URLs of genome data files to download. You can also provide an output directory to place the downloaded data.

If using a file make sure each URL is on its own line.

```Bash
# Single URL no output folder specifed
python genomedownload.py --url ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR752/ERR752938/ERR752938_1.fastq.gz

# Single URL with output folder
python genomedownload.py --url ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR752/ERR752938/ERR752938_1.fastq.gz -o output/

# List of URLs with output folder
python genomedownload.py -f yeastDNAlinks.txt -o output/


# Complete usage guide
usage: genomedownload.py [-h] [--url URL | -f FILE] [-o OUTPUT]

Tool to download genome data files from EMBL-EBI

optional arguments:
  -h, --help            show this help message and exit
  --url URL             The absolute URL to the genome data you want
                        downloaded
  -f FILE, --file FILE  Path to a plain text file containing full URLs to the
                        genome data you want downloaded
  -o OUTPUT, --output OUTPUT
                        Location you want to store the downloaded genome data.
                        Default to current working directory
```

# To-dos
* Publish to PyPi for easier end uer installation
* Progress bar
* Refine logging control

# Contributing
Submit a pull request with your changes. Open an issue if you find any!
