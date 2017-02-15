import cgi

print("Content-Type: text/html")
print("")

print("<pre>")
form = cgi.FieldStorage()

mode = form.getvalue("mode", default="")
print("mode=", mode)

print("--- all params ---")
for k in form.keys():
    print(k, "=", form.getvalue(k))
