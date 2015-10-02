import urllib2
import json

mylist = ['Eva','Florence','Franklin','Gandhi','Ghandalf','Golda','Hitler','Julius','Mao','Mark','MLK','Napoleon','Obama','Snowden', 'Stalin','Thatcher','Trump','Turing', 'Manson']
mylistFull = ['Eva Peron','Florence Nightingale','Benjamin Franklin','Mahatma Gandhi','Ghandalf','Golda Meir','Aldolf Hitler','Gaius Julius Caesar','Mao Zedong','Mark Zuckerberg','Martin Luther King Jr','Napoleon Bonaparte','Barack Obama','Edward Snowden', 'Joseph Stalin','Margaret Thatcher','Donald Trump','Alan Turing', 'Marilyn Manson']
mycount = 0
for person in mylist:
    textfile = open("C://Users//KOU//Desktop//hitlervsMLK//" + person + ".txt", "r")
    myText = textfile.read()
    myText1 = myText.replace(" ", "+").replace(",", "%2C").replace("\n", "+")
    textfile.close()

    weather = urllib2.urlopen("https://api.idolondemand.com/1/api/sync/analyzesentiment/v1?text=" + myText1 + "&apikey=<MASKED>".replace("/n",""))

    wjson = weather.read()
    wjdata = json.loads(wjson)
    #print json.dumps(wjdata, sort_keys=True,indent=4, separators=(',', ': '))
    #print json.dumps(wjdata['negative'][1])

    myarray =[]
    myarray.append(person)
    myarray.append(json.dumps(wjdata['aggregate']['sentiment']).replace('\"', ""))
    myarray.append(json.dumps(wjdata['aggregate']['score']))
    for myscore in wjdata['negative']:
        myarray.append(  myscore['score'] )
    for myscore in wjdata['positive']:
        myarray.append(  myscore['score'] )
    #print person + "Array=" + str(myarray)

    print "if (sender == \"" + person + "\") {$('#msgid').html(\"<font size=6>" + json.dumps(wjdata['aggregate']).replace('\"',"'") + " " + mylistFull[mycount] +"</font><p>\"+\"" + myText.replace("\n", "<p>\" + \"") + "\")}"
    mycount = mycount + 1

