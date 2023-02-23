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
        
        
generate_rectangles(25)
