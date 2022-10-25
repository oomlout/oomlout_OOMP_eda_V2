
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "RF_Module"
    oIndex = "nRF24L01_Breakout"
    hexID = "FZKRFMONRF24L1BREAKOUT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'nRF24L01_Breakout', 'description': 'nRF24L01 breakout board', 'tags': 'nRF24L01 adapter breakout', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/RF_Module.3dshapes/nRF24L01_Breakout.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('RF_Module : nRF24L01_Breakout')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

