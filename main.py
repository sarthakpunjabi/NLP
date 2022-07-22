import sys
import string
sys.path.append('fast-coref/src')
from inference.model_inference import Inference

def replace():
    # For joint model
    inference_model = Inference("./", encoder_name="shtoshni/longformer_coreference_joint")

    doc = '''Hey Shawn! Why are you mad at Steve. Steve is just stupid. Tom is the hero of cartoon. Tom is very cute.'''
    output = inference_model.perform_coreference(doc)

    main_list = list()
    for cluster in output["clusters"]:
      if len(cluster) > 1:
        each_cluster=list()
        for each in cluster:
            each_cluster.append(each[1])
        main_list.append(each_cluster)

    # Creating a dictionary from clusters, where Key will be the first word of each list of list and rest other items will be values.

    dict = {}

    for x in main_list:
        dict[x[0]] = x[1:]

    print(dict)

    words = doc.split(' ')
    current = ''

    for i, word in enumerate(words):
        if word[-1] == '.':
            word = word[:-1]

        if word in dict:
            current = word

        if current:
            if word in dict[current]:
                words[i] = current

    new_text = ' '.join(words)

    for person in dict:
        for pronoun in dict[person]:
            possibilities = [
                                pronoun + i
                                for i in string.punctuation
                            ] + [
                                pronoun + ' '
                            ]
            for p in possibilities:
                if p in new_text:
                    new_text = new_text.replace(pronoun, person)
                    break

    print("ORIGINAL:-", doc)
    print("CONVERTED:-")
    print(new_text)

replace()
