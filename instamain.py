import requests

BASE_URL = "https://api.instagram.com/v1/"
ACCESS_TOKEN = "2079733714.2775929.8b23c552a7a643e4b2446fa5a825f601"
def my_info():
    requested_url = (BASE_URL +"users/self/?access_token=%s") %(ACCESS_TOKEN)
    print "Requested url:%s" %(requested_url)
    access_my_info = requests.get(requested_url).json()
    #print access_my_info


    if access_my_info['meta']['code'] == 200:
        if len(access_my_info['data']):
            print "Username:%s" %(access_my_info['data']['username'])
            print "Full name of the user:%s" %(access_my_info['data']['full_name'])
            print "Followers:%d" %(access_my_info['data']['counts']['followed_by'])
            print "following:%d" %(access_my_info['data']['counts']['follows'])

        else:
            print "No user exists!!!"

    else:
        print "Status code other than 200!!!"
