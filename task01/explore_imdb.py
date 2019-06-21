import tensorflow as tf
from tensorflow import keras

imdb = keras.datasets.imdb
(train_data, train_labels), (test_data, test_labels) = imdb.load_data(path="/home/niko/github/nlp_learn/task01/imdb/imdb.npz",
                                                                      num_words=10000)
                                                                      
print(train_data[0:5]) #打印前10条数据集
print('\n\n\n\n')
print(train_labels[0:5]) #打印前10条标签
