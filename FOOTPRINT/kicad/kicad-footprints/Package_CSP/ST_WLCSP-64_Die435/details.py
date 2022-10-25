
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_CSP"
    oIndex = "ST_WLCSP-64_Die435"
    hexID = "FZKCSPSTWLCSP64DIE435"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'ST_WLCSP-64_Die435', 'description': 'WLCSP-64, 8x8 raster, 3.141x3.127mm package, pitch 0.35mm; see section 7.5 of http://www.st.com/resource/en/datasheet/DM00257211.pdf', 'tags': 'BGA 64 0.35', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_CSP.3dshapes/ST_WLCSP-64_Die435.wrl', 'pins': {'type': 'smd', 'shape': 'circle'}})
    newPart['name'].append('Package_CSP : ST_WLCSP-64_Die435')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

