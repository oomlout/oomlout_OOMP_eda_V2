
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_TO_SOT_THT"
    oIndex = "TO-46-3_Pin2Center_Window"
    hexID = "FZKSOTTO463PIN2CENTERWINDOW"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TO-46-3_Pin2Center_Window', 'description': 'TO-46-3, Pin2 at center of package, Thorlabs photodiodes, https://www.thorlabs.de/drawings/374b6862eb3b5a04-9360B5F6-5056-2306-D912111C06C3F830/FDGA05-SpecSheet.pdf', 'tags': 'TO-46-3 Thorlabs', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_TO_SOT_THT.3dshapes/TO-46-3_Pin2Center_Window.wrl', 'pins': {'type': 'thru_hole', 'shape': 'oval'}})
    newPart['name'].append('Package_TO_SOT_THT : TO-46-3_Pin2Center_Window')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

