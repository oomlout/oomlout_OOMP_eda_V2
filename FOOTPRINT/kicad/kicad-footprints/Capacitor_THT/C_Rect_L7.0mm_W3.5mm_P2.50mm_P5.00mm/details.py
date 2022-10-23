
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Capacitor_THT"
    oIndex = "C_Rect_L7.0mm_W3.5mm_P2.50mm_P5.00mm"
    hexID = "FZKCCRECTL7W35P25P5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'C_Rect_L7.0mm_W3.5mm_P2.50mm_P5.00mm', 'description': 'C, Rect series, Radial, pin pitch=2.50mm 5.00mm, , length*width=7*3.5mm^2, Capacitor', 'tags': 'C Rect series Radial pin pitch 2.50mm 5.00mm  length 7mm width 3.5mm Capacitor', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Capacitor_THT.3dshapes/C_Rect_L7.0mm_W3.5mm_P2.50mm_P5.00mm.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Capacitor_THT : C_Rect_L7.0mm_W3.5mm_P2.50mm_P5.00mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

