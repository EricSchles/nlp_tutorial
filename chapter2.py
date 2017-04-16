string = "“Dr. Watson, Mr. Sherlock Holmes”, said Stamford, introducing us."
# "http://www.londoninternational.ac.uk/sites/default/files/computing-samples/co3354_ch1-3.pdf" pg 18 (or pg 12)
# rule 1. spliting on spaces
tokenized = string.split(' ')
# rule 2. splitting on punctuation
new_tokenized = []
for elem in tokenized:
    if "," in elem:
        if len(new_tokenized) < 2:
            if elem.find(",") == 0:
                new_tokenized.append(",")
                new_tokenized.append(elem.replace(",",""))
            else:
                new_tokenized.append(elem.replace(",",""))
                new_tokenized.append(",")
        elif not elem.replace(",","") in [new_tokenized[-2],new_tokenized[-1]]:
            if elem.find(",") == 0:
                new_tokenized.append(",")
                new_tokenized.append(elem.replace(",",""))
            else:
                new_tokenized.append(elem.replace(",",""))
                new_tokenized.append(",")
    if "." in elem:
        if len(new_tokenized) < 2:
            if elem.find(".") == 0:
                new_tokenized.append(".")
                new_tokenized.append(elem.replace(".",""))
            else:
                new_tokenized.append(elem.replace(".",""))
                new_tokenized.append(".")
        elif not elem.replace(".","") in [new_tokenized[-2],new_tokenized[-1]]:
            if elem.find(".") == 0:
                new_tokenized.append(".")
                new_tokenized.append(elem.replace(".",""))
            else:
                new_tokenized.append(elem.replace(".",""))
                new_tokenized.append(".")
    if "“" in elem:
        if len(new_tokenized) < 2:
            if elem.find("“") == 0:
                new_tokenized.append("“")
                new_tokenized.append(elem.replace("“",""))
            else:
                new_tokenized.append(elem.replace("“",""))
                new_tokenized.append("“")
        elif not elem.replace("“","") in [new_tokenized[-2],new_tokenized[-1]]:
            if elem.find("“") == 0:
                new_tokenized.append("“")
                new_tokenized.append(elem.replace("“",""))
            else:
                new_tokenized.append(elem.replace("“",""))
                new_tokenized.append("“")
tokenized = new_tokenized[:]
print(tokenized)
