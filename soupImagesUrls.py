import requests
import json
class UrlImages:

    imageURLs = []


    def __init__(self):
        states_abbr = json.load(open('us_states_abbr.json.txt'))
        state_list = list(states_abbr.values())
        self.state_list = state_list
        self.testURLs = ['https://www.usmint.gov/images/pressroom/{}_uncirc.jpg',
        'https://www.usmint.gov/images/pressroom/{}_uncirc.gif',
            'https://www.usmint.gov/images/pressroom/{}_unc.gif',
            'https://www.usmint.gov/images/pressroom/2008_{}_Thumb.jpg',
            'https://www.usmint.gov/images/pressroom/{}_Unc_Thumb.jpg',
            'https://www.usmint.gov/images/pressroom/2006_{}_unc_thumb.jpg',

            ]
        self.imageURLs.append([ 'ma', 'https://www.usmint.gov/images/pressroom/mass_unc.gif'])

    def getImageJson(self):

        for value in self.state_list:
            for url in self.testURLs:
                lVal = value.lower()
                address =url.format(lVal)
                ind = self.getIndex(address, lVal)
                if ind == -1:
                    break
        for item in self.imageURLs:
            print (item[0], item[1])
        print(len(self.imageURLs))
        return self.imageURLs
    def getIndex(self, url, val):
        response = requests.get(url)
        #print (response.text)
        ind = response.text.find('Page Not Found')
        if ind == -1:
            self.imageURLs.append([val, url])
        return ind
