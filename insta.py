import requests
import urllib


# declaring global variables i.e. BASE_URL and ACCESS_TOKEN(generated)
BASE_URL = "https://api.instagram.com/v1/"
ACCESS_TOKEN = "2079733714.2775929.8b23c552a7a643e4b2446fa5a825f601"


def my_info():
    request_url = (BASE_URL +"users/self/?access_token=%s") %(ACCESS_TOKEN)
    print "Get url:%s" %(request_url)
    access_my_info = requests.get(request_url).json()


    if access_my_info['meta']['code'] == 200:
        if len(access_my_info['data']):
            print "Username: %s" %(access_my_info['data']['username'])
            print "Full name of the user: %s " %(access_my_info['data']['full_name'])
            print "Followers:  %d" %(access_my_info['data']['counts']['followed_by'])
            print "following: %d" %(access_my_info['data']['counts']['follows'])

        else:
            print "No user exists!!!"

    else:
        print "Status code other than 200!!!"



def get_user_id(username):
    request_url = (BASE_URL +"users/search?q=%s&access_token=%s") %(username, ACCESS_TOKEN)
    print "Requested url is:%s" %(request_url)
    user_info = requests.get(request_url).json()


    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            return user_info['data'][0]['id']

        else:
            return None

    else:
        print "status code other than 200 received"
        exit()



def get_user_info(username):
    user_id = get_user_id(username)
    if user_id == None:
        print "No user exists"


    request_url = (BASE_URL + "users/%s?access_token=%s") % (user_id, ACCESS_TOKEN)
    print "Requested url is:%s" % (request_url)
    user_info = requests.get(request_url).json()


    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            print "Username: %s" % (user_info['data']['username'])
            print "Full name of the user: %s " % (user_info['data']['full_name'])
            print "Followers:  %d" % (user_info['data']['counts']['followed_by'])
            print "following: %d" % (user_info['data']['counts']['follows'])


        else:
            print "No user exists!!!"

    else:
        print "Status code other than 200!!!"



def get_own_media():
    request_url = (BASE_URL +"users/self/media/recent/?access_token=%s") %(ACCESS_TOKEN)
    print "Requested url is:%s" %(request_url)
    own_media = requests.get(request_url).json()


    if own_media['meta']['code'] == 200:
        if len(own_media['data']):
            return own_media['data'][0]['id']

        else:
            print "No media exists"
    else:
        print "status code other than 200 returned."



def get_user_media(username):

    user_id = get_user_id(username)
    if user_id == None:
        print "User does not exist"

    else:

        request_url = (BASE_URL +"users/%s/media/recent/?access_token=%s") %(user_id, ACCESS_TOKEN)
        print "Requested url is:%s" %(request_url)
        user_media = requests.get(request_url).json()


        if user_media['meta']['code'] == 200:
            if len(user_media['data']):
                return user_media['data'][0]['id']


            else:
                print "No media exists"
        else:
            print "status code other than 200 returned."



def download_own_media():
    request_url = (BASE_URL +"users/self/media/recent/?access_token=%s") %(ACCESS_TOKEN)
    print "Requested url is:%s" %(request_url)
    own_media = requests.get(request_url).json()


    if own_media['meta']['code'] == 200:
        if len(own_media['data']):
            image_name =  own_media['data'][0]['id'] +".jpeg"
            image_url = own_media['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url,image_name)
            print "Your image has been downloaded"

        else:
            print "Post doesn't exist"
    else:
        print "status code other than 200 returned."

def download_user_media(username):

    user_id = get_user_id(username)
    if user_id == None:
        print "User does not exist"

    else:
        request_url = (BASE_URL +"users/%s/media/recent/?access_token=%s") %(user_id,ACCESS_TOKEN)
        print "Requested url is:%s" %(request_url)
        user_media = requests.get(request_url).json()


        if user_media['meta']['code'] == 200:
            if len(user_media['data']):
                image_name =  user_media['data'][0]['id'] +".jpeg"
                image_url = user_media['data'][0]['images']['standard_resolution']['url']
                urllib.urlretrieve(image_url,image_name)
                print "User's image has been downloaded"

            else:
                print "Post doesn't exist"
        else:
            print "status code other than 200 returned."

def get_media_id(username):
    user_id = get_user_id(username)
    if user_id == None:
        print "User does not exist"

    else:

        request_url = (BASE_URL + "users/%s/media/recent/?access_token=%s") % (user_id, ACCESS_TOKEN)
        print "Requested url is:%s" % (request_url)
        user_media = requests.get(request_url).json()


        if user_media['meta']['code'] == 200:
            if len(user_media['data']):
                return user_media['data'][0]['id']


            else:
                print "No media exists"
        else:
            print "status code other than 200 returned."


def set_like(username):
    post_id = get_media_id(username)
    request_url = (BASE_URL +"media/%s/likes") %(post_id)
    payload = {'access_token' : ACCESS_TOKEN}
    print "Post url is : %s" %(request_url)
    post_like = requests.post(request_url, payload).json()

    if post_like['meta']['code'] == 200:
        print "Photo has been liked by you!!!"

    else:
        print "Try Again"



def post_comment(username):
    media_id = get_media_id(username)
    request_url = (BASE_URL +"media/%s/comments") %(media_id)
    payload = { 'access_token' : ACCESS_TOKEN,
                'text' :"nice"}
    print "Post url is : %s" %(request_url)
    set_comment = requests.post(request_url, payload).json()

    if set_comment['meta']['code'] == 200:
        print "Your comment has been successfully posted!!"

    else:
        print "Try again!!"


def media_found(latitude,longitude):

    if latitude == "" or longitude == "":
        print "enter valid latitude and longitute"
        exit()

    else:
        request_url=BASE_URL+'media/search?lat=%s&lng=%s&access_token=%s' %(latitude,longitude,ACCESS_TOKEN)
        media_info = requests.get(request_url).json()
        if media_info['meta']['code']==200:
            length = len(media_info['data'])
            if len(media_info['data']):
                i=0
                k=0
                length=len(media_info['data'])
                while(length):
                    if media_info['data'][i]['type']=="image" and ( media_info['data'][i]['caption']['text']=="#flood" or media_info['data'][i]['caption']['text']=="#earthquake" ):
                        image_name = media_info['data'][i]['id'] + '.jpeg'
                        image_url = media_info['data'][i]['images']['standard_resolution']['url']
                        urllib.urlretrieve(image_url, image_name)
                        print 'Your image has been downloaded! and image id is %s' % (media_info['data'][i]['id'])
                        k=k+1
                    else:
                        print "No image of calamity is found"
                    length=length-1
                    i=i+1
                print "total no image found=%s" %(k)

            else:
                print "No media found in the searched location"

        else:
            print 'Status code other than 200 received!'


print "Welcome to the bot"

def start_bot():
    while(True):

        print "Enter your choice?"

        choice = raw_input("Enter your choice here \n1)Access your own information. \n2)Retrieve sanbox user's ID. \n3)Access"
                           " user's information. \n4)Getting own media. \n5)Getting user's media. \n6)Download own media. "
                           "\n7)Download user's media. \n8)Getting Media ID. \n9)Posting a like on user's media. \n10)Posting "
                           "comment on user's media. \n11)Finding disaster images in certain area. ")

        if choice == "1":
            my_info()


        elif choice == "2":
            username = raw_input("enter the username")
            get_user_id(username)


        elif choice == "3":
            username = raw_input("enter the username")
            get_user_info(username)


        elif choice == "4":
            get_own_media()


        elif choice == "5":
            username = raw_input("enter the username")
            get_user_media(username)


        elif choice == "6":
            download_own_media()


        elif choice == "7":
            username = raw_input("enter the username of the user")
            download_user_media(username)


        elif choice == "8":
            username = raw_input("enter the username of the user")
            get_media_id(username)


        elif choice == "9":
            username = raw_input("enter the username of the user")
            set_like(username)


        elif choice == "10":
            username = raw_input("enter the username of the user")
            post_comment(username)


        elif choice == "11":
            latitude = raw_input("Enter the latitude")
            longitude = raw_input("Enter the longitude")
            media_found(latitude, longitude)
            exit()
            #latitude: 28.4504 & longitude: 77.2837

        else :
            print "no such choice"

start_bot()