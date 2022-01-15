h, m = map(lambda x: int(x), input().split(':'))
def t2w(t):
    n2w = dict(zip([*list(range(1, 21)), 30, 40, 50],
        ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
        'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen',
        'eighteen', 'nineteen', 'twenty', 'thirty', 'forty', 'fifty']))
    if t < 20: return f"{n2w[t]}"
    return f"{n2w[t-t%10]} {n2w[t%10]}"
if m == 0: print(f"{t2w(h)} O'clock")
elif m == 15: print(f"quarter past {t2w(h)}")
elif m < 30: print(f"{t2w(m)} minute(s) past {t2w(h)}")
elif m == 30: print(f"half past {t2w(h)}")
elif m == 45: print(f"quarter to {t2w(h)}")
else: print(f"{t2w(m)} minute(s) to {t2w(h)}")
