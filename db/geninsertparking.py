def generate_stmt(zonelabel, start, end):
    for i in range(start, end+1):
        stmt = "INSERT INTO [dbo].[parking_zone]([oc_status],[slot_num],[zone_label],[vehicle_id]) VALUES('AVAILABLE', {}, '{}', null);".format(i, zonelabel)
        print(stmt)


# zone A 1-88
generate_stmt('A', 1, 88)

# zone B 1-71
generate_stmt('B', 1, 71)

# zone C 1-75
generate_stmt('C', 1, 75)

# zone D 1-85
generate_stmt('D', 1, 85)

# zone E 1-95
generate_stmt('E', 1, 95)

#zone F 1-101
generate_stmt('F', 1, 101)

# zone G 1-109
generate_stmt('G', 1, 109)

# zone H 1-118
generate_stmt('H', 1, 118)

# zone I 1-129
generate_stmt('I', 1, 129)

# zone J 1-144
generate_stmt('J', 1, 144)

# zone K 1-165
generate_stmt('K', 1, 165)

# zone L 1-193
generate_stmt('L', 1, 193)

# zone M 1-213
generate_stmt('M', 1, 213)

# zone N 1-111
generate_stmt('N', 1, 111)

# zone O 1-134
generate_stmt('O', 1, 134)

# zone T 1-76
generate_stmt('T', 1, 76)
