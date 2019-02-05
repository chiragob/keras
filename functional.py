from keras.utils import plot_model
from keras.models import Model
from keras.layers import Input
from keras.layers import Dense
visible = Input(shape=(3,3))
hidden = Dense(2)(visible)
hidden = Dense(2)(hidden)
model = Model(inputs=visible, outputs=hidden)


print(model.summary())
# plot graph
plot_model(model, to_file='multilayer_perceptron_graph.png')
