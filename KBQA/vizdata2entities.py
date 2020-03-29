import re
import os
import json
import time

from collections import Counter   #引入Counter

triple_template = "<http://kg.course/ai-food-time/{}> <http://kg.course/ai-foood-time/{}> \"{}\" ."

data_dir  = './data'
output_root = './external_dict'

avpair_file = 'vizdata_mimini_aglin.json'


# ----------------------------------
print('\n\n------Convert Avpair to Entities List------\n\n')

avpair_cnt  = 0
entities_num = 0
entities_list = []
avpair_list = list()
avpair_set  = set()
vizdata_dict = dict()
    
avpair_link_file_path = os.path.join(data_dir, avpair_file)


print(avpair_link_file_path)

if not os.path.exists(avpair_link_file_path):
    print("file {} not exit !".format(avpair_link_file_path))

with open(avpair_link_file_path) as f:
    content_all = json.load(f)

content = content_all["links"]

for link in content:

    if (link['relation'] == '属于'):
        subject = link['source'].split("-")[1]
    else:
        subject = link['source']
    object = link['target']
                
    if (subject not in entities_list):
        entities_list.append(subject)
        entities_num += 1
    if (object not in entities_list):
        entities_list.append(object)
        entities_num += 1


print("entities list is : {}".format(entities_list))
print("number of entities is {} ".format(entities_num))


# ----------------------------------
print('\n\n------Write Entities list into Files------\n\n')

entities_list = sorted(entities_list)

entities_file = os.path.join(output_root, 'entities_list.txt')
print('write path: {}'.format(entities_file))

with open(entities_file, 'w') as f:
    for item in entities_list:
        f.write(item + ' ai' +'\n')


print('\n\nFinish\n\n')

exit(-1)

