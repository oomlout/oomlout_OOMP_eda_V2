
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Module"
    oIndex = "Carambola2"
    hexID = "FZKMOCARAMBOLA2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Carambola2', 'description': '8devices Carambola2, OpenWRT, industrial SoM computer, https://www.8devices.com/media/products/carambola2/downloads/carambola2-datasheet.pdf', 'tags': 'carambola2 8devices', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Module.3dshapes/Carambola2.wrl', 'pins': {'type': 'smd', 'shape': 'custom'}})
    newPart['name'].append('Module : Carambola2')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

