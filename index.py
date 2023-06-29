import ijson
import json
import csv
import itertools
import pandas as pd
import numpy as np

document_title = []
yes_no_answer = []
question_text = []
full_list = []
np.random.seed(2015)
df = pd.DataFrame(columns=['document_title', 'question_text'])
i = 0


data = ijson.parse(open('json_test.json', encoding="utf8"),multiple_values=True)
for prefix, event, value in data:
    # if (prefix, event) == ('annotations.item.yes_no_answer', 'string'):
    #     yes_no_answer.append(value)
    #     print(yes_no_answer)
    if (prefix, event) == ('document_title', 'string'):
        document_title.append(value)
        print(document_title)
        # df[i]['document_title'] = document_title
    if (prefix, event) == ('question_text', 'string'):
        question_text.append(value)
        print(question_text)
        # df[i]['question_text'][i] = question_text
        # full_list = document_title + question_text
        # print(df)l
    # print(full_list)
    # print(document_title) 
    # ab = itertools.chain(question_text, yes_no_answer, question_text)
    # print(list(ab))

