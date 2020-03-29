# encoding=utf-8

"""

@file: query_main.py

@time: 2020/03/29

"""
import jena_sparql_endpoint
import question2sparql


if __name__ == '__main__':
    # TODO 连接Fuseki服务器。
    fuseki = jena_sparql_endpoint.JenaFuseki()
    # TODO 初始化自然语言到SPARQL查询的模块，参数是外部词典列表。
    q2s = question2sparql.Question2Sparql(
        ['./external_dict/movie_title.txt', './external_dict/person_name.txt',
         './external_dict/vivre_zhpname.txt', './external_dict/onepiece_place_terminology.txt', './external_dict/entities_list.txt'])

    print("\n\n爱好美食的您好啊，小食在此为您提供问答服务")
    print("可以提问的菜品大类包括：1.红烧肉类，2.红烧排骨类，3.可乐鸡翅类，4.糖醋排骨类，5.水煮鱼类")
    print("                        6.红烧鱼类，7.凉拌黑木耳类，8.鱼香肉丝类，9.水煮肉片类，10.意大利面类")
    print("您可以提问的问题类型包括：制作方法，所有食材，主料，辅料，配料，特色，大类包含的菜品等")
    print("提示：您可以提问的问题例如：")
    print("如何制作水煮鱼？")
    print("水煮鱼的制作步骤是什么？")
    print("红烧肉类包含哪些菜？")
    print("麻辣水煮肉片的食材有哪些？")
    print("水煮肉片的主料是什么？")

    while True:
        print("\n\n")
        print('-' * 150)
        print("^_^请提问：")
        question = input()
        my_query = q2s.get_sparql(question)
        #print('最终的查询语句:\n{}'.format(my_query))
        print('\n小食：')
        if my_query is not None:
            result = fuseki.get_sparql_result(my_query)
            value = fuseki.get_sparql_result_value(result)

            # TODO 判断结果是否是布尔值，是布尔值则提问类型是"ASK"，回答“是”或者“不知道”。
            if isinstance(value, bool):
                if value is True:
                    print('Yes')
                else:
                    print('I don\'t know. :(')
            else:
                # TODO 查询结果为空，根据OWA，回答“不知道”
                if len(value) == 0:
                    if ('配料' in question):
                        print("这道菜好像不需要配料哦，试试问我其它问题哈。")
                    else:
                        print('这个我真是不知道，请再问个其它问题，例如：')
                        print('如何制作水煮鱼？')
                elif len(value) == 1:
                    print(value[0])
                else:
                    output = ''
                    for v in value:
                        output += v + u'、'
                    print(output[0:-1])

        else:
            # TODO 自然语言问题无法匹配到已有的正则模板上，回答“无法理解”
            print('这个问题我真是无法回答。')

        #print('\nquestion: {}'.format(question))
        print('=' * 150)
