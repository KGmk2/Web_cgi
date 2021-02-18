#! /usr/bin/env python3
import html
import cgi
import cgitb
cgitb.enable()


html_body = """

print("Content-Type: text/html; charset=UTF-8")
print()

# フォームデータを取得する
form = cgi.FieldStorage()

# value = form.getlist("foo")
# print('<p>%s: %s</p>' % ("foo", value))


#全体の設定
FILE_LOG = "chat-log.txt"


# データの値を取得する
text = form.getvalue('text','')

print(html_body % (text))