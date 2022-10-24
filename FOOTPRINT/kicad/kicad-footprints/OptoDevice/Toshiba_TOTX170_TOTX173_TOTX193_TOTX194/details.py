
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "OptoDevice"
    oIndex = "Toshiba_TOTX170_TOTX173_TOTX193_TOTX194"
    hexID = "FZKOPTOSHIBATOTX17TOTX173TOTX193TOTX194"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Toshiba_TOTX170_TOTX173_TOTX193_TOTX194', 'description': 'Fiberoptic Reciver, RX, Toshiba, Toslink, TORX170, TORX173, TORX193, TORX194', 'tags': 'Fiberoptic Reciver RX Toshiba Toslink TORX170 TORX173 TORX193 TORX194', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/OptoDevice.3dshapes/Toshiba_TOTX170_TOTX173_TOTX193_TOTX194.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('OptoDevice : Toshiba_TOTX170_TOTX173_TOTX193_TOTX194')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

