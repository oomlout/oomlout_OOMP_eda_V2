
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Crystal"
    oIndex = "Crystal_HC52-8mm_Horizontal_1EP_style2"
    hexID = "FZKXXHC528HORIZONTAL1EPSTYLE2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Crystal_HC52-8mm_Horizontal_1EP_style2', 'description': 'Crystal THT HC-51/8mm http://www.kvg-gmbh.de/assets/uploads/files/product_pdfs/XS71xx.pdf', 'tags': 'THT crystal', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Crystal.3dshapes/Crystal_HC52-8mm_Horizontal_1EP_style2.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Crystal : Crystal_HC52-8mm_Horizontal_1EP_style2')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

