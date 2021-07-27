url="https://www.emag.bg"

try:
    link=url.split("https://")
    link1=link[1].split("/")
    link2=link1[0]
    link3=link2.split("www.")
    real_link=link3[1]

except IndexError:
    link=url.split("https://")
    link1=link[1].split("/")
    real_link=link1[0]


print("link: ",link)
print("link1: ",link1)
print("link2: ",link2)
print("link3: ",link3)
print("real_link: ",real_link)