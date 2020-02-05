def init_parmas(name, allow_domains='r18.com', *args):
    return [name, allow_domains, *args]

#  爬虫初始化参数
actress = init_parmas('actress', ['https://www.r18.com/videos/vod/movies/actress/letter=a/sort=popular/page=1/?lg=zh'])
category = init_parmas(
    'category',
    [
        'https://www.r18.com/videos/vod/movies/category/?lg=zh',
        'https://www.r18.com/videos/vod/amateur/category/?lg=zh',
        'https://www.r18.com/videos/vod/anime/category/?lg=zh'
    ]
)
product_v2 = init_parmas('product_v2', ['https://www.r18.com/videos/vod/movies/actress/letter=a/sort=popular/page=1/?lg=zh'])
product = init_parmas('product', ['https://www.r18.com/videos/vod/movies/list/pagesize=120/price=all/sort=new/type=all/page=1/?lg=zh'])


db = dict(host="192.168.0.101", port=27017, dbname='dmm')