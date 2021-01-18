bri = set(['brazil', 'russia', 'india'])
print('india' in bri)
# True
print('usa' in bri)
# False
bric = bri.copy()
bric.add('china')
print(bric.issuperset(bri))
# True
bri.remove('russia')
print(bri & bric)  # 或者是 bri.intersection(bric)
# {'brazil', 'india'}
bri.add("russia")
bri.add("russia")

print(bri)
