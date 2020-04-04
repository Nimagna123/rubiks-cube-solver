"""white = ['b','b','b','b','y','y','y','g','w']
red = ['y','g','g','o','r','w','r','r','r']
orange = ['g','r','y','o','b','w','o','b','o']
blue = ['w','b','o','g','w','w','o','o','b']
green = ['w','r','g','o','r','g','o','r','g']
yellow = ['y','r','g','y','w','b','y','w','y']"""

white = []
red = []
orange = []
blue = []
green = []
yellow = []


def display(face):
    for i in range(9):
        print(face[i]+" ")
    print("")

def rotate_clock(choice):
    if (choice=='w'):
        print("White")
        white[3],white[7]=white[7],white[3]
        white[4],white[6]=white[6],white[4]
        white[2],white[0]=white[0],white[2]
        white[5],white[7]=white[7],white[5]
        white[4],white[0]=white[0],white[4]
        white[3],white[1]=white[1],white[3]

        orange[0],blue[0]=blue[0],orange[0]
        orange[7],blue[7]=blue[7],orange[7]
        orange[6],blue[6]=blue[6],orange[6]
        green[6],orange[6]=orange[6],green[6]
        green[7],orange[7]=orange[7],green[7]
        green[0],orange[0]=orange[0],green[0]
        red[6],green[6]=green[6],red[6]
        red[7],green[7]=green[7],red[7]
        red[0],green[0]=green[0],red[0]

  
    elif(choice=='r'):
        print("Red")
        red[4],red[0]=red[0],red[4]
        red[5],red[7]=red[7],red[5]
        red[3],red[1]=red[1],red[3]
        red[6],red[0]=red[0],red[6]
        red[5],red[1]=red[1],red[5]
        red[4],red[2]=red[2],red[4]
    
        white[3],blue[6]=blue[6],white[3]
        white[2],blue[5]=blue[5],white[2]
        white[1],blue[4]=blue[4],white[1]
        green[0],white[1]=white[1],green[0]
        green[1],white[2]=white[2],green[1]
        green[2],white[3]=white[3],green[2]
        yellow[3],green[0]=green[0],yellow[3]
        yellow[2],green[1]=green[1],yellow[2]
        yellow[1],green[2]=green[2],yellow[1]
        

    elif(choice=='y'):
        print("Yellow")
        yellow[5],yellow[1]=yellow[1],yellow[5]
        yellow[4],yellow[2]=yellow[2],yellow[4]
        yellow[6],yellow[0]=yellow[0],yellow[6]
        yellow[3],yellow[1]=yellow[1],yellow[3]
        yellow[4],yellow[0]=yellow[0],yellow[4]
        yellow[5],yellow[7]=yellow[7],yellow[5]
          
        red[4],blue[4]=blue[4],red[4]
        red[3],blue[3]=blue[3],red[3]
        red[2],blue[2]=blue[2],red[2]
        green[2],red[2]=red[2],green[2]
        green[3],red[3]=red[3],green[3]
        green[4],red[4]=red[4],green[4]
        orange[4],green[4]=green[4],orange[4]
        orange[3],green[3]=green[3],orange[3]
        orange[2],green[2]=green[2],orange[2]


    elif(choice=='o'):
        print("Orange")
        orange[0],orange[4]=orange[4],orange[0]
        orange[1],orange[3]=orange[3],orange[1]
        orange[7],orange[5]=orange[5],orange[7]
        orange[2],orange[4]=orange[4],orange[2]
        orange[1],orange[5]=orange[5],orange[1]
        orange[0],orange[6]=orange[6],orange[0]

        yellow[5],blue[2]=blue[2],yellow[5]
        yellow[6],blue[1]=blue[1],yellow[6]
        yellow[7],blue[0]=blue[0],yellow[7]
        green[6],yellow[5]=yellow[5],green[6]
        green[5],yellow[6]=yellow[6],green[5]
        green[4],yellow[7]=yellow[7],green[4]
        white[7],green[6]=green[6],white[7]
        white[6],green[5]=green[5],white[6]
        white[5],green[4]=green[4],white[5]


    elif(choice=='g'):
        print("Green")
        green[2],green[6]=green[6],green[2]
        green[3],green[5]=green[5],green[3]
        green[1],green[7]=green[7],green[1]
        green[6],green[4]=green[4],green[6]
        green[3],green[7]=green[7],green[3]
        green[2],green[0]=green[0],green[2]
        
        orange[2],white[5]=white[5],orange[2]
        orange[1],white[4]=white[4],orange[1]
        orange[0],white[3]=white[3],orange[0]
        orange[2],yellow[3]=yellow[3],orange[2]
        orange[1],yellow[4]=yellow[4],orange[1]
        orange[0],yellow[5]=yellow[5],orange[0]
        red[6],yellow[3]=yellow[3],red[6]
        red[5],yellow[4]=yellow[4],red[5]
        red[4],yellow[5]=yellow[5],red[4]
    
    elif(choice=='b'):
        print("Blue")
        blue[7],blue[1]=blue[1],blue[7]
        blue[6],blue[2]=blue[2],blue[6]
        blue[3],blue[5]=blue[5],blue[3]
        blue[0],blue[2]=blue[2],blue[0]
        blue[3],blue[7]=blue[7],blue[3]
        blue[4],blue[6]=blue[6],blue[4]
        
        orange[4],yellow[1]=yellow[1],orange[4]
        orange[5],yellow[0]=yellow[0],orange[5]
        orange[6],yellow[7]=yellow[7],orange[6]
        orange[4],white[7]=white[7],orange[4]
        orange[5],white[0]=white[0],orange[5]
        orange[6],white[1]=white[1],orange[6]
        red[0],white[7]=white[7],red[0]
        red[1],white[0]=white[0],red[1]
        red[2],white[1]=white[1],red[2]

 
def white_bottom(q):
    if((yellow[0]=='w' and blue[3]==q) or (yellow[2]=='w' and red[3]==q) or (yellow[4]=='w' and green[3]==q) or (yellow[6]=='w' and orange[3]==q)):
        if(q=='b'):
            while(blue[3]!=q or yellow[0]!='w'):
                rotate_clock('y')
        if(q=='r'):
            while(red[3]!=q or yellow[2]!='w'):
                rotate_clock('y')
            if(q!='b'):
                while(white[0]!='w' and blue[7]!='b'):
                    rotate_clock('w')
        
        if(q=='g'):
            while(green[3]!=q or yellow[4]!='w'):
                rotate_clock('y')
            if(q!='b'):
                while(white[0]!='w' and blue[7]!='b'):
                    rotate_clock('w')
        
        if(q=='o'):
            while(orange[3]!=q or yellow[6]!='w'):
                rotate_clock('y')
            if(q!='b'):
                while(white[0]!='w' and blue[7]!='b'):
                    rotate_clock('w')
        
        rotate_clock(q)
        rotate_clock(q)

def right_alg(a,c):
    rotate_clock(a)
    rotate_clock(a)
    rotate_clock(a)
    rotate_clock('y')
    rotate_clock(a)
    white_bottom(c)


def white_right(q):
    if(blue[1]=='w' or red[1]=='w' or green[1]=='w' or orange[1]=='w'):
        if(blue[5]==q and red[1]=='w'):
            right_alg('b',q)
        if(red[5]==q and green[1]=='w'):
            right_alg('r',q)
        if(green[5]==q and orange[1]=='w'):
            right_alg('g',q)
        if(orange[5]==q and blue[1]=='w'):
            right_alg('o',q)
    
def left_alg(a,c):
    rotate_clock(a)
    rotate_clock('y')
    rotate_clock(a)
    rotate_clock(a)
    rotate_clock(a)
    white_bottom(c)

def white_left(q):
    if(blue[5]=='w' or red[5]=='w' or green[5]=='w' or orange[5]=='w'):
        if(blue[5]=='w' and red[1]==q):
            left_alg('r',q)
        if(red[5]=='w' and green[1]==q):
            left_alg('g',q)
        if(green[5]=='w' and orange[1]==q):
            left_alg('o',q)
        if(orange[5]=='w' and blue[1]==q):
            left_alg('b',q)
    
def top_alg(a, b, c):
    rotate_clock(a)
    rotate_clock(a)
    rotate_clock(a)
    rotate_clock('w')
    rotate_clock(b)
    rotate_clock('w')
    rotate_clock('w')
    rotate_clock('w')
    white_bottom(c)
    
def white_top(q):
    if (blue[7] == 'w' and white[0] == q):
        top_alg('b', 'r', q)    
    if (red[7] == 'w' and white[2] == q):
        top_alg('r', 'g', q)    
    if (green[7] == 'w' and white[4] == q):
        top_alg('g', 'o', q)
    if (orange[7] == 'w' and white[6] == q):
        top_alg('o', 'b', q)
        
def inv_alg(a, b, c):
    rotate_clock(a)
    rotate_clock(b)
    rotate_clock('y')
    rotate_clock('y')
    rotate_clock('y')
    rotate_clock(b)
    rotate_clock(b)
    rotate_clock(b)
    rotate_clock(a)
    rotate_clock(a)
    rotate_clock(a)
    white_bottom(c)


def white_bottom_inverted(q):
    if (blue[3] == 'w' or red[3] == 'w' or green[3] == 'w' or orange[3] == 'w'):
        if (blue[3] == 'w' and yellow[0] == q):
            inv_alg('b', 'r', q)        
        if (red[3] == 'w' and yellow[2] == q):
            inv_alg('r', 'g', q)        
        if (green[3] == 'w' and yellow[4] == q):
            inv_alg('g', 'o', q)        
        if (orange[3] == 'w' and yellow[6] == q):
            inv_alg('o', 'b', q)
    
 
def solve_white_cross():
    prefer = ['b','r','g','o']
        
    for i in range(4):
        if (white[0] == 'w' and blue[7] == prefer[i]):
            rotate_clock('b')
        if (white[2] == 'w' and red[7] == prefer[i]):
            rotate_clock('r')        
        if (white[4] == 'w' and green[7] == prefer[i]):
            rotate_clock('g')        
        if (white[6] == 'w' and orange[7] == prefer[i]):
            rotate_clock('o')        
        white_bottom(prefer[i])
        white_bottom_inverted(prefer[i])
        white_left(prefer[i])
        white_right(prefer[i])
        white_top(prefer[i])
        if (i != 0):
            while (blue[7] != 'b'):
                rotate_clock('w')
        if (white[0] == 'w' and white[2] == 'w' and white[4] == 'w' and white[6] == 'w' and blue[7] == 'b' and red[7] == 'r' and green[7] == 'g' and orange[7] == 'o'):
            break

 
def white_corners_alg_left():
    rotate_clock('b')
    rotate_clock('b')
    rotate_clock('b')
    rotate_clock('y')
    rotate_clock('y')
    rotate_clock('y')
    rotate_clock('b')

def white_corners_alg_right():
    rotate_clock('r')
    rotate_clock('y')
    rotate_clock('r')
    rotate_clock('r')
    rotate_clock('r')

def solve_white_corners():
    while (red[0] != 'r' or red[6] != 'r' or blue[0] != 'b' or blue[6] != 'b' or orange[0] != 'o' or orange[6] != 'o' or green[0] != 'g' or green[6] != 'g'):
        while (red[7] != 'r'):
            rotate_clock('w')
        
        if (blue[4] == 'w' or red[4] == 'w' or green[4] == 'w' or orange[4] == 'w'):
            while (blue[4] != 'w'):
                rotate_clock('y')
            while (red[2] != red[7]):
                rotate_clock('w')            
            white_corners_alg_left()
            while (red[7] != 'r'):
                rotate_clock('w')
            
        elif (blue[2] == 'w' or red[2] == 'w' or green[2] == 'w' or orange[2] == 'w'):
            while (red[2] != 'w'):
                rotate_clock('y')
            
            while (red[7] != yellow[1]):
                rotate_clock('w')
            
            white_corners_alg_right()
            while (red[7] != 'r'):
                rotate_clock('w')
            
        elif (yellow[1] == 'w' or yellow[3] == 'w' or yellow[5] == 'w' or yellow[7] == 'w'):
            while (yellow[1] != 'w'):
                rotate_clock('y')
            
            while (red[2] != blue[7]):
                rotate_clock('w')
            
            rotate_clock('b')
            rotate_clock('b')
            rotate_clock('b')
            rotate_clock('y')
            rotate_clock('y')
            rotate_clock('b')
            while (blue[4] != 'w'):
                rotate_clock('y')
            
            while (red[2] != red[7]):
                rotate_clock('w')
            
            white_corners_alg_left()
            while (red[7] != 'r'):
                rotate_clock('w')
            
        else:
            while (red[7] == red[0]):
                rotate_clock('w')
            
            white_corners_alg_left()
            while (red[7] != 'r'):
                rotate_clock('w')

def middle_place_left_alg(left, center):
    rotate_clock('y')
    rotate_clock('y')
    rotate_clock('y')
    rotate_clock(left)
    rotate_clock(left)
    rotate_clock(left)
    rotate_clock('y')
    rotate_clock(left)
    rotate_clock('y')
    rotate_clock(center)
    rotate_clock('y')
    rotate_clock('y')
    rotate_clock('y')
    rotate_clock(center)
    rotate_clock(center)
    rotate_clock(center)


def middle_place_right_alg(center, right):
    rotate_clock('y')
    rotate_clock(right)
    rotate_clock('y')
    rotate_clock('y')
    rotate_clock('y')
    rotate_clock(right)
    rotate_clock(right)
    rotate_clock(right)
    rotate_clock('y')
    rotate_clock('y')
    rotate_clock('y')
    rotate_clock(center)
    rotate_clock(center)
    rotate_clock(center)
    rotate_clock('y')
    rotate_clock(center)

def solve_middle_layer():
    while (red[5] != 'r' or red[1] != 'r' or blue[1] != 'b' or blue[5] != 'b' or orange[1] != 'o' or orange[5] != 'o' or green[1] != 'g' or green[5] != 'g'):

        if ((orange[1] != 'o' and green[5] != 'g') and (orange[1] != 'y' or green[5] != 'y')):
            while (green[3] != 'y' and yellow[4] != 'y'):
                rotate_clock('y')
            
            middle_place_right_alg('g', 'o')
        elif ((orange[5] != 'o' and blue[1] != 'b') and (orange[5] != 'y' or blue[1] != 'y')):
            while (orange[3] != 'y' and yellow[6] != 'y'):
                rotate_clock('y')
            
            middle_place_right_alg('o', 'b')
        elif ((blue[5] != 'b' and red[1] != 'r') and (blue[5] != 'y' or red[1] != 'y')):
            while (blue[3] != 'y' and yellow[0] != 'y'):
                rotate_clock('y')
            
            middle_place_right_alg('b', 'r')
        elif ((red[5] != 'r' and green[1] != 'g') and (red[5] != 'y' or green[1] != 'y')):
            while (red[3] != 'y' and yellow[2] != 'y'):
                rotate_clock('y')
            
            middle_place_right_alg('r', 'g')
        

        while (red[3] == 'y' or yellow[2] == 'y'):
            rotate_clock('y')
        

        if (red[3] == 'r' and yellow[2] != 'y'):
            if (yellow[2] == 'g'):
                middle_place_right_alg('r', 'g')
            elif (yellow[2] == 'b'):
                middle_place_left_alg('b', 'r')
            
        elif (red[3] == 'b' and yellow[2] != 'y'):
            rotate_clock('y')
            if (yellow[0] == 'r'):
                middle_place_right_alg('b', 'r')
            elif (yellow[0] == 'o'):
                middle_place_left_alg('o', 'b')
            
        elif (red[3] == 'o' and yellow[2] != 'y'):
            rotate_clock('y')
            rotate_clock('y')
            if (yellow[6] == 'b'):
                middle_place_right_alg('o', 'b')
            elif (yellow[6] == 'g'):
                middle_place_left_alg('g', 'o')
            
        elif (red[3] == 'g' and yellow[2] != 'y'):
            rotate_clock('y')
            rotate_clock('y')
            rotate_clock('y')
            if (yellow[4] == 'o'):
                middle_place_right_alg('g', 'o')
            elif (yellow[4] == 'r'):
                middle_place_left_alg('r', 'g')
            
def yellow_cross_algorithm():
    rotate_clock('r')
    rotate_clock('y')
    rotate_clock('g')
    rotate_clock('y')
    rotate_clock('y')
    rotate_clock('y')
    rotate_clock('g')
    rotate_clock('g')
    rotate_clock('g')
    rotate_clock('r')
    rotate_clock('r')
    rotate_clock('r')

def solve_yellow_cross():
    while (yellow[0] != 'y' or yellow[2] != 'y' or yellow[4] != 'y' or yellow[6] != 'y'):
        if ((yellow[0] == 'y' and yellow[6] == 'y') or (yellow[4] == 'y' and yellow[6] == 'y') or
            (yellow[2] == 'y' and yellow[4] == 'y') or (yellow[0] == 'y' and yellow[2] == 'y')):
            while (yellow[0] != 'y' and yellow[6] != 'y'):
                rotate_clock('y')
            
            yellow_cross_algorithm()
        
        if ((yellow[2] == 'y' and yellow[6] == 'y') or (yellow[0] == 'y' and yellow[4] == 'y')):
            while (yellow[0] != 'y' and yellow[4] != 'y'):
                rotate_clock('y')
            
            yellow_cross_algorithm()
            yellow_cross_algorithm()
        elif (yellow[8] == 'y'):
            yellow_cross_algorithm()
            rotate_clock('y')
            yellow_cross_algorithm()
            yellow_cross_algorithm()
        
    

def yellow_corners_algorithm():
    rotate_clock('g')
    rotate_clock('y')
    rotate_clock('g')
    rotate_clock('g')
    rotate_clock('g')
    rotate_clock('y')
    rotate_clock('g')
    rotate_clock('y')
    rotate_clock('y')
    rotate_clock('g')
    rotate_clock('g')
    rotate_clock('g')

def solve_yellow_corners():
    while (yellow[1] != 'y' or yellow[3] != 'y' or yellow[5] != 'y' or yellow[7] != 'y'):
        if ((yellow[1] == 'y' and yellow[3] != 'y' and yellow[5] != 'y' and yellow[7] != 'y') or
            (yellow[3] == 'y' and yellow[1] != 'y' and yellow[5] != 'y' and yellow[7] != 'y') or
            (yellow[5] == 'y' and yellow[1] != 'y' and yellow[3] != 'y' and yellow[7] != 'y') or
            (yellow[7] == 'y' and yellow[1] != 'y' and yellow[3] != 'y' and yellow[5] != 'y')):
            while (yellow[1] != 'y'):
                rotate_clock('y')
            
            yellow_corners_algorithm()
        elif ((green[2] == 'y' and green[4] == 'y' and yellow[1] == 'y' and yellow[7] == 'y') or
            (orange[2] == 'y' and orange[4] == 'y' and yellow[1] == 'y' and yellow[3] == 'y') or
            (blue[2] == 'y' and blue[4] == 'y' and yellow[3] == 'y' and yellow[5] == 'y') or
            (red[2] == 'y' and red[4] == 'y' and yellow[5] == 'y' and yellow[7] == 'y')):
            while (red[2] != 'y' and red[4] != 'y' and yellow[5] != 'y' and yellow[7] != 'y'):
                rotate_clock('y')
            
            yellow_corners_algorithm()
        elif ((red[4] == 'y' and orange[2] == 'y' and yellow[1] == 'y' and yellow[7] == 'y') or
            (blue[2] == 'y' and green[4] == 'y' and yellow[1] == 'y' and yellow[3] == 'y') or
            (red[2] == 'y' and orange[4] == 'y' and yellow[3] == 'y' and yellow[5] == 'y') or
            (blue[4] == 'y' and green[2] == 'y' and yellow[5] == 'y' and yellow[7] == 'y')):
            while (red[2] != 'y' and orange[4] != 'y' and yellow[3] != 'y' and yellow[5] != 'y'):
                rotate_clock('y')
            
            yellow_corners_algorithm()
        elif ((green[2] == 'y' and green[4] == 'y' and blue[2] == 'y' and blue[4] == 'y') or
            (red[2] == 'y' and red[4] == 'y' and orange[2] == 'y' and orange[4] == 'y')):
            while (green[2] != 'y' and green[4] != 'y' and blue[2] != 'y' and blue[4] != 'y'):
                rotate_clock('y')
            
            yellow_corners_algorithm()
        elif ((green[2] == 'y' and orange[2] == 'y' and orange[4] == 'y' and blue[4] == 'y') or
            (red[4] == 'y' and orange[2] == 'y' and blue[2] == 'y' and blue[4] == 'y') or
            (red[2] == 'y' and red[4] == 'y' and green[4] == 'y' and blue[2] == 'y') or
            (green[2] == 'y' and green[4] == 'y' and orange[4] == 'y' and red[2] == 'y')):
            while (green[2] != 'y' and orange[2] != 'y' and orange[4] != 'y' and blue[4] != 'y'):
                rotate_clock('y')
            
            yellow_corners_algorithm()
        elif ((yellow[1] == 'y' and yellow[5] == 'y' and yellow[3] != 'y' and yellow[7] != 'y') or
            (yellow[3] == 'y' and yellow[7] == 'y' and yellow[1] != 'y' and yellow[5] != 'y')):
            while (red[2] != 'y' and green[4] != 'y'):
                rotate_clock('y')
            
            yellow_corners_algorithm()
        
    

def yellow_corner_orientation_algorithm():
    rotate_clock('g')
    rotate_clock('g')
    rotate_clock('g')
    rotate_clock('r')
    rotate_clock('g')
    rotate_clock('g')
    rotate_clock('g')
    rotate_clock('o')
    rotate_clock('o')
    rotate_clock('g')
    rotate_clock('r')
    rotate_clock('r')
    rotate_clock('r')
    rotate_clock('g')
    rotate_clock('g')
    rotate_clock('g')
    rotate_clock('o')
    rotate_clock('o')
    rotate_clock('g')
    rotate_clock('g')
    rotate_clock('y')
    rotate_clock('y')
    rotate_clock('y')

def yellow_corner_orientation():
    while (red[2] != 'r' or red[4] != 'r' or green[2] != 'g' or green[4] != 'g' or
        orange[2] != 'o' or orange[4] != 'o' or blue[2] != 'b' or blue[4] != 'b'):
        if ((red[2] == red[4]) or (green[2] == green[4]) or (orange[2] == orange[4]) or (blue[2] == blue[4])):
            while (orange[2] != orange[4]):
                rotate_clock('y')
            
            yellow_corner_orientation_algorithm()
            while (blue[2] != 'b'):
                rotate_clock('y')
            
        else:
            while (orange[4] != 'o' and red[4] != 'r'):
                rotate_clock('y')
            
            yellow_corner_orientation_algorithm()
            while (orange[2] != orange[4]):
                rotate_clock('y')
            
            yellow_corner_orientation_algorithm()
            while (blue[2] != 'b'):
                rotate_clock('y')
            
        
    

def yellow_edges_colour_arrangement_right():
    rotate_clock('r')
    rotate_clock('r')
    rotate_clock('y')
    rotate_clock('y')
    rotate_clock('y')
    rotate_clock('g')
    rotate_clock('g')
    rotate_clock('g')
    rotate_clock('b')
    rotate_clock('r')
    rotate_clock('r')
    rotate_clock('b')
    rotate_clock('b')
    rotate_clock('b')
    rotate_clock('g')
    rotate_clock('y')
    rotate_clock('y')
    rotate_clock('y')
    rotate_clock('r')
    rotate_clock('r')

def yellow_edges_colour_arrangement_left():
    rotate_clock('r')
    rotate_clock('r')
    rotate_clock('y')
    rotate_clock('b')
    rotate_clock('g')
    rotate_clock('g')
    rotate_clock('g')
    rotate_clock('r')
    rotate_clock('r')
    rotate_clock('b')
    rotate_clock('b')
    rotate_clock('b')
    rotate_clock('g')
    rotate_clock('y')
    rotate_clock('r')
    rotate_clock('r')

def yellow_edges_colour_arrangement():
    while (red[2] != 'r'):
        rotate_clock('r')
    
    if (red[3] == 'o' and orange[3] == 'r' and blue[3] == 'g' and green[3] == 'b'):
        yellow_edges_colour_arrangement_left()
    elif (red[3] == 'b' and blue[3] == 'r'):
        yellow_edges_colour_arrangement_left()
    elif (red[3] == 'g' and green[3] == 'r'):
        yellow_edges_colour_arrangement_left()
    
    while (orange[2] != orange[3]):
        rotate_clock('y')
    
    if (red[3] == green[2]):
        yellow_edges_colour_arrangement_right()
    elif (red[3] == blue[2]):
        yellow_edges_colour_arrangement_left()
    
    while (red[3] != 'r'):
        rotate_clock('y')

def main():
    print("________________________| RUBIK'S CUBE SOLVER |________________________")
    print("Input :")
    
    print("White Side : ")
    for i in range(9):
        white.append(input())
    
    print("Red Side : ")
    for i in range(9):
        red.append(input())
    
    print("Orange Side : ")
    for i in range(9):
        orange.append(input())
    
    print("Blue Side : ")
    for i in range(9):
        blue.append(input())
    
    print("Green Side : ")
    for i in range(9):
        green.append(input())
    
    print("Yellow Side : ")
    for i in range(9):
        yellow.append(input())
    
    #-----------------------------------
    print("-------------------------------------------------")
    print("Rotate these sides in Clockwise Direction by 90 degrees in this exact order...")
    solve_white_cross()
    solve_white_corners()
    solve_middle_layer()
    solve_yellow_cross()
    solve_yellow_corners()
    yellow_corner_orientation()
    yellow_edges_colour_arrangement()
    #------------------------------------
    print("-------------------------------------------------")
    print("Your Cube is now solved Output : ")
    print("White Side : ")
    display(white)
    print("Red Side : ")
    display(red)
    print("Orange Side : ")
    display(orange)
    print("Blue Side : ")
    display(blue)
    print("Green Side : ")
    display(green)
    print("Yellow Side : ")
    display(yellow)
    
main()