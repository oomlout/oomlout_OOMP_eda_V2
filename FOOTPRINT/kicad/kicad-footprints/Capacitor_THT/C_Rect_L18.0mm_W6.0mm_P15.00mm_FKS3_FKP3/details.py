
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Capacitor_THT"
    oIndex = "C_Rect_L18.0mm_W6.0mm_P15.00mm_FKS3_FKP3"
    hexID = "FZKCCRECTL18W6P15FKS3FKP3"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'C_Rect_L18.0mm_W6.0mm_P15.00mm_FKS3_FKP3', 'description': 'C, Rect series, Radial, pin pitch=15.00mm, , length*width=18*6mm^2, Capacitor, http://www.wima.com/EN/WIMA_FKS_3.pdf', 'tags': 'C Rect series Radial pin pitch 15.00mm  length 18mm width 6mm Capacitor', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Capacitor_THT.3dshapes/C_Rect_L18.0mm_W6.0mm_P15.00mm_FKS3_FKP3.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Capacitor_THT : C_Rect_L18.0mm_W6.0mm_P15.00mm_FKS3_FKP3')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

