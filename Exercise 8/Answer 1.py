from json import load
from jmespath import search
with open("employee.json","r") as file1 :
    object=load(file1)


print(search("[?gender==`female`].fullName",object))

print(search("[?company==`MAPNA` && gender==`male` ].fullName",object))

print(search("[?company==`Iran Khodro Co.`].[fullName,email]",object))

print(search("sort_by(@, &salary) | reverse(@)[:3].[*]",object))
