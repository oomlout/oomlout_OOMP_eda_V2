
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Filter"
    oIndex = "Filter_Schaffner_FN406"
    hexID = "FZKFILFILSCHAFFNERFN46"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Filter_Schaffner_FN406', 'description': 'Ultra Compact EMC Filter (https://www.schaffner.com/products/download/product/datasheet/fn-406-ultra-compact-emc-filter/)', 'tags': 'emi filter', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Filter.3dshapes/Filter_Schaffner_FN406.wrl', 'pins': {'type': 'thru_hole', 'shape': 'roundrect'}})
    newPart['name'].append('Filter : Filter_Schaffner_FN406')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

