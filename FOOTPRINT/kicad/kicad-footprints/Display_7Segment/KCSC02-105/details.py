
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Display_7Segment"
    oIndex = "KCSC02-105"
    hexID = "FZKDI7SKCSC215"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'KCSC02-105', 'description': 'http://www.kingbright.com/attachments/file/psearch/000/00/00/KCSC02-105(Ver.9A).pdf', 'tags': 'Single digit 7 segement hyper red LED', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Display_7Segment.3dshapes/KCSC02-105.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Display_7Segment : KCSC02-105')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

