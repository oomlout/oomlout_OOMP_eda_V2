
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_CSP"
    oIndex = "ST_WLCSP-25_Die425"
    hexID = "FZKCSPSTWLCSP25DIE425"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'ST_WLCSP-25_Die425', 'description': 'WLCSP-25, 5x5 raster, 2.097x2.493mm package, pitch 0.4mm; see section 7.6 of http://www.st.com/resource/en/datasheet/stm32l031f6.pdf', 'tags': 'BGA 25 0.4', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_CSP.3dshapes/ST_WLCSP-25_Die425.wrl', 'pins': {'type': 'smd', 'shape': 'circle'}})
    newPart['name'].append('Package_CSP : ST_WLCSP-25_Die425')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

