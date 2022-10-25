
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Module"
    oIndex = "Arduino_UNO_R2"
    hexID = "FZKMOARDUNOR2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Arduino_UNO_R2', 'description': 'Arduino UNO R2, http://www.mouser.com/pdfdocs/Gravitech_Arduino_Nano3_0.pdf', 'tags': 'Arduino UNO R2', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Module.3dshapes/Arduino_UNO_R2.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Module : Arduino_UNO_R2')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

