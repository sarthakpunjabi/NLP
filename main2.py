import spacy
nlp = spacy.load("en_core_web_sm")
sent = "Modi is a great leader.He has made India proud. Rahul Gandhi is naive . He is not fit to be prime minister."
doc=nlp(sent)

sub_toks = [tok for tok in doc if ((tok.dep_ == "nsubj") )]
print(sub_toks)

nc= [x for x in doc.noun_chunks]
print(nc)


l=[]
for i,token in enumerate(doc):
    if token.pos_ in ('PROPN','PRON'):
        l.append([token.text,i,token.pos_])
