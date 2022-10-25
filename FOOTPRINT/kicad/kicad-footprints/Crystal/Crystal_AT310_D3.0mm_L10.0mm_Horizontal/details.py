
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Crystal"
    oIndex = "Crystal_AT310_D3.0mm_L10.0mm_Horizontal"
    hexID = "FZKXXAT31D3L1HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Crystal_AT310_D3.0mm_L10.0mm_Horizontal', 'description': 'Crystal THT AT310 10.0mm-10.5mm length 3.0mm diameter http://www.cinetech.com.tw/upload/2011/04/20110401165201.pdf', 'tags': "['AT310']", 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Crystal.3dshapes/Crystal_AT310_D3.0mm_L10.0mm_Horizontal.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Crystal : Crystal_AT310_D3.0mm_L10.0mm_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

