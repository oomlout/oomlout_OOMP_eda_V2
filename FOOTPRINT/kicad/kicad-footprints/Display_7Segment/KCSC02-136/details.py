
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Display_7Segment"
    oIndex = "KCSC02-136"
    hexID = "FZKDI7SKCSC2136"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'KCSC02-136', 'description': 'http://www.kingbright.com/attachments/file/psearch/000/00/00/KCSC02-136(Ver.6B).pdf', 'tags': 'Single digit 7 segement super bright yellow LED', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Display_7Segment.3dshapes/KCSC02-136.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Display_7Segment : KCSC02-136')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

