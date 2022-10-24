
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SO"
    oIndex = "SO-8_3.9x4.9mm_P1.27mm"
    hexID = "FZKSOSO839X49P127"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SO-8_3.9x4.9mm_P1.27mm', 'description': 'SO, 8 Pin (https://www.nxp.com/docs/en/data-sheet/PCF8523.pdf), generated with kicad-footprint-generator ipc_gullwing_generator.py', 'tags': 'SO SO', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/SO-8_3.9x4.9mm_P1.27mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_SO : SO-8_3.9x4.9mm_P1.27mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

