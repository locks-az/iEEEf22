{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "at8IFFIXj52I",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "88837df3-ecdd-458d-c02e-b401f1ab8363"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Looking in indexes: https://pypi.org/simple, https://us-python.pkg.dev/colab-wheels/public/simple/\n",
            "Requirement already satisfied: beautifulsoup4 in /usr/local/lib/python3.7/dist-packages (4.6.3)\n"
          ]
        }
      ],
      "source": [
        "pip install beautifulsoup4"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "pip install google"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "hS0iRHFDNSyF",
        "outputId": "332099df-3d60-4bc2-d08f-4eb2c101117e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Looking in indexes: https://pypi.org/simple, https://us-python.pkg.dev/colab-wheels/public/simple/\n",
            "Requirement already satisfied: google in /usr/local/lib/python3.7/dist-packages (2.0.3)\n",
            "Requirement already satisfied: beautifulsoup4 in /usr/local/lib/python3.7/dist-packages (from google) (4.6.3)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "try:\n",
        "\tfrom googlesearch import search\n",
        "except ImportError:\n",
        "\tprint(\"The 'google' module should be installed by calling 'pip install google'\")\n",
        " \n",
        "from urllib.request import urlopen\n",
        "from bs4 import BeautifulSoup"
      ],
      "metadata": {
        "id": "XxekyZZtNZPr"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "\"\"\"\n",
        "https://www.freecodecamp.org/news/how-to-substring-a-string-in-python/\n",
        "\n",
        "If the domain is something like this, we want to retrieve the part\n",
        "www.freecodecamp.org\n",
        "\"\"\"\n",
        "def getPrimaryDomain(link):\n",
        "    \n",
        "    l = 0\n",
        "\n",
        "    forwardslashCountFromLeft = 0\n",
        "    while (forwardslashCountFromLeft != 2):\n",
        "        if (link[l] == '/'):\n",
        "            forwardslashCountFromLeft += 1\n",
        "        l += 1\n",
        "\n",
        "    r = l\n",
        "\n",
        "    while (link[r] != '/'):\n",
        "        r += 1\n",
        "\n",
        "    primaryDomain = link[l : r]\n",
        "\n",
        "    return primaryDomain"
      ],
      "metadata": {
        "id": "6QtB7xXLRpzD"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def getSearchResults(query):\n",
        "    resultsGeneratorObject = search(query, tld = \"co.in\", num = 20, stop = 20, pause = 2)\n",
        "\n",
        "    # from the 30 results stored in the generator object, we want to ensure that\n",
        "    # the 5 results we display all are different website (ie. different domains name)\n",
        "    # we do not want all 5 results to be sub-pages of only one website\n",
        "    listOfFinalResults = []\n",
        "\n",
        "    domainsEncountered = []\n",
        "\n",
        "    for result in resultsGeneratorObject:\n",
        "        \n",
        "        # we have found the required number of results and have stored it\n",
        "        # in the array listOfFinalResults\n",
        "        if (len(listOfFinalResults) == 5):\n",
        "            break\n",
        "\n",
        "        resultPrimaryDomain = getPrimaryDomain(result)\n",
        "\n",
        "        # this domain has not been encountered previously\n",
        "        if (resultPrimaryDomain not in domainsEncountered):\n",
        "            listOfFinalResults.append(result)\n",
        "            domainsEncountered.append(resultPrimaryDomain)\n",
        "\n",
        "    for searchResult in listOfFinalResults:\n",
        "        print(\"Title: \", end = \" \")\n",
        "        try:\n",
        "            soup = BeautifulSoup(urlopen(searchResult))\n",
        "            print(soup.title.get_text().strip())\n",
        "            print(\"Link: \" + searchResult.strip())\n",
        "        except Exception:\n",
        "            print(getPrimaryDomain(searchResult).strip())\n",
        "            print(\"Link: \" + searchResult.strip())\n",
        "\n",
        "        print()"
      ],
      "metadata": {
        "id": "-I9_Sy3WOEhE"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Some Applications:\n",
        "\n",
        "\n",
        "\n",
        "1.   Supplemental Material related to slide title\n",
        "2.   Question posed in recording\n",
        "\n"
      ],
      "metadata": {
        "id": "ufF5CUeUXvsN"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "getSearchResults(\"Demand Curve\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "FmytmZMGZ-97",
        "outputId": "03bf5b13-f8f9-4d3b-e572-dd00ddcb3d2d"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Title:  www.investopedia.com\n",
            "Link: https://www.investopedia.com/terms/d/demand-curve.asp\n",
            "\n",
            "Title:  Demand Curve | Level up your marketing\n",
            "Link: https://www.demandcurve.com/\n",
            "\n",
            "Title:  Demand curve - Wikipedia\n",
            "Link: https://en.wikipedia.org/wiki/Demand_curve\n",
            "\n",
            "Title:  The Demand Curve - YouTube\n",
            "Link: https://www.youtube.com/watch?v=kUPm2tMCbGE\n",
            "\n",
            "Title:  www.britannica.com\n",
            "Link: https://www.britannica.com/topic/demand-curve\n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "getSearchResults(\"How do fish breathe?\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "zP3FLMcoZFAt",
        "outputId": "400838f8-78da-41b2-cc4d-ef4a5b0acf74"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Title:  How do fish breathe? - DNR News Releases\n",
            "Link: https://www.iowadnr.gov/About-DNR/DNR-News-Releases/ArticleID/1454/How-do-fish-breathe\n",
            "\n",
            "Title:  www.dkfindout.com\n",
            "Link: https://www.dkfindout.com/us/animals-and-nature/fish/how-fish-breathe/\n",
            "\n",
            "Title:  How do fish breathe underwater? | Live Science\n",
            "Link: https://www.livescience.com/how-do-fish-breathe\n",
            "\n",
            "Title:  How Do Fish Breathe? The Science Behind Gills - NESS Journal\n",
            "Link: https://nessf.org/how-do-fish-breathe-the-science-behind-gills/\n",
            "\n",
            "Title:  How Do Fish Breathe Underwater? | Wonderopolis\n",
            "Link: https://www.wonderopolis.org/wonder/how-do-fish-breathe-underwater\n",
            "\n"
          ]
        }
      ]
    }
  ]
}
