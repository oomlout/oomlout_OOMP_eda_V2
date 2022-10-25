
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Hirose"
    oIndex = "Hirose_DF13-15P-1.25DS_1x15_P1.25mm_Horizontal"
    hexID = "FZKCNHIROSEHIROSEDF1315P125DS1X15P125HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Hirose_DF13-15P-1.25DS_1x15_P1.25mm_Horizontal', 'description': 'Hirose DF13 through hole, DF13-15P-1.25DS, 15 Pins per row (https://www.hirose.com/product/en/products/DF13/DF13-4P-1.25DS%2820%29/), generated with kicad-footprint-generator', 'tags': 'connector Hirose DF13 horizontal', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Hirose.3dshapes/Hirose_DF13-15P-1.25DS_1x15_P1.25mm_Horizontal.wrl', 'pins': {'type': 'thru_hole', 'shape': 'roundrect'}})
    newPart['name'].append('Connector_Hirose : Hirose_DF13-15P-1.25DS_1x15_P1.25mm_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

