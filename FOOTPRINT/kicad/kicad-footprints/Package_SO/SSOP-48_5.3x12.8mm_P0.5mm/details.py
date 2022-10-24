
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SO"
    oIndex = "SSOP-48_5.3x12.8mm_P0.5mm"
    hexID = "FZKSOSS4853X128P5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SSOP-48_5.3x12.8mm_P0.5mm', 'description': 'SSOP, 48 Pin (https://www.analog.com/media/en/package-pcb-resources/package/pkg_pdf/ltc-legacy-ssop/05081887_A_G48.pdf), generated with kicad-footprint-generator ipc_gullwing_generator.py', 'tags': 'SSOP SO', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/SSOP-48_5.3x12.8mm_P0.5mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_SO : SSOP-48_5.3x12.8mm_P0.5mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

