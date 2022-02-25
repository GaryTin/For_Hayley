from turtle import *
from math import floor

def draw_buildings(buildings,shift,scale):

    t = Turtle()
    t.pu()
    t.speed(0)
    t.hideturtle()
    for building in buildings:
        t.goto(building[0]*scale+shift,shift)
        t.pd()
        t.goto(building[0] * scale  +shift, building[2] * scale +shift)
        t.goto(building[1] * scale+shift, building[2] * scale+shift)
        t.goto(building[1] * scale+shift, shift)
        t.pu()
def draw_line(lines,shift,scale):
    t = Turtle()
    t.pu()
    t.speed(0)
    t.pensize(3)
    t.hideturtle()

    for line in lines:
        if line[1] > 0:
            t.pencolor('red')
            t.goto(line[0] * scale + shift, shift)
            t.pd()
            t.goto(line[0] * scale + shift, line[1] * scale + shift)
            t.pu()
        else:
            t.pencolor('green')
            t.goto(line[0] * scale + shift, shift+line[1] * scale*-1)
            t.pd()
            t.goto(line[0] * scale + shift,  shift)
            t.pu()
def build_data(buildings):
    l=[]
    r=[]
    h=[]
    for building in buildings:
        l.append(building[0])
        r.append(building[1])
        h.append(building[2])
    return l,r,h

def maxheight(x):
    max = 0
    for building in buildings:
        if (x>=building[0] and x<=building[1]) and (building[2]>max):
            max = building[2]
    return max


def sil(p,q):
    m = floor((p+q)/2)
    if p == q:
        return [(l[p],h[p]),(r[p],-h[p])]
    else:
        left_result = sil(p,m)
        right_result = sil(m+1,q)
        left_len = len(left_result) -1
        right_len = len(right_result) -1
        left_pt = 0
        right_pt = 0

        final_result = []
        while (left_pt <= left_len) and (right_pt<=right_len):
            if left_result[left_pt][0] < right_result[right_pt][0]:
                if left_result[left_pt][1]>0:
                    if maxheight(left_result[left_pt][0])==(left_result[left_pt][1]):
                        final_result.append(left_result[left_pt])
                elif left_result[left_pt][1]<0:
                    if maxheight(left_result[left_pt][0])==(left_result[left_pt][1] * -1):
                        final_result.append(left_result[left_pt])

                left_pt = left_pt + 1
            else:
                if right_result[right_pt][1] > 0:
                    if maxheight(right_result[right_pt][0]) == (right_result[right_pt][1]):
                        final_result.append(right_result[right_pt])

                elif right_result[right_pt][1] < 0:
                    if maxheight(right_result[right_pt][0]) == (right_result[right_pt][1] * -1):
                        final_result.append(right_result[right_pt])
                right_pt = right_pt + 1

        if (right_pt<=right_len):
            final_result.extend(right_result[right_pt::])
        else:
            final_result.extend(left_result[left_pt::])

        return final_result


if __name__ == "__main__":
    buildings = [[1,4,2],[8,9,5],[7,10,3],[3,6,3],[2,5,4]] #[1,4,2],[8,9,5],[7,10,3],[3,6,3],[2,5,4]
    l,r,h = build_data(buildings)
    draw_buildings(buildings,-500,100)
    result = sil(0,len(buildings)-1)
    print(result)
    draw_line(result,-500,100)

    done()