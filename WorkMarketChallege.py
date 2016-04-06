#### Challenge 1 ####
## Name: Danielle Williams
## Date: 4/6/16

#Open file and remove newline characters
with open("C:\Users\Dani\Documents\Blogging\scriptassets\Resume_WilliamsDanielle.txt", "r") as resumeText:
	resumeData=resumeText.read().replace("\n", "")

#Use re.sub to remove white space characters 
import re
resumeData = re.sub('[\s+]', "", resumeData)

#Use for loop to remove non-alphanumeric characters
for ch in resumeData:
	if not(ch.isalpha()):
		resumeData = resumeData.replace(ch,"")
		
#Put text into lowercase		
resumeData = resumeData.lower()

#Remove special characters
resumeData = resumeData.replace('\xef', '')
resumeData = resumeData.replace('\xe2', '')

#Begin the frequency count
import collections
letterDict = collections.defaultdict(int)
for letter in resumeData:
	letterDict[letter] += 1

#Make the Bar chart
import plotly.plotly as py
import plotly.graph_objs as go

resumeBarX = [] #plot's x labels
resumeBarY = [] #plot's y values

for key in letterDict:
    resumeBarX.append(key)
    resumeBarY.append(letterDict[key])

resumeBar = go.Bar(
    resumeBarX, resumeBarY,
    marker=dict(color='rgb(158,202,225)',
                line=dict(color='rgb(8,48,107)',
                    width=1.5,)
                ),
            opacity=0.6)

data = [resumeBar]
layout = go.Layout(
    title='Resume Character Frequencies',
)
fig = go.Figure(data=data, layout=layout)

#Render plotly url
plot_url = py.plot(fig, filename='text-hover-bar')
