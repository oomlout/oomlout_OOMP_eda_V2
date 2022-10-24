
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "OptoDevice"
    oIndex = "Maxim_OLGA-14_3.3x5.6mm_P0.8mm"
    hexID = "FZKOPMAXIMOLGA1433X56P8"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Maxim_OLGA-14_3.3x5.6mm_P0.8mm', 'description': 'https://pdfserv.maximintegrated.com/land_patterns/90-0602.PDF', 'tags': 'OLGA-14 OESIP-14', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/OptoDevice.3dshapes/Maxim_OLGA-14_3.3x5.6mm_P0.8mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('OptoDevice : Maxim_OLGA-14_3.3x5.6mm_P0.8mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

