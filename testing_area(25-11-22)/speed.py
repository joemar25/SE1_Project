from Generator import Score
sc = Score()
text: list[str] = [
    'my name is Joemar',
    'and i lives in my houses',  # suppose 'live' and 'house'
    'i do a lots',
]

r = sc.rate(text, 6)  # 5.653333333333333
print(r)
