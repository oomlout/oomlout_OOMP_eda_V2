
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Crystal"
    oIndex = "Crystal_C26-LF_D2.1mm_L6.5mm_Horizontal_1EP_style2"
    hexID = "FZKXXC26LFD21L65HORIZONTAL1EPSTYLE2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Crystal_C26-LF_D2.1mm_L6.5mm_Horizontal_1EP_style2', 'description': 'Crystal THT C26-LF 6.5mm length 2.06mm diameter', 'tags': "['C26-LF']", 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Crystal.3dshapes/Crystal_C26-LF_D2.1mm_L6.5mm_Horizontal_1EP_style2.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Crystal : Crystal_C26-LF_D2.1mm_L6.5mm_Horizontal_1EP_style2')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

