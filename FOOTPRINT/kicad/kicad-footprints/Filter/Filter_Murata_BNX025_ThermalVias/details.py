
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Filter"
    oIndex = "Filter_Murata_BNX025_ThermalVias"
    hexID = "FZKFILFILMBNX25THERMALVIAS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Filter_Murata_BNX025_ThermalVias', 'description': 'https://www.murata.com/en-us/products/productdata/8796778004510/QNFH9101.pdf?1496719830000', 'tags': 'EMI Filter', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Filter.3dshapes/Filter_Murata_BNX025.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Filter : Filter_Murata_BNX025_ThermalVias')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

