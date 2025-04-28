import pyshorteners
#get the link from the user
link=input("enter the link:")
#create a shortener object
shortener_link=pyshorteners.shortener()
#shortn the link using tinyURL
shortener_link=shortener_link.tinturl.short(link)
#print the shortend link
print("shortened link:",shortener_link)
