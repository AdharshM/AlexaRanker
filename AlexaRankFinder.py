import seolib
n=raw_input("Enter full URL of the Website(with http or https): ")     #user enters URL here
alexanumber=seolib.get_alexa(n)                     #seolib.get_alexa() returns real time alexa rank of the website
print "The Alexa Ranking of "+ n +" is " + str(alexanumber)                                   #displays the alexa ranking of the website
k=raw_input("Press Enter to close the console..... ")
#This is Not a GUI based program and all the data is displayed at real time, please enter the url withh http://#Alexa Rank is that of website, whatever be the body of the URL unless, the domain remains same
