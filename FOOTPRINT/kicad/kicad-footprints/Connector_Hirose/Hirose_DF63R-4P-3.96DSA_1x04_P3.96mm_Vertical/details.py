
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Hirose"
    oIndex = "Hirose_DF63R-4P-3.96DSA_1x04_P3.96mm_Vertical"
    hexID = "FZKCNHIROSEHIROSEDF63R4P396DSA1X4P396VERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Hirose_DF63R-4P-3.96DSA_1x04_P3.96mm_Vertical', 'description': 'Hirose DF63 through hole, DF63R-4P-3.96DSA, 4 Pins per row (https://www.hirose.com/product/en/products/DF63/), generated with kicad-footprint-generator', 'tags': 'connector Hirose DF63 vertical', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Hirose.3dshapes/Hirose_DF63R-4P-3.96DSA_1x04_P3.96mm_Vertical.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_Hirose : Hirose_DF63R-4P-3.96DSA_1x04_P3.96mm_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

