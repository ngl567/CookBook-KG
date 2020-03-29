import os
import json

vizdata_file = './vizdata_mimini.json'
aglin_file = './vizdata_mimini_aglin.json'

new_vizdata = {}

with open(vizdata_file) as f:
    vizdata = json.load(f)

new_links = []

links = vizdata['links']

for index, link in enumerate(links):
    if (link['relation'] == '属于'):
        new_links.append(link)
        continue
    target = link['target']
    target = target.strip('末')
    target = target.strip('段')
    target = target.strip('片')
    if ('五花肉' in target):
        target = '五花肉'
    if ('糖' in target):
        target = '糖'
    if ('蒜' in target):
        target = '蒜'
    if ('姜' in target):
        target = '姜'
    if ('葱' in target):
        target = '葱'
    if ('豆瓣酱' in target):
        target = '豆瓣酱'
    if ('排' in target):
        target = '排骨'
    if (target == '鸡中翅'):
        target = '鸡翅中'
    if ('草鱼肉' == target):
        target = '草鱼'
    if ('干' in target and '椒' in target):
        target = '干辣椒'
    if ('胡椒' in target):
        target = '胡椒'
    if ('花生' in target):
        target = '花生'
    if ('醋' in target):
        target = '醋'
    if ('木耳' in target):
        target = '木耳'
    if ('酱油' in target):
        target = '酱油'
    if ('黄瓜' in target):
        target = '黄瓜'
    if ('青辣椒' in target or '青椒' in target or '红辣椒' in target or '红椒' in target):
        target = '彩椒'
    if ('辣椒' in target):
        target = '辣椒'
    if ('里脊' in target):
        target = '里脊肉'
    if ('豆芽' in target):
        target = '豆芽'
    if ('意面' == target):
        target = '意大利面'
    
    link['target'] = target

    if (link not in new_links):
        new_links.append(link)

new_nodes = []

nodes = vizdata['nodes']

for index, node in enumerate(nodes):
    if (node['group'] != "2"):
        new_nodes.append(node)
        continue
    target = node['id']
    target = target.strip('末')
    target = target.strip('段')
    target = target.strip('片')
    if ('五花肉' in target):
        target = '五花肉'
    if ('糖' in target):
        target = '糖'
    if ('蒜' in target):
        target = '蒜'
    if ('姜' in target):
        target = '姜'
    if ('葱' in target):
        target = '葱'
    if ('豆瓣酱' in target):
        target = '豆瓣酱'
    if ('排' in target):
        target = '排骨'
    if (target == '鸡中翅'):
        target = '鸡翅中'
    if ('草鱼肉' == target):
        target = '草鱼'
    if ('干' in target and '椒' in target):
        target = '干辣椒'
    if ('胡椒' in target):
        target = '胡椒'
    if ('花生' in target):
        target = '花生'
    if ('醋' in target):
        target = '醋'
    if ('木耳' in target):
        target = '木耳'
    if ('酱油' in target):
        target = '酱油'
    if ('黄瓜' in target):
        target = '黄瓜'
    if ('青辣椒' in target or '青椒' in target or '红辣椒' in target or '红椒' in target):
        target = '彩椒'
    if ('辣椒' in target):
        target = '辣椒'
    if ('里脊' in target):
        target = '里脊肉'
    if ('豆芽' in target):
        target = '豆芽'
    if ('意面' == target):
        target = '意大利面'
    
    node['id'] = target

    if (node not in new_nodes):
        new_nodes.append(node)

new_vizdata['links'] = new_links
new_vizdata['nodes'] = new_nodes


with open(aglin_file, 'w', encoding='utf-8') as f:
    json.dump(new_vizdata, f, ensure_ascii=False, indent=4)
