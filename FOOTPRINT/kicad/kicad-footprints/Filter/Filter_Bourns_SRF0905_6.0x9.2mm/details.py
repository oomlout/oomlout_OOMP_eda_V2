
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Filter"
    oIndex = "Filter_Bourns_SRF0905_6.0x9.2mm"
    hexID = "FZKFILFILBOURNSSRF956X92"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Filter_Bourns_SRF0905_6.0x9.2mm', 'description': 'https://www.bourns.com/docs/Product-Datasheets/SRF0905.pdf', 'tags': 'Line Filter', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Filter.3dshapes/Filter_Bourns_SRF0905_6.0x9.2mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Filter : Filter_Bourns_SRF0905_6.0x9.2mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

