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
    # zone J 1-69
    generate_row(69, x, 0, 'J', 1)

    # zone J 70-144
    generate_row(75, x, 3, 'J', 70)
        
        
generate_rectangles(25)
