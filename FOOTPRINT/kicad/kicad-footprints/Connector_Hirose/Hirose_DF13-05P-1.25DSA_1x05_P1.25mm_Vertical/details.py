
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Hirose"
    oIndex = "Hirose_DF13-05P-1.25DSA_1x05_P1.25mm_Vertical"
    hexID = "FZKCNHIROSEHIROSEDF135P125DSA1X5P125VERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Hirose_DF13-05P-1.25DSA_1x05_P1.25mm_Vertical', 'description': 'Hirose DF13 through hole, DF13-05P-1.25DSA, 5 Pins per row (https://www.hirose.com/product/en/products/DF13/DF13-2P-1.25DSA%2850%29/), generated with kicad-footprint-generator', 'tags': 'connector Hirose DF13 vertical', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Hirose.3dshapes/Hirose_DF13-05P-1.25DSA_1x05_P1.25mm_Vertical.wrl', 'pins': {'type': 'thru_hole', 'shape': 'roundrect'}})
    newPart['name'].append('Connector_Hirose : Hirose_DF13-05P-1.25DSA_1x05_P1.25mm_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

