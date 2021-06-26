import pandas as pd
import random 
import statistics as sts
import plotly.figure_factory as ff
import plotly.graph_objects as go

df = pd.read_csv('./hwFiles/data/medium_data.csv')
data = df["reading_time"].tolist()

population_mean = sts.mean(data)
population_stdev = sts.stdev(data)

print("Population Mean: " + str(population_mean))
print("Population Standard Deviation: " + str(population_stdev))

dist_figure = ff.create_distplot([data], ["Population Data"], show_hist=False)

def get_sample_data_mean(counter, data):
    sample_data_points = []

    for i in range(0, counter):
        random_index = random.randint(0, len(data) - 1)
        random_data_point = data[random_index]

        sample_data_points.append(random_data_point)

    sample_mean = sts.mean(sample_data_points)

    return sample_mean

def show_mean_figures(mean_list):
    sample_mean = sts.mean(mean_list)
    sample_stdev = sts.stdev(mean_list)
    z_score = (sample_mean - population_mean) / sample_stdev
    print ("Sampling Distribution Mean: " + str(sample_mean))
    print ("Sampling Distribution Standard Deviation: " + str(sample_stdev))
    print("Z Score: " + str(z_score))

    first_start_stdev, first_end_stdev = sample_mean - sample_stdev, sample_mean + sample_stdev
    second_start_stdev, second_end_stdev = sample_mean - (2*sample_stdev), sample_mean + (2*sample_stdev)
    final_start_stdev, final_end_stdev = sample_mean - (3*sample_stdev), sample_mean + (3*sample_stdev)

    sample_figure = ff.create_distplot([mean_list], ["Results"], show_hist=False)

    sample_figure.add_trace(go.Scatter(x=[sample_mean, sample_mean], y=[0, 1], mode="lines", name="Mean of Sampling Distribution"))

    sample_figure.add_trace(go.Scatter(x=[sample_mean, sample_mean], y=[0, 0.2], mode="lines", name="Mean of All Samples"))

    sample_figure.add_trace(go.Scatter(x=[first_start_stdev, first_start_stdev], y=[0, 0.17], mode="lines", name="First Start St_Dev"))
    sample_figure.add_trace(go.Scatter(x=[first_end_stdev, first_end_stdev], y=[0, 0.17], mode="lines", name="First End St_Dev"))

    sample_figure.add_trace(go.Scatter(x=[second_start_stdev, second_start_stdev], y=[0, 0.17], mode="lines", name="Second Start St_Dev"))
    sample_figure.add_trace(go.Scatter(x=[second_end_stdev, second_end_stdev], y=[0, 0.17], mode="lines", name="Second End St_Dev"))

    sample_figure.add_trace(go.Scatter(x=[final_start_stdev, final_start_stdev], y=[0, 0.17], mode="lines", name="Final Start St_Dev"))
    sample_figure.add_trace(go.Scatter(x=[final_end_stdev, final_end_stdev], y=[0, 0.17], mode="lines", name="Final End St_Dev"))

    sample_figure.show()

def get_mean_of_all_samples(counter):
    final_samples_mean_result = []

    for i in range(0, counter):
        sample_mean = get_sample_data_mean(30, data)
        final_samples_mean_result.append(sample_mean)
    
    show_mean_figures(final_samples_mean_result)

dist_figure.show()
get_mean_of_all_samples(100)