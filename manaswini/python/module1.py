import module
module.greetings("sean")
a=module.person["name"]
print(a)
print(module.person["age"])
import module as mod
a=mod.person["id"]
print(a)
#built in modules
import platform
x=platform.system()
print(x)
x=dir(platform)
print(x)
