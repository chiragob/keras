from f keras.models import Sequential
from keras.layers import Dense
model = Sequential([Dense(2, input_dim=1), Dense(1)])
# from keras.models import Sequential
# from keras.layers import Dense
# from keras.utils import plot_model
# model = Sequential()
# model.add(Dense(2, input_dim=1))
# model.add(Dense(1))
# summarize layers
print(model.summary())
# plot graph
plot_model(model, to_file='multilayer_perceptron_graph.png')
