#!/bin/bash

# Loading finetuned without having to move it to ./data
loadfin=${1:-./data/LASTtrain.pth}
loadfin2=${2:-./data/LASTtraindev.pth}

# 50 Feats, Seed 126
cp ./data/hm_vgattr5050.tsv ./data/HM_img.tsv

python hm.py --seed 126 --model O \
--test dev_seen --lr 1e-5 --batchSize 8 --tr bert-large-uncased --epochs 5 --tsv \
--num_features 50 --loadfin $loadfin --exp O50

python hm.py --seed 126 --model O \
--test test_seen,test_unseen --lr 1e-5 --batchSize 8 --tr bert-large-uncased --epochs 5 --tsv \
--num_features 50 --loadfin $loadfin2 --exp O50