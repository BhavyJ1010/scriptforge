import cv2

def clean_glyph_boxes(boxes, min_width=8, min_height=8, min_area=80):
    
    filtered_boxes = []

    for x, y, w, h in boxes:
        area = w*h
    
        if (w >= min_width and h >= min_height and area >= min_area):

            filtered_boxes.append((x,y,w,h))

    return filtered_boxes
