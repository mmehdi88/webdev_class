#Maintainer Qamber Mehdi
# Created on August 25, 2018

import requests, json

def search_businesses(search_term, search_location):

    api_key = "z6Ki-01wJkXzlDyFkdLMp-uhkqdC5ZnMJmQH2QdXfpYU3Z15zh5HbVhCM24LNiQ1BVib8rwP5PLMPATJblk3tuAVjfw_rp5w37w1SiXSKR1YXp0mOmCY-ZCVvotWW3Yx"

    url = "https://api.yelp.com/v3/businesses/search"

    my_headers = {
        "Authorization": "Bearer %s" % api_key
    }

    my_params = {
        "term": search_term,
        "location": search_location,
        "limit": 3,
    }

    businesses_object = requests.get(url, headers=my_headers, params=my_params)

    businesses_dict = json.loads(businesses_object.text)

    businesses_list = businesses_dict['businesses']
    #
    list_of_businesses = []
    for each in businesses_list:
        list_of_businesses.append(each)
    return list_of_businesses
