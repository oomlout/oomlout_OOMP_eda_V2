
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Capacitor_THT"
    oIndex = "C_Rect_L10.0mm_W5.0mm_P5.00mm_P7.50mm"
    hexID = "FZKCCRECTL1W5P5P75"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'C_Rect_L10.0mm_W5.0mm_P5.00mm_P7.50mm', 'description': 'C, Rect series, Radial, pin pitch=5.00mm 7.50mm, , length*width=10*5mm^2, Capacitor', 'tags': 'C Rect series Radial pin pitch 5.00mm 7.50mm  length 10mm width 5mm Capacitor', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Capacitor_THT.3dshapes/C_Rect_L10.0mm_W5.0mm_P5.00mm_P7.50mm.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Capacitor_THT : C_Rect_L10.0mm_W5.0mm_P5.00mm_P7.50mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

