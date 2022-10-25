
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "OptoDevice"
    oIndex = "LaserDiode_TO5-D9-3"
    hexID = "FZKOPLASERDIODETO5D93"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'LaserDiode_TO5-D9-3', 'description': 'Laser Diode, TO5-like (D=9mm), 3pin', 'tags': 'Laser Diode TO5-like', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/OptoDevice.3dshapes/LaserDiode_TO5-D9-3.wrl', 'pins': {'type': 'thru_hole', 'shape': 'roundrect'}})
    newPart['name'].append('OptoDevice : LaserDiode_TO5-D9-3')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

