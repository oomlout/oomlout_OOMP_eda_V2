
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Crystal"
    oIndex = "Crystal_C38-LF_D3.0mm_L8.0mm_Horizontal_1EP_style1"
    hexID = "FZKXXC38LFD3L8HORIZONTAL1EPSTYLE1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Crystal_C38-LF_D3.0mm_L8.0mm_Horizontal_1EP_style1', 'description': 'Crystal THT C38-LF 8.0mm length 3.0mm diameter', 'tags': "['C38-LF']", 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Crystal.3dshapes/Crystal_C38-LF_D3.0mm_L8.0mm_Horizontal_1EP_style1.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Crystal : Crystal_C38-LF_D3.0mm_L8.0mm_Horizontal_1EP_style1')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

