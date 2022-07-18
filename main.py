import sys
sys.path.append('fast-coref/src')
from inference.model_inference import Inference

def replace():
    # For joint model
    inference_model = Inference("./", encoder_name="shtoshni/longformer_coreference_joint")

    doc = "My sister has a dog. She loves him."

    output = inference_model.perform_coreference(doc)

    main_list = list()
    for cluster in output["clusters"]:
      if len(cluster) > 1:
        each_cluster=list()
        for each in cluster:
            each_cluster.append(each[1])
        main_list.append(each_cluster)

        print(main_list)


    # Creating a dictionary from clusters, where Key will be the first word of each list of list and rest other items will be values.

    dict = {}

    for x in main_list:
        dict[x[0]] = x[1:]

    print(dict)

    # Now, we have to create a logic which uses dictionary to scan input doc and replace all values with a key of the dictionary.

    # Tried this but didnt got correct output. Check this logic:
    for word, replacement in dict.items():
        doc = doc.replace(str(word), str(replacement))
    print(doc)

replace()
