def get_all_moves(two_pts): # points in internal (y, x) format
    if two_pts[0][0] == two_pts[1][0]: # y same, l or r it is
        if two_pts[0][1] < two_pts[1][1]:
            return [two_pts[0], "r"]
        return [two_pts[0], "l"]
    if two_pts[0][0] < two_pts[1][0]:
        return [two_pts[0], "d"]
    return [two_pts[0], "u"]
