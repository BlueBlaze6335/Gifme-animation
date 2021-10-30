import cv2
import cvzone
cap=cv2.VideoCapture("balnobg.mp4")
overlay=cv2.imread("ball-removebg-preview.png", cv2.IMREAD_UNCHANGED)
y=[500, 504, 507, 510, 515, 520, 523, 534, 543, 552, 561, 571, 582, 593, 605, 617, 626, 643, 656, 670, 684, 699, 713, 728, 743, 758, 774, 790, 805, 821, 837, 852, 868, 883, 898, 912, 925, 912, 898, 883, 868, 852, 837, 821, 805, 790, 774, 759, 743, 728, 713, 699, 684, 670, 656, 643, 630, 617, 605, 593, 582, 571, 561, 552, 543, 534, 527, 520, 515, 510, 507, 504, 504, 504, 507, 510, 515, 520, 527, 534, 543, 552, 561, 571, 582, 593, 605, 617, 630, 643, 657, 670, 684, 699, 713, 728, 743, 759, 774, 790, 805, 821, 837, 852, 868, 883, 898, 912, 925, 912, 898, 883, 868, 852, 837, 821, 805, 790, 774, 759, 743, 728, 713, 699, 684, 670, 656, 643, 630, 617, 605, 593, 582, 571, 561, 552, 543, 534, 527, 520, 515, 510, 507, 504, 504, 504, 507, 510, 515, 520, 527, 534, 543, 552, 561, 571, 582, 593, 605, 617, 630, 643, 657, 670, 684, 699, 713, 728, 743, 759, 774, 790, 805, 821, 837, 852, 868, 883, 898, 912, 925, 912, 898, 883, 868, 852, 837, 821, 805, 790, 774, 759, 743, 728, 713, 699, 684, 670, 656, 643, 630, 617, 605, 593, 582, 571, 561, 552, 543, 534, 527, 520, 515, 510, 507, 504, 504, 504, 507, 510, 515, 520, 527, 534, 543, 552, 561, 571, 582, 593, 605, 617, 630, 643, 657, 670, 684, 699, 713, 728, 743, 759, 774, 790, 805, 821, 837, 852, 868, 883, 898, 912, 925, 912, 897, 882, 866, 850, 834, 818, 802, 786, 770, 754, 738, 723, 707, 692, 678, 664, 650, 636, 623, 610, 598, 586, 575, 564, 554, 545, 536, 528, 521, 515, 510, 507, 504, 504]
mean=int(sum(y)/len(y))
print(mean)
x=426
y1=180
while cap.isOpened():
    _,frame=cap.read()
    for i in y:
        if i>mean:
            i=mean
        res=cvzone.overlayPNG(frame,overlay,[x+300,y1+((i-y[0]))])
        cv2.imshow("result",res)
        cv2.waitKey(1)
