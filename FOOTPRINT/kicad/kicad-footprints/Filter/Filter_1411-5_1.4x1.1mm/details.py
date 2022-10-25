
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Filter"
    oIndex = "Filter_1411-5_1.4x1.1mm"
    hexID = "FZKFILFIL1411514X11"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Filter_1411-5_1.4x1.1mm', 'description': '5-pin filter package - 1.4x1.1 mm Body; (see https://global.kyocera.com/prdct/electro/product/pdf/sf14_tdlte.pdf)', 'tags': 'Filter 5', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Filter.3dshapes/Filter_1411-5_1.4x1.1mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Filter : Filter_1411-5_1.4x1.1mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

