
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "OptoDevice"
    oIndex = "Toshiba_TORX170_TORX173_TORX193_TORX194"
    hexID = "FZKOPTOSHIBATORX17TORX173TORX193TORX194"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Toshiba_TORX170_TORX173_TORX193_TORX194', 'description': 'Fiberoptic Reciver, RX, Toshiba, Toslink, TORX170, TORX173, TORX193, TORX194', 'tags': 'Fiberoptic Reciver RX Toshiba Toslink TORX170 TORX173 TORX193 TORX194', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/OptoDevice.3dshapes/Toshiba_TORX170_TORX173_TORX193_TORX194.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('OptoDevice : Toshiba_TORX170_TORX173_TORX193_TORX194')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

