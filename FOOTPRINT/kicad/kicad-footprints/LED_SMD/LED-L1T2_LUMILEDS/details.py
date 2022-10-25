
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "LED_SMD"
    oIndex = "LED-L1T2_LUMILEDS"
    hexID = "FZKLSMLL1T2LUMS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'LED-L1T2_LUMILEDS', 'description': 'http://www.lumileds.com/uploads/438/DS133-pdf', 'tags': 'LUMILEDS LUXEON TX L1T2 LED', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/LED_SMD.3dshapes/LED-L1T2_LUMILEDS.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('LED_SMD : LED-L1T2_LUMILEDS')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

