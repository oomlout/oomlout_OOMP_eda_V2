
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Capacitor_THT"
    oIndex = "C_Rect_L33.0mm_W15.0mm_P27.50mm_MKS4"
    hexID = "FZKCCRECTL33W15P275MKS4"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'C_Rect_L33.0mm_W15.0mm_P27.50mm_MKS4', 'description': 'C, Rect series, Radial, pin pitch=27.50mm, , length*width=33*15mm^2, Capacitor, http://www.wima.com/EN/WIMA_MKS_4.pdf', 'tags': 'C Rect series Radial pin pitch 27.50mm  length 33mm width 15mm Capacitor', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Capacitor_THT.3dshapes/C_Rect_L33.0mm_W15.0mm_P27.50mm_MKS4.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Capacitor_THT : C_Rect_L33.0mm_W15.0mm_P27.50mm_MKS4')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

