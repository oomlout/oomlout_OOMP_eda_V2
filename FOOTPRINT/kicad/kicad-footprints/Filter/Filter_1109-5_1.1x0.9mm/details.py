
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Filter"
    oIndex = "Filter_1109-5_1.1x0.9mm"
    hexID = "FZKFILFIL119511X9"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Filter_1109-5_1.1x0.9mm', 'description': '5-pin SAW filter package - 1.1x0.9 mm Body; (see https://www.murata.com/~/media/webrenewal/support/library/catalog/products/filter/rf/p73e.ashx?la=en-gb)', 'tags': 'Filter 5', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Filter.3dshapes/Filter_1109-5_1.1x0.9mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Filter : Filter_1109-5_1.1x0.9mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

