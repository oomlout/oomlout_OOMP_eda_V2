
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DirectFET"
    oIndex = "DirectFET_SC"
    hexID = "FZKDFETDIRECTFETSC"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'DirectFET_SC', 'description': 'DirectFET SC https://www.infineon.com/dgdl/Infineon-AN-1035-ApplicationNotes-v29_01-EN.pdf?fileId=5546d462533600a40153559159020f76#page=24', 'tags': 'DirectFET SC MOSFET Infineon', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DirectFET.3dshapes/DirectFET_SC.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_DirectFET : DirectFET_SC')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

