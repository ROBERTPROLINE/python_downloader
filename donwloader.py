import sys
import requests

def print_name():
 print('''
      *******       ********          ************************           ********************
       *******     ********          **************************          ********************
        *******   ********          *******              *******         *******        *****
         ******* *******            *******              *******         *******        *****
          *************             *******              *******         ********************
          *************             *******              *******         *******************
         ******* *******            *******              *******         *******    *******
        *******   *******           *******              *******         *******     ********
       *******     *******           **************************          *******       *******
      *******       *******           ************************           *******         *******

      Downloader by RobertSibanda : {pythonroot429913@elude.in}

 ''')


print_name()


def download(url, filename):
    with open(filename, 'wb') as f:
        response = requests.get(url, stream=True)
        total = response.headers.get('content-length')

        if total is None:
            f.write(response.content)
        else:
            downloaded = 0
            total = int(total)
            for data in response.iter_content(chunk_size=max(int(total/1000), 1024*1024)):
                downloaded += len(data)
                f.write(data)
                done = int(50*downloaded/total)
                sys.stdout.write('\r[{}{} {}MB {}]'.format('=' * done,'>',downloaded/1024/1024 ,'.' * (50-done)))
                sys.stdout.flush()
    sys.stdout.write('\nDone !!\n')


def main():     
    import optparse
    parser = optparse.OptionParser('usage %prog' + '-u <url> - <file>')
    parser.add_option('-u', dest = 'tgtUrl', help = 'enter the url')
    parser.add_option('-f', dest = 'tgtfile', help = 'enter the filename')

    (options,args) = parser.parse_args()
    if(options.tgtUrl == None) or (options.tgtfile == None):
         print(parser.usage)
    else:
       try:
          url = options.tgtUrl
          file = options.tgtfile

          download(url,file)
       except Exception as ex:
           print(ex) 


main()
