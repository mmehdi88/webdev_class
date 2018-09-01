#Maintainer Qamber Mehdi
# Created on August 25, 2018

import requests, json

def search_businesses(search_term, search_location):

    api_key = "Huqj0Cnn6Pja3AoUYtzZHqlMMC9LiVHAYYtH9fQ7zDlk8QcT8U3ocXfV5rhZ8BxaDaUQnsKr3UWb9EbIK5moHqszFKzyeoBw8DDcA8hA4ULa2xR6_D8rPlpIi21_W3Yx"

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
