import argparse, sys
from urllib.error import HTTPError, URLError
import urllib.request
import urllib.parse

# haha classes go brrrrrrr

class Color:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    RESET = '\033[0m'

class Response:
    def __init__(self, response) -> None:
        self.status_code = response.code if hasattr(response, 'code') else None
        self.headers = response.headers if hasattr(response, 'headers') else None
        self.text = response.read().decode('utf-8') if hasattr(response, 'read') else str(response)

    def json(self):
        import json
        return json.loads(self.text)


class requests:
    def get(self, url, params=None, headers=None) -> Response:
        if params:
            url += "?" + urllib.parse.urlencode(params)

        req = urllib.request.Request(url, headers=headers or {})

        try:
            with urllib.request.urlopen(req) as response:
                return Response(response)
        except HTTPError as e:
            error_message = f"HTTPError {e.code}: {e.reason}"
            return Response(f"Error: {error_message}")
        except URLError as e:
            error_message = f"URLError: {e.reason}"
            return Response(f"Error: {error_message}")


class duckbuster:
    def __init__(self, parser: argparse.ArgumentParser) -> None:
        self.parser = parser
        self.setup_arguments()
        self.run()

    def setup_arguments(self) -> None:
        self.parser.add_argument("-w", "-WORDLIST",help="Wordlist Path")
        self.parser.add_argument("-u", "-URL", help="Target URL")
        self.parser.add_argument("-T", "-THRESHOLD", help="How fast we send out requests")


    def load_wordlist(self, wordlist):
        lines = []
        try:
            with open(wordlist, 'r') as file:
                lines = [line.strip() for line in file if line.strip() and not line.startswith('#')]
        except FileNotFoundError:
            print(f"{Color.RED}[!] An error occurred while opening the wordlist: {Color.RESET} File not found")
        except Exception as e:
            print(f"{Color.RED}[!] An error occurred while opening the wordlist: {Color.RESET} {e}")

        return lines


    def bruteforce(self, wordlist, target):
        if len(wordlist) == 0:
            print(f"{Color.RED} [!] An error occurred while discovering directories: {Color.RESET} Wordlist was somehow empty.")
            return

        print("[/] Starting...")
        for word in wordlist:
            try:
                url = f"{target}/{word}"
                response = requests().get(url)
                # print(f"Checking: {url}")
                sys.stdout.flush()  

                if response.status_code == 200:  
                    print(f"{Color.GREEN}[+] Found: {url}{Color.RESET}")
                else:
                    print(f"{Color.YELLOW}[-] Not Found: {url} (Status: {response.status_code}){Color.RESET}")
            except KeyboardInterrupt:
                print(f"\n{Color.RED}[!] User Interrupted process, exiting...{Color.RESET}")
                break
            except Exception as e:
                print(f"{Color.RED}[!] Error with request: {e}{Color.RESET}")
                continue

    def run(self):
        print(f""" {Color.BLUE}
    ·▄▄▄▄  ▄• ▄▌ ▄▄· ▄ •▄ ▄▄▄▄· ▄• ▄▌.▄▄ · ▄▄▄▄▄▄▄▄ .▄▄▄  
    ██▪ ██ █▪██▌▐█ ▌▪█▌▄▌▪▐█ ▀█▪█▪██▌▐█ ▀. •██  ▀▄.▀·▀▄ █·
    ▐█· ▐█▌█▌▐█▌██ ▄▄▐▀▀▄·▐█▀▀█▄█▌▐█▌▄▀▀▀█▄ ▐█.▪▐▀▀▪▄▐▀▀▄ 
    ██. ██ ▐█▄█▌▐███▌▐█.█▌██▄▪▐█▐█▄█▌▐█▄▪▐█ ▐█▌·▐█▄▄▌▐█•█▌
    ▀▀▀▀▀•  ▀▀▀ ·▀▀▀ ·▀  ▀·▀▀▀▀  ▀▀▀  ▀▀▀▀  ▀▀▀  ▀▀▀ .▀  ▀
                  Author: 1lordduck
              {Color.RESET}""")
        args = self.parser.parse_args()
        target = args.u 
        wordlist = args.w 

        words = self.load_wordlist(wordlist)

        self.bruteforce(words, target)


def main() -> None:
    parser = argparse.ArgumentParser(description="Lightweight brute-force directory discovery tool")
    duckbuster(parser)



if __name__ == "__main__":
    main()
