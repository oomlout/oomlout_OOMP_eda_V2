
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "RF_Module"
    oIndex = "ZETA-433-SO_THT"
    hexID = "FZKRFMOZETA433SOTHT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'ZETA-433-SO_THT', 'description': 'RF transceiver THT style https://www.rfsolutions.co.uk/downloads/1456219226DS-ZETA.pdf', 'tags': 'RF transceiver SMD style', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/RF_Module.3dshapes/ZETA-433-SO_THT.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('RF_Module : ZETA-433-SO_THT')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

