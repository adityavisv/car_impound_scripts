# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
def generate_row(rowcount, xscale, yscale, rowLabel, start):
    j = start
    for i in range(rowcount):
        id = '{}{}'.format(rowLabel, j)
        j = j+1
        rectstr = '<rect id="{}" x="{}"  y="{}" width="{}" height="{}" stroke="black" fill="green" strokeWidth="2"  onClick={} />'.format(id, xscale * i, yscale * xscale, xscale, xscale, "{this.showModal}")
        print(rectstr)
        
def generate_rectangles(x):
    # zone A 1-28
    generate_row(28, x, 0, 'A', 1)

    # zone A 29-56
    generate_row(28, x, 1, 'A', 29)
        
    # zone A 57-89
    generate_row(33, x, 4, 'A', 57)
        
    # zone B 1-34
    generate_row(34, x, 5.5, 'B', 1)
    
    # zone B 35-71
    generate_row(37, x, 8.5, 'B', 35)
        
    # zone C 1-37
    generate_row(37, x, 10, 'C', 1)
    
    # zone C 38-76
    generate_row(39, x, 13, 'C', 38)
    
    # zone D 1-40
    generate_row(40, x, 14.5, 'D', 1)
    
    # zone D 41-86
    generate_row(46, x, 17.5, 'D', 41)
    
    # zone E 1-46
    generate_row(46, x, 19, 'E', 1)
    
    # zone E 47-95
    generate_row(49, x, 22, 'E', 47)
    
    # zone F 1-49
    generate_row(49, x, 23.5, 'F', 1)
    
    # zone F 50-101
    generate_row(52, x, 26.5, 'F', 50)
    
    # zone G 1-53
    generate_row(53, x, 28, 'G', 1)
    
    # zone G 54-109
    generate_row(56, x, 31, 'G', 54)
    
    # zone H 1-57
    generate_row(57, x, 32.5, 'H', 1)
    
    # zone H 58-118
    generate_row(61, x, 35.5, 'H', 58)
    
    # zone I 1-62
    generate_row(62, x, 37, 'I', 1)
    
    # zone I 63-129
    generate_row(67, x, 40, 'I', 63)
    
    # zone J 1-69
    generate_row(69, x, 41.5, 'J', 1)
    
    # zone J 70-144
    generate_row(75, x, 44.5, 'J', 70)
    
    # zone K 1-78
    generate_row(78, x, 46, 'K', 1)
    
    # zone K 79-165
    generate_row(87, x, 49, 'K', 79)
    
    # zone L 1-92
    generate_row(92, x, 50.5, 'L', 1)
    
    # zone L 93-193
    generate_row(101, x, 53.5, 'L', 93)
    
    # zone M 1-104
    generate_row(104, x, 55, 'M', 1)
    
    # zone M 105-213
    generate_row(109, x, 58, 'M', 105)
    
    # zone N 1-111
    generate_row(111, x, 59.5, 'N', 1)
    
    # zone O 1-134
    generate_row(134, x, 62.5, 'O', 1)
generate_rectangles(20)
