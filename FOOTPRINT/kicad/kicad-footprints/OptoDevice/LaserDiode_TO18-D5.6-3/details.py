
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "OptoDevice"
    oIndex = "LaserDiode_TO18-D5.6-3"
    hexID = "FZKOPLASERDIODETO18D563"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'LaserDiode_TO18-D5.6-3', 'description': 'Laser Diode, TO18-like (D=5.6mm), 3pin', 'tags': 'Laser Diode TO18-like', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/OptoDevice.3dshapes/LaserDiode_TO18-D5.6-3.wrl', 'pins': {'type': 'thru_hole', 'shape': 'roundrect'}})
    newPart['name'].append('OptoDevice : LaserDiode_TO18-D5.6-3')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

