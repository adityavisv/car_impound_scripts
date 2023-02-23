# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
def generate_row(rowcount, xscale, yscale, rowLabel, start):
    j = start
    for i in range(rowcount):
        id = '{}{}'.format(rowLabel, j)
        j = j+1
        rectstr = '<rect id="{}" x="{}px"  y="{}px" width="{}px" height="{}px" stroke="black" fill="green" strokeWidth="2"  onClick={} />'.format(id, xscale * i, xscale * yscale, xscale, xscale, "{this.showModal}")
        print(rectstr)
        
def generate_rectangles(x):
    # zone F 1-49
    generate_row(rowcount = 49, xscale = x, yscale = 0, rowLabel = 'F', start = 1)

    # zone F 50-101
    generate_row(rowcount = 52, xscale = x, yscale = 3, rowLabel = 'F', start = 50)
        
        
generate_rectangles(25)
