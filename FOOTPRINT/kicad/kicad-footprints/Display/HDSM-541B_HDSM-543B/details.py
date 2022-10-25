
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Display"
    oIndex = "HDSM-541B_HDSM-543B"
    hexID = "FZKDIHDSM541BHDSM543B"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'HDSM-541B_HDSM-543B', 'description': '2 digit 7 segement blue LED with right hand decimal, https://docs.broadcom.com/docs/AV02-1588EN', 'tags': '2 digit 7 segement blue LED with right hand decimal', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Display.3dshapes/HDSM-541B_HDSM-543B.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Display : HDSM-541B_HDSM-543B')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

