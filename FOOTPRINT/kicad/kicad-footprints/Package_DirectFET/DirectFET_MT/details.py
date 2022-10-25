
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DirectFET"
    oIndex = "DirectFET_MT"
    hexID = "FZKDFETDIRECTFETMT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'DirectFET_MT', 'description': 'DirectFET MT https://www.infineon.com/dgdl/Infineon-AN-1035-ApplicationNotes-v29_01-EN.pdf?fileId=5546d462533600a40153559159020f76#page=26', 'tags': 'DirectFET MT MOSFET Infineon', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DirectFET.3dshapes/DirectFET_MT.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_DirectFET : DirectFET_MT')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

