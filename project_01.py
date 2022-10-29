def station_list():
    my_station=['야탑', '모란', '이매', '선릉', '한티', '왕십리']
    for station in my_station:
        print(station)


station_list()

def station_point():
    my_station=['야탑', '모란', '이매', '선릉', '한티', '왕십리']
    for station in my_station:
        if station == '선릉':
            print(station)

station_point()

class article:
    id = '',
    title = '',
    author = '',
    content = ''

first_article = article()
first_article.id = '1'
first_article.title = '제목'
first_article.author = '김철수'
first_article.content = '글 내용입니다.'
print(first_article.id)
print(first_article.title)
print(first_article.author)
print(first_article.content)
