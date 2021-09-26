import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd

df=pd.read_csv("studentMarks.csv")
data=df["Math_score"].tolist()

mean=statistics.mean(data)
standarddeviation=statistics.stdev(data)
print(mean)
print(standarddeviation)

def randomsetofmean(counter):
    dataset=[]
    for i in range(0,counter):
        randomindex=random.randint(0,len(data)-1)
        value=data[randomindex]
        dataset.append(value)
    mean=statistics.mean(dataset)
    return mean
meanlist=[]
for i in range(0,1000):
    setofmean=randomsetofmean(100)
    meanlist.append(setofmean)
standarddeviation1=statistics.stdev(meanlist)
mean1=statistics.mean(meanlist)
print(mean1)
print(standarddeviation1)
fig=ff.create_distplot([meanlist],['Math Score'],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.20],mode="lines",name="mean"))
#fig.show()

firstSDstart,firstSDend = mean-standarddeviation,mean+standarddeviation
secondSDstart, secondSDEnd = mean-(2*standarddeviation), mean+(2*standarddeviation)
thirdSDstart, thirdSdEnd = mean-(3*standarddeviation), mean+(3*standarddeviation)
#listofdatawithen1SD=[result for result in diceResult if result>firstSDstart and result<firstSDend]

fig=ff.create_distplot([meanlist],["result"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean],y=[0,0.17],mode="lines",name="mean"))
fig.add_trace(go.Scatter(x=[firstSDstart,firstSDstart],y=[0,0.17],mode="lines",name="SD1 Start"))
fig.add_trace(go.Scatter(x=[firstSDend,firstSDend],y=[0,0.17],mode="lines",name="SD1 End"))
fig.add_trace(go.Scatter(x=[secondSDstart,secondSDstart], y=[0,0.17], mode="lines", name="SD2 Start"))
fig.add_trace(go.Scatter(x=[secondSDEnd,secondSDEnd], y=[0,0.17], mode="lines", name="SD2 End"))
fig.add_trace(go.Scatter(x=[thirdSDstart,thirdSDstart], y=[0,0.17], mode="lines", name="SD3 Start"))
fig.add_trace(go.Scatter(x=[thirdSdEnd, thirdSdEnd], y = [0,0.17], mode="lines",name="3SD End"))
#fig.show()
df=pd.read_csv("data1.csv")
data=df["Math_score"].tolist()
meanofsample1=statistics.mean(data)
fig=ff.create_distplot([meanlist],["result"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean],y=[0,0.17],mode="lines",name="mean"))
fig.add_trace(go.Scatter(x=[meanofsample1,meanofsample1],y=[0,0.17],mode="lines",name="SD1 Start"))
fig.add_trace(go.Scatter(x=[firstSDend,firstSDend],y=[0,0.17],mode="lines",name="SD1 End"))
#fig.show()

df=pd.read_csv("data2.csv")
data=df["Math_score"].tolist()
meanofsample2=statistics.mean(data)
fig=ff.create_distplot([meanlist],["result"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean],y=[0,0.17],mode="lines",name="mean"))
fig.add_trace(go.Scatter(x=[meanofsample2,meanofsample2],y=[0,0.17],mode="lines",name="SD1 Start"))
fig.add_trace(go.Scatter(x=[firstSDend,firstSDend],y=[0,0.17],mode="lines",name="SD1 End"))
fig.add_trace(go.Scatter(x=[secondSDEnd,secondSDEnd], y=[0,0.17], mode="lines", name="SD2 End"))
#fig.show()

df=pd.read_csv("data3.csv")
data=df["Math_score"].tolist()
meanofsample3=statistics.mean(data)
fig=ff.create_distplot([meanlist],["result"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean],y=[0,0.17],mode="lines",name="mean"))
fig.add_trace(go.Scatter(x=[meanofsample3,meanofsample3],y=[0,0.17],mode="lines",name="SD1 Start"))
fig.add_trace(go.Scatter(x=[firstSDend,firstSDend],y=[0,0.17],mode="lines",name="SD1 End"))
fig.add_trace(go.Scatter(x=[thirdSdEnd, thirdSdEnd], y = [0,0.17], mode="lines",name="3SD End"))
#fig.show()

zscore=(meanofsample3-mean)/standarddeviation
print(zscore)