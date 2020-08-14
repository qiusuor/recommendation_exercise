import os

#处理MovieLens数据源rating.csv文件的函数，从而得到二分图。这里设置评分大于4.5分就是喜欢这部电影，也就是二分图中的线，才算用户对电影的“行为”。
def get_graph_from_data(input_file):
    """
    :param input_file: user to rating of item file
    :return:
        a dict:{userA:{itemb:1,itemc:1},itemb:{userA:1}}
        以user为key，value是user行为过的item
        以item为key，value是item被行为过的user
    """

    if not os.path.exists(input_file):
        print('文件不存在')
        return {}

    graph = {}
    linenum = 0
    with open(input_file, encoding='utf-8') as fp:
        for line in fp:
            if linenum == 0:
                linenum += 1
                continue
            item = line.strip().split(',')
            if len(item) < 3:
                continue
            userid, itemid, rating = item[0], "item_" + item[1], item[2]
            if float(rating) < 4.5:
                continue
            if userid not in graph:
                graph[userid] = {}
            graph[userid][itemid] = 1
            if itemid not in graph:
                graph[itemid] = {}
            graph[itemid][userid] = 1
        return graph


def get_item_info(input_file):
    '''
    get item info:[title,genre]
    :param input_file:
    :return: a dict:{itemid:[title,genre]}
    '''
    if not os.path.exists(input_file):
        return {}
    linenum = 0
    item_info = {}
    with open(input_file, encoding='UTF-8') as fp:
        for line in fp:
            if linenum == 0:
                linenum += 1
                continue
            item = line.strip().split(',')
            if len(item) < 3:
                continue
            elif len(item) == 3:
                itemid, title, genre = item[0], item[1], item[2]
            elif len(item) > 3:
                itemid = item[0]
                genre = item[2]
                title = ','.join(item[1:-1])
            item_info[itemid] = [title, genre]
    return item_info

