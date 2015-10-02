This is a simple experiment that examines the mentality of various historical figures.

![alt tag](https://raw.githubusercontent.com/ajkou/Historical-Speech-Experiment/master/pagelayout.png)

The HP OnDemand IDOL Sentiment Analysis API is a text analysis tool that examines various facets of text, including keywords with negative/positive connotations, context created by sentence structure, and grammatical modifiers. A recognition of sentiment is given a score between -1 to +1, a range indicating from very negative to a very positive expression of sentiment. These scorings are then aggregated by arithmetic mean to arrive at the overall sentiment.
SAcaller.py feeds text to the text analysis API and returns sentiment scores in json. The web applet in index.html uses Jquery to control the DOM and animate screen objects that display the results of the API calls. 

The initial goal of this application was to show whether villainous figures in history use hate speech (negative sentiment) to express their ideology. If this was true, figures like Hitler, Stalin, and Mao should have had the lowest and most negative sentiment scores. This was not always the case. For example, the overall sentiment of Aldolf Hitler's quotations is moderately positive due to his frequent use of boisterous and inspirational speech. On the other hand, many heroic historical figures (MLK, Mahatma Ghandi, Benjamin Franklin) made use of negative speech to change the world for the better. There is no direct correlation between negative sentiment and the morality of a public figure. 

Modern leaders and celebrities are keen to take advantage of the self-promotional effect of positive speech. Figures like Obama, Trump, and Zuckerberg are all overwhelmingly positive in their dialog, likely preferring to avoid expressing negative sentiment publically.

Edward Snowden is the only person in this collection who expresses truly neutral sentiment (sentiment score = 0) The reason for this is likely that Snowden's correspondence uses highly abstract expressions of sentiment.

Modern communications will ostensibly be subject to text analysis on a regular basis. Public figures can expect their communications to be algorithmically scrutinized not only in political discourse but also in the formation of their historical legacy hundreds of years from now.


