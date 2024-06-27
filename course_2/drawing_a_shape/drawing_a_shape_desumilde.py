h = 4

for i in range(h):
  row = list(map(lambda _: ' ', range(h + 1)))
  row[len(row) - (2 + i)] = '/'
  row[len(row) - 1] = '|'
  row = ''.join(row)
  if i == len(row) - 2:
    row = '_'.join(row.split(' '))
  print(row)


