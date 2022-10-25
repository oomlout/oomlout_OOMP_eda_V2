
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector"
    oIndex = "GB042-34S-H10"
    hexID = "FZKCNGB4234SH1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'GB042-34S-H10', 'description': 'http://www.lsmtron.com/pdf/Connector&Antenna_catalog.PDF', 'tags': '34pin SMD connector ', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector.3dshapes/GB042-34S-H10.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Connector : GB042-34S-H10')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

