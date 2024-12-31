from string import Template
t = Template('$who likes $what')
print(t.substitute(who='tim', what='kung pao'))
print(t.substitute(who='kung pao', what='tim'))
