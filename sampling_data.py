import random
import statistics
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go

def random_set_of_means(counter,data):
    dataset=[]

    for i in range(0,counter):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        dataset.append(value)

    mean=statistics.mean(dataset)
    return mean

def show_fig(data,mean):
    fig=ff.create_distplot([data],['Claps'],show_hist=False)
    fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.0035],mode='lines',name='Sample Mean'))
    fig.show()

def setup(data):
    mean_list=[]
    for i in range(0,100):
        set_of_means=random_set_of_means(30,data)
        mean_list.append(set_of_means)

    mean_of_means=statistics.mean(mean_list)

    show_fig(mean_list,mean_of_means)

    print('Sampling Mean is {}'.format(mean_of_means))

def main():
    df=pd.read_csv('medium_data.csv')
    data=df['claps'].tolist()
    population_mean=statistics.mean(data)

    setup(data)

    print('Population Mean is {}'.format(population_mean))

if __name__ == '__main__':
    main()
    