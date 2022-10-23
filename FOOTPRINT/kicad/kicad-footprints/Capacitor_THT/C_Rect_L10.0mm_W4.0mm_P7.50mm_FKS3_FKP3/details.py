
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Capacitor_THT"
    oIndex = "C_Rect_L10.0mm_W4.0mm_P7.50mm_FKS3_FKP3"
    hexID = "FZKCCRECTL1W4P75FKS3FKP3"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'C_Rect_L10.0mm_W4.0mm_P7.50mm_FKS3_FKP3', 'description': 'C, Rect series, Radial, pin pitch=7.50mm, , length*width=10*4mm^2, Capacitor, http://www.wima.com/EN/WIMA_FKS_3.pdf', 'tags': 'C Rect series Radial pin pitch 7.50mm  length 10mm width 4mm Capacitor', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Capacitor_THT.3dshapes/C_Rect_L10.0mm_W4.0mm_P7.50mm_FKS3_FKP3.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Capacitor_THT : C_Rect_L10.0mm_W4.0mm_P7.50mm_FKS3_FKP3')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

