
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Module"
    oIndex = "BeagleBoard_PocketBeagle"
    hexID = "FZKMOBEAGLEBOARDPOCKETBEAGLE"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'BeagleBoard_PocketBeagle', 'description': 'PocketBeagle, https://github.com/beagleboard/pocketbeagle/wiki/System-Reference-Manual#71_Expansion_Header_Connectors', 'tags': 'PocketBeagle', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Module.3dshapes/BeagleBoard_PocketBeagle.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Module : BeagleBoard_PocketBeagle')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

