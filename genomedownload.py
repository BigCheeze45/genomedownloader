import os
import argparse

import requests
from requests_ftp.ftp import FTPSession


parser = argparse.ArgumentParser(
  description='Tool to download genome data files from EMBL-EBI'
)

group = parser.add_mutually_exclusive_group()
group.add_argument('--url', help='The absolute URL to the genome data you want downloaded')
group.add_argument('-f', '--file',
                   help='Path to a plain text file containing full URLs to the genome data you want downloaded')

parser.add_argument('-o', '--output',
                    help='Location you want to store the downloaded genome data. Default to current working directory')

args = parser.parse_args()


def is_ftp(url):
  split_url = url.split('/')
  return 'ftp' in split_url[0]


def clean_link(link):
  """
  Remove trailing new lines from the provided link. This is helpful when working with files.
  """
  return link.rstrip()


def get_file_name(full_url):
  """
  Get file name or identifier from the given absolute URL.
  """
  split_url = clean_link(full_url).split('/')
  # Assuming the URL ends in a file name/identifier then the last item in the list can be use a file name
  return split_url[-1]


def write_file(**kwargs):
  """
  Write the given content to the specified file. The content and file names need to be specified as key word arguments. For example:

  write_file(
      file_name='awesomefile.txt',
      content='Write this to file'
  )
  """
  if kwargs['destination']:
    output_file = '{}/{}'.format(kwargs['destination'], kwargs['file_name'])
    with open(output_file, 'wb') as data_file:
      data_file.write(kwargs['content'])
      data_file.close()
  else:
    with open(kwargs['file_name'], 'wb') as data_file:
      data_file.write(kwargs['content'])
      data_file.close()


if args.url is None and args.file is None:
  print('Either a single URL or a list (via file) must be provided')
  parser.print_help()
  exit(1)

if args.output:
  print('Downloaded files will be placed in {}'.format(args.output))
else:
  print('Downloaded files will be placed in {}'.format(os.getcwd()))

if args.url:
  full_url = args.url
  print('Retrieving {}'.format(full_url))

  if is_ftp(full_url):
    ftp = FTPSession()
    resp = ftp.retr(full_url, timeout=30)
  else:
    resp = requests.get(url=full_url, timeout=30)

  if resp.ok:
    print('File successfully retrieved. Writting file...')
    write_file(
      file_name=get_file_name(full_url),
      content=resp.content,
      destination=args.output if args.output else None
    )
    print('{} written successfully'.format(get_file_name(full_url)))
  else:
    print('Encounter an error while retrieving {}'.format(full_url))
elif args.file:
  file_with_links = open(args.file)
  for line in file_with_links:
    link = clean_link(link=line)

    print('Retrieving {}'.format(link))
    if is_ftp(link):
      ftp = FTPSession()
      resp = ftp.retr(link, timeout=30)
    else:
      resp = requests.get(url=link, timeout=30)

    if resp.ok:
      print('File successfully retrieved. Writting file...')
      write_file(
        file_name=get_file_name(full_url=link),
        content=resp.content,
        destination=args.output if args.output else None
      )
      print('{} written successfully'.format(get_file_name(link)))
    else:
      print('Encounter an error while retrieving {}'.format(link))
