
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "OptoDevice"
    oIndex = "Vishay_CAST-3Pin"
    hexID = "FZKOPVISHAYCAST3PIN"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Vishay_CAST-3Pin', 'description': 'IR Receiver Vishay TSOP-xxxx, CAST package, see https://www.vishay.com/docs/82493/tsop311.pdf', 'tags': 'IRReceiverVishayTSOP-xxxx CAST', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/OptoDevice.3dshapes/Vishay_CAST-3Pin.wrl', 'pins': {'type': 'thru_hole', 'shape': 'roundrect'}})
    newPart['name'].append('OptoDevice : Vishay_CAST-3Pin')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

