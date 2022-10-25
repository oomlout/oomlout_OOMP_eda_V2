
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "OptoDevice"
    oIndex = "Vishay_MINICAST-3Pin"
    hexID = "FZKOPVISHAYMCAST3PIN"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Vishay_MINICAST-3Pin', 'description': 'IR Receiver Vishay TSOP-xxxx, MINICAST package, see https://www.vishay.com/docs/82669/tsop32s40f.pdf', 'tags': 'IR Receiver Vishay TSOP-xxxx MINICAST', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/OptoDevice.3dshapes/Vishay_MINICAST-3Pin.wrl', 'pins': {'type': 'thru_hole', 'shape': 'roundrect'}})
    newPart['name'].append('OptoDevice : Vishay_MINICAST-3Pin')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

