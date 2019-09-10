price = [
  [10, 20, 15], 
  [8, 14, 22], 
  [30, 25, 20], 
  [44, 16, 28], 
  [15, 25, 35],
  [9, 29, 19]
]

country = ['A', 'B', 'C', 'D', 'E', 'F']
firm = ['X', 'Y', 'Z']

select = firm.copy()

print('FROM_COUNTRY TO_COUNTRY SHIPMENT_COMPANY CARGO_AMOUNT')

for c1 in range(6):
    for c2 in range(6):
        if c1 == c2:
            continue

        p = 0
        f = 0

        for i in range(len(select)):
            tf = firm.index(select[i])
            tp = price[c1][tf]

            if i == 0 or p > tp:
                f = tf
                p = tp

        print(country[c1], '          ', country[c2], '        ', firm[f],
              '              ', p)

        if len(select) == 1:
            select = firm.copy()
        else:
            select.remove(firm[f])
