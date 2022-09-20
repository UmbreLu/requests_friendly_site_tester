import sys
import re
import requests

# make sure script was runned with additional arg
assert len(sys.argv) == 2

if __name__ == '__main__':
    print('\nChecking http response code for url: "{}".'.format(sys.argv[1]))

    headers= {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0'}

    # try block for requesting url
    try:
        response = requests.get(sys.argv[1], headers=headers, timeout=5)
        print("...\nResponse status code was {}.".format(str(response.status_code)))
    except Exception as exception:
        print("...\nAn exception occurred when requesting given url:\n{}".format(exception))

    # in case of a positive response
    if response and response.status_code < 400:

        #try block for site name re extraction
        try: # replace is for removing "\" from names to keep paths relative
            re_match = re.search("""^(http:\/\/|https:\/\/)(.+)(\/)""", sys.argv[1])
            site_file_name = re_match[2].replace('/', '_')
        except Exception as exception:
            site_file_name = sys.argv[1][:25].replace('/', '_')
            print("ReGex error.\nError message: {}".format(exception))

        # file handling block for writing down successful response
        if response.text:
            with open(site_file_name + '.html', 'w') as fileh:
                fileh.write(response.text)
        else:
            with open(site_file_name, + '.txt', 'w') as fileh:
                fileh.write(response.content)

        # file creation print warning        
        print("...\nResponse code less than 400, response text saved to file {}.".format(site_file_name))

