
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Display"
    oIndex = "HDSM-441B_HDSM-443B"
    hexID = "FZKDIHDSM441BHDSM443B"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'HDSM-441B_HDSM-443B', 'description': '2 Digit 7 segemnt blue LED, right hand decimal, https://docs.broadcom.com/docs/AV02-1589EN', 'tags': '2 Digit 7 segment blue LED', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Display.3dshapes/HDSM-441B_HDSM-443B.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Display : HDSM-441B_HDSM-443B')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

