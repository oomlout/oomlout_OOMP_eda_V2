
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SO"
    oIndex = "SSOP-20_5.3x7.2mm_P0.65mm"
    hexID = "FZKSOSS253X72P65"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SSOP-20_5.3x7.2mm_P0.65mm', 'description': 'SSOP, 20 Pin (http://ww1.microchip.com/downloads/en/DeviceDoc/40001800C.pdf), generated with kicad-footprint-generator ipc_gullwing_generator.py', 'tags': 'SSOP SO', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/SSOP-20_5.3x7.2mm_P0.65mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_SO : SSOP-20_5.3x7.2mm_P0.65mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

