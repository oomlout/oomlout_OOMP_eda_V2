
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Diode_SMD"
    oIndex = "Diode_Bridge_OnSemi_SDIP-4L"
    hexID = "FZKDIODESMDIODEBRIDGEONSEMISDIP4L"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Diode_Bridge_OnSemi_SDIP-4L', 'description': 'SMD diode bridge OnSemi SDIP-4L, see https://www.onsemi.com/pdf/datasheet/df10s1-d.pdf', 'tags': 'OnSemi Diode Bridge SDIP-4L', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Diode_SMD.3dshapes/Diode_Bridge_OnSemi_SDIP-4L.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Diode_SMD : Diode_Bridge_OnSemi_SDIP-4L')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

