
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Display_7Segment"
    oIndex = "7SEGMENT-LED__HDSM531_HDSM533_SMD"
    hexID = "FZKDI7S7SLHDSM531HDSM533SM"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': '7SEGMENT-LED__HDSM531_HDSM533_SMD', 'description': '7-Segment Display, HDSM53x, https://docs.broadcom.com/docs/AV02-0713EN', 'tags': '7segment LED HDSM531 HDSM533', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Display_7Segment.3dshapes/7SEGMENT-LED__HDSM531_HDSM533_SMD.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Display_7Segment : 7SEGMENT-LED__HDSM531_HDSM533_SMD')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

