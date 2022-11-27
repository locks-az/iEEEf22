import cv2 as cv
import pytesseract as pt
from PIL.Image import Image
from matplotlib import pyplot as plt
try:
    from googlesearch import search
except ImportError:
    print("The 'google' module should be installed by calling 'pip install google'")

from urllib.request import urlopen
from bs4 import BeautifulSoup
import sys

from pytesseract import pytesseract

img_path = input('Please enter the file path of your image: ')
img = cv.imread(img_path)

height = img.shape[0]
width = img.shape[1]

clickCount = 0

topLeftX = 0
topLeftY = 0
bottomRightX = 0
bottomRightY = 0

clicks = []


def click_event(event, x, y, flags, params):
    global img
    global clickCount

    if (clickCount == 2):
        clicks.sort()
        topLeftX = clicks[0][0]
        topLeftY = clicks[0][1]
        bottomRightX = clicks[1][0]
        bottomRightY = clicks[1][1]

        cv.line(img, (topLeftX, topLeftY), (bottomRightX, topLeftY), (0, 0, 0), 2)
        cv.line(img, (topLeftX, topLeftY), (topLeftX, bottomRightY), (0, 0, 0), 2)
        cv.line(img, (bottomRightX, bottomRightY), (topLeftX, bottomRightY), (0, 0, 0), 2)
        cv.line(img, (bottomRightX, bottomRightY), (bottomRightX, topLeftY), (0, 0, 0), 2)

        cv.imshow('image', img)
        cv.waitKey(5000)
        cv.destroyAllWindows()

    if event == cv.EVENT_LBUTTONDOWN:
        clickCount += 1
        img = cv.circle(img, (x, y), radius=7, color=(0, 0, 255), thickness=-1)
        cv.imshow('image', img)
        clicks.append([x, y])


cv.imshow('image', img)
cv.setMouseCallback('image', click_event)
cv.waitKey(0)

cropped_image = img[clicks[0][1]:clicks[1][1], clicks[0][0]:clicks[1][0]]

print(clicks)

cv.imshow("cropped", cropped_image)
cv.waitKey(5000)
cv.destroyAllWindows()


img_text = pt.image_to_string(cropped_image)
split_img = img_text.split('\n')

#print(img_text)
for string in split_img:
  if string == " " or string == "":
    continue
  else:
    print(string)
    break

def getPrimaryDomain(link):
    l = 0

    forwardslashCountFromLeft = 0
    while (forwardslashCountFromLeft != 2):
        if (link[l] == '/'):
            forwardslashCountFromLeft += 1
        l += 1

    r = l

    while (link[r] != '/'):
        r += 1

    primaryDomain = link[l: r]

    return primaryDomain


def getSearchResults(query):
    resultsGeneratorObject = search(query, tld="co.in", num=20, stop=20, pause=2)

    # from the 30 results stored in the generator object, we want to ensure that
    # the 5 results we display all are different website (ie. different domains name)
    # we do not want all 5 results to be sub-pages of only one website
    listOfFinalResults = []

    domainsEncountered = []

    for result in resultsGeneratorObject:

        # we have found the required number of results and have stored it
        # in the array listOfFinalResults
        if (len(listOfFinalResults) == 5):
            break

        resultPrimaryDomain = getPrimaryDomain(result)

        # this domain has not been encountered previously
        if (resultPrimaryDomain not in domainsEncountered):
            listOfFinalResults.append(result)
            domainsEncountered.append(resultPrimaryDomain)

    for searchResult in listOfFinalResults:
        print("Title: ", end=" ")
        try:
            soup = BeautifulSoup(urlopen(searchResult), features="html.parser")
            print(soup.title.get_text().strip())
            print("Link: " + searchResult.strip())
        except Exception:
            print(getPrimaryDomain(searchResult).strip())
            print("Link: " + searchResult.strip())

        print()

getSearchResults(string)