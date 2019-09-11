import urllib.request
import webbrowser

def main():
    query = input("Enter the Name of person")
    query = query.replace(' ','_')
    query = query.capitalize()
    url = "https://en.wikipedia.org/wiki/"+query
    try:
        page = urllib.request.urlopen(url)
        webbrowser.open_new_tab(url)
        return url
    except:
        return "An error occured."


if __name__ == "__main__":
    main()