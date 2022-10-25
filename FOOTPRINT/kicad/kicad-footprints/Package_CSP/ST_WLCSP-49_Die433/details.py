
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_CSP"
    oIndex = "ST_WLCSP-49_Die433"
    hexID = "FZKCSPSTWLCSP49DIE433"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'ST_WLCSP-49_Die433', 'description': 'WLCSP-49, 7x7 raster, 3.029x3.029mm package, pitch 0.4mm; see section 7.1.1 of http://www.st.com/resource/en/datasheet/stm32f401ce.pdf', 'tags': 'BGA 49 0.4', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_CSP.3dshapes/ST_WLCSP-49_Die433.wrl', 'pins': {'type': 'smd', 'shape': 'circle'}})
    newPart['name'].append('Package_CSP : ST_WLCSP-49_Die433')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

