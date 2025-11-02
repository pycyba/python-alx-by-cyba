SP = '.'
GW = '$'
wysokosc = int(input('Podaj wysokość: '))
lgw = 1
lsp = wysokosc
for i in range(wysokosc):
    print(SP * lsp + GW * lgw + SP * lsp)
    lgw += 2
    lsp -= 1
