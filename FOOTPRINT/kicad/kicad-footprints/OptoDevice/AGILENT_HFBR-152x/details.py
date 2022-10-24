
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "OptoDevice"
    oIndex = "AGILENT_HFBR-152x"
    hexID = "FZKOPAGILENTHFBR152X"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'AGILENT_HFBR-152x', 'description': 'Fiberoptic Transmitter TX, HFBR series (https://docs.broadcom.com/docs/AV02-3283EN)', 'tags': 'Fiberoptic Transmitter', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/OptoDevice.3dshapes/AGILENT_HFBR-152x.wrl', 'pins': {'type': 'thru_hole', 'shape': 'roundrect'}})
    newPart['name'].append('OptoDevice : AGILENT_HFBR-152x')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

