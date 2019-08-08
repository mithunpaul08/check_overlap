import json
import argparse

def read_jsonl(filename):
    with open(filename) as f:
        for l in f:
            line=json.loads(l)
            pred=line["prediction"]
    return pred

def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--predictions_lex', metavar='DATASET', default='predictions_lex.jsonl')
    parser.add_argument('--predictions_delex', metavar='DATASET', default='predictions_delex.jsonl')
    args = parser.parse_args()
    return args

def calculate_overlap(predictions_lex,predictions_delex):
    counter=0
    for x,y in zip(predictions_lex,predictions_delex):
        if (int(x)== int(y)):
            counter=counter+1
    overlap_percentage=100* counter/len(predictions_delex)
    return overlap_percentage

args=create_parser()
predictions_lex=read_jsonl(args.predictions_lex)
predictions_delex=read_jsonl(args.predictions_delex)
overlap=calculate_overlap(predictions_lex,predictions_delex)
print(f" found {overlap} % overlap")