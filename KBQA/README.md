# KBQA 智能问答系统
基于构建的中式菜谱知识图谱，设计知识库问答KBQA系统，根据提出的和菜品有关的问题，系统自动给出答案，对于无法给出回答的情况系统也能进行回应。
## 文件夹结构
+ /data：包含三元组数据aifoodtime_ntriples.nt
+ /external_dict：包含所有菜品和原料的实体列表entities_list.txt
+ query_main.py：KBQA主函数
+ jena_sparql_endpoint.py：启动jena_sparql服务
+ question2sparql.py：自然语言问题到SPARQL查询的转换
+ question_temp.py：自然语言到SPARQL的问题模板
+ vizdata2entities.py：从可视化存储数据到实体列表文件的转换
+ word_tagging.py：中文分词，使用的是jieba
