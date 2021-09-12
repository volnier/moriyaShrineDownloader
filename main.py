import json
import sys
import requests


def main():
    downloads = {}
    num = 0
    with open('downloads.json') as file:
        oui = json.load(file)
        for i in oui:
            downloads[i] = oui[i]

    for i in downloads:
        num += 1
        print(str(num) + ". " + i)

    dwnld = input("Which game do you want to download (Enter the name, not the number): ")

    for l in downloads:
        if dwnld.lower() == l.lower():
            with open(dwnld.lower() + ".zip", "wb") as k:
                print("Downloading %s" % dwnld.lower())
                response = requests.get(downloads[l], stream=True)
                length = response.headers.get('content-length')
                if length is None:  # no length header
                    k.write(response.content)
                else:
                    pp = 0
                    length = int(length)
                    for data in response.iter_content(chunk_size=4096):
                        pp += len(data)
                        k.write(data)
                        done = int(50 * pp / length)
                        sys.stdout.write("\r[%s%s]" % ('X' * done, ' ' * (50 - done)))
                        sys.stdout.flush()


if __name__ == "__main__":
    main()
