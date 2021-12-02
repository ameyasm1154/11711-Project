from sentence_transformers.cross_encoder import CrossEncoder
import pdb

eval_dataset_path = '/home/ubuntu/Karthik/11711-Project/two-step-reader/data/cross-encoder-data/cross-encoder-test-balanced-1000.csv'

class Preprocess():
    def __init__(self):
        model_path = "/home/ubuntu/Karthik/11711-Project/two-step-reader/output/cross-encoder-demo-2021-12-01_07-27-20"
        model = CrossEncoder(model_path)

    def preprocess(dataset):
        pair = []
        for example in dataset:    
            doc = example["context"]
            doc_sents = list(nlp(doc).sents)
            # doc_sents = [cleanSent(t.text) for t in doc_sents]
            question = example["question"]
            answer = cleanSent(example["answers"]["text"][0])

            context = [" ".join(doc_sents[i:i+3]) for i in range(0,len(doc_sents)-3)]
            
            pair = [[c, question] for c in context]
            self.model.predict(pair)
            pdb.set_trace()
            # pair += [[c, question, 0] for c in c_neg]


                    # current_json = {
                    #         'answers': {
                    #             'answer_start': [start_id], 
                    #             'text': [answer_span]
                    #         },
                    #         'context': context, 
                    #         'domain': "public_forum", 
                    #         'id': _id , 
                    #         'question': question, 
                    #         'title': title 
                    #     }


# with open(eval_dataset_path, 'rt', encoding='utf8') as fIn:
    # reader = csv.DictReader(fIn, delimiter='\t', quoting=csv.QUOTE_NONE, fieldnames=['sentence1', 'sentence2', 'score'])
    # for row in reader:
        # score = float(row['score'])  # Normalize score to range 0 ... 1
        # eval_samples.append(InputExample(texts=[row['sentence1'], row['sentence2']], label=score))

# model = CrossEncoder(model_save_path)

# corr_evaluator = CECorrelationEvaluator.from_input_examples(test_samples, name='correlation-test')
# corr_evaluator(model)

# binary_evaluator = CEBinaryAccuracyEvaluator.from_input_examples(test_samples, name='binary-test')
# binary_evaluator(model)