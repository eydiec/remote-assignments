import pymysql.cursors

connection = pymysql.connect(host='localhost',
                             user = 'root',
                             password='a12345678',
                             database='assignment',
                             cursorclass=pymysql.cursors.DictCursor)


with connection.cursor() as cursor:
    for i in range(1,31):
        title =  f'Article {i} title'
        content = f'Article {i} content'
        author = f'author{i}'
        cursor.execute("INSERT INTO article (title, content, author) VALUES (%s, %s, %s)",
                       (title, content, author))
connection.commit()
connection.close()
