import pafy

print("If you want to download audio or video from youtube, please put URL")
url = input("Enter URL: ")


def download(url):
    try:
        pafyobject = pafy.new(url)

        streams = pafyobject.streams
        availableStreams = {}
        count = 1

        for stream in streams:
            availableStreams[count] = stream
            print(f"{count}: {stream}")
            count += 1

        streamCount = int(input("Enter number: "))

        donwloadStream = streams[streamCount-1].download()

        print("Downloading successfully completed!")

    except:
        print("Error...Sorry, please check entered data")


download(url)
