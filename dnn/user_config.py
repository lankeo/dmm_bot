def init_parmas(*args):
    return args

#  爬虫初始化参数
actress = init_parmas('actress', ['r18.com'], ['https://www.r18.com/videos/vod/movies/actress/letter=a/sort=popular/page=1/?lg=zh'])
category = init_parmas(
    'category',
    ['r18.com'],
    [
        'https://www.r18.com/videos/vod/movies/category/?lg=zh',
        'https://www.r18.com/videos/vod/amateur/category/?lg=zh',
        'https://www.r18.com/videos/vod/anime/category/?lg=zh'
    ]
)
product_v2 = init_parmas('product_v2', ['r18.com'], ['https://www.r18.com/videos/vod/movies/actress/letter=a/sort=popular/page=1/?lg=zh'])
product = init_parmas('product', ['r18.com'], ['https://www.r18.com/videos/vod/movies/list/pagesize=120/price=all/sort=new/type=all/page=1/?lg=zh'])


db = dict(host="192.168.44.20", port=27017, dbname='dmm')


# 遇到的一个坑是把allow_domains设置成了字符串，结果只能爬取一页