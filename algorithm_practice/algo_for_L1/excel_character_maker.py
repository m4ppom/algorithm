def excel_alpha(idx):
    result = ""
    idx += 1
    if idx <= 1:
        result = "A"
        return result
    while 1:
        if idx > 26:
            idx, r = divmod(idx - 1, 26)
            result = chr(r + ord('A')) + result
        else:
            return chr(idx + ord('A') - 1) + result
# for i in range(1, 16386):
#     print ("%4d : %s" % (i, excel_alpha(i)))
print(excel_alpha(10))