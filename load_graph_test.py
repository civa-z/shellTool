# -*- coding: utf-8 -*-

"""RCNN Hand Gesture Recognizer"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import codecs
import rcnn_input_data
import tensorflow as tf
import numpy as np
from tensorflow.python.platform import gfile
n_classes = 29


# Load data set
te_data, te_seq_labels, te_clip_labels, te_seq_num, te_flag = rcnn_input_data.load_data('DataBase/t1_test_shuffled.data')
te_data_n = rcnn_input_data.data_normalized(te_data, -1, 1)
te_seq_labels_n = rcnn_input_data.generate_one_hot_sequence_labels(te_seq_labels, te_seq_num, n_classes)
with gfile.FastGFile("models/graph_vsd.pb",'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        tf.import_graph_def(graph_def, name='')

        with tf.Session() as session:
                for node in graph_def.node:
                        if -1 != node.name.find("nWeights"):
                                print (node.name)
                                session.run(session.graph.get_operation_by_name(node.name))


		te_size = te_data_n.shape[0]
		acc_test = []
		for begin in range(0, te_size, 1):
			end = begin + 1
			if end <= te_size:
				acc_test_temp = session.run(
                        		session.graph.get_tensor_by_name("accuracy_test:0"),
                        		feed_dict={session.graph.get_tensor_by_name("x_test:0"): te_data_n[begin:end, ...],
						session.graph.get_tensor_by_name("y_test:0"): te_seq_labels_n[begin:end, ...]})
				acc_test.append(acc_test_temp)
		test_acc_2 = np.mean(acc_test)
		print('testing acc=%5f' % (test_acc_2))

