def get_tile_number(X):
    tile_number = 0
    if (X >= 0 and X < 120):
        tile_number = 1
    elif (X >= 120 and X < 4080):
        if (X % 120 == 0):
            tile_number = X // 120 + 1
        else:    
            tile_number = X // 120
    else:
        tile_number = 33
    return tile_number        
            
if __name__ == '__main__':

    print(get_tile_number(2880))
