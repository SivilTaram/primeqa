### PrimeQA support trainining and inference of question answering models for table and text.

#### To train model on hybridqa dataset
```shell
python primeqa/mitqa/run_mitqa.py primeqa/mitqa/config/train_hybridqa.json
```

#### To train model on Open Domin ottqa dataset
```shell
python primeqa/mitqa/run_mitqa.py primeqa/mitqa/config/train_ottqa.json
```

#### To do inference on the pretrained model on hybridqa dataset
```shell
python primeqa/mitqa/run_mitqa.py primeqa/mitqa/config/inference_hybridqa.json
```

#### To do inference on the pretrained model on ottqa dataset
```shell
python primeqa/mitqa/run_mitqa.py primeqa/mitqa/config/inference_ottqa.json
```

#### Dataset and Performance
- Model trained on hybridqa dataset achieves: 65 % EM and 72 % F1 on dev set.
- Model trained on ottqa dataset achievs:  34% EM and 38% F1 on dev set using top 5 tables and top 5 links using link generator. We can get 36% EM and 41% F1 using top 50 tables and top 5 links.