lst = [
    "fnd17_oxlcxspebq",
    "fnd17_shsoutbs",
    "fnd17_oxlcxspebq",
    "fnd28_value_05191q",
    "fnd17_oxlcxspebq",
    "fnd28_value_05192q",
    "fnd17_oxlcxspebq",
    "fnd28_value_05301q",
    "fnd17_oxlcxspebq",
    "fnd28_value_05302",
    "fnd17_pehigh",
    "fnd17_pelow",
    "fnd17_priceavg150day",
    "fnd17_priceavg200day",
    "fnd17_priceavg150day",
    "fnd17_priceavg50day",
    "fnd17_priceavg200day",
    "fnd17_priceavg50day",
    "fnd17_pxedra",
    "fnd17_tbea",
    "fnd17_pxedra",
    "fnd28_newa3_value_18191a",
    "fnd17_pxedra",
    "fnd28_newa3_value_18198a",
    "fnd17_pxedra",
    "fnd28_value_02300a",
    "fnd17_pxedra",
    "fnd28_value_05302",
    "fnd17_pxedra",
    "mdl175_ebitda",
    "fnd17_pxedra",
    "mdl175_pain",
]
s = set()
s.add(1)
s.add(1)
s.add(2)

for i in lst:
    s.add(i)

for i in s:
    for j in s:
        if i != j:
            print(f"ts_regression(ts_zscore({i}, 500), ts_zscore({j}, 500), 500)")
