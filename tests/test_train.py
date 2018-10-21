# -*- coding: utf-8 -*-

from yolo.net.yolonet import Yolonet
from yolo.train import train_fn
from yolo.dataset.generator import BatchGenerator


def test_train(setup_tf_eager, setup_darknet_weights, setup_train_dirs):
    
    ann_fnames, image_root = setup_train_dirs
    darknet_weights = setup_darknet_weights

    # 1. create generator
    generator = BatchGenerator(ann_fnames, image_root,
                                 batch_size=2,
                                 labels_naming=["raccoon"],
                                 jitter=False)
    valid_generator = BatchGenerator(ann_fnames, image_root,
                                       batch_size=2,
                                       labels_naming=["raccoon"],
                                       jitter=False)
 
    # 2. create model
    model = Yolonet(n_classes=1)
    model.load_darknet_params(darknet_weights, True)
     
    # 3. training
    loss_history = train_fn(model,
                            generator,
                            valid_generator,
                            num_epoches=3)
    assert loss_history[0] > loss_history[-1]


import pytest
if __name__ == '__main__':
    pytest.main([__file__, "-v", "-s"])
 


