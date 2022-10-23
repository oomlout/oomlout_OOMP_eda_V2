
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Capacitor_THT"
    oIndex = "C_Rect_L13.0mm_W6.5mm_P7.50mm_P10.00mm"
    hexID = "FZKCCRECTL13W65P75P1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'C_Rect_L13.0mm_W6.5mm_P7.50mm_P10.00mm', 'description': 'C, Rect series, Radial, pin pitch=7.50mm 10.00mm, , length*width=13*6.5mm^2, Capacitor', 'tags': 'C Rect series Radial pin pitch 7.50mm 10.00mm  length 13mm width 6.5mm Capacitor', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Capacitor_THT.3dshapes/C_Rect_L13.0mm_W6.5mm_P7.50mm_P10.00mm.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Capacitor_THT : C_Rect_L13.0mm_W6.5mm_P7.50mm_P10.00mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

