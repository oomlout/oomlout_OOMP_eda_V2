
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SO"
    oIndex = "HTSSOP-28-1EP_4.4x9.7mm_P0.65mm_EP2.85x5.4mm_ThermalVias"
    hexID = "FZKSOHTSS281EP44X97P65EP285X54THERMALVIAS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'HTSSOP-28-1EP_4.4x9.7mm_P0.65mm_EP2.85x5.4mm_ThermalVias', 'description': 'HTSSOP, 28 Pin (https://pdfserv.maximintegrated.com/package_dwgs/21-0108.PDF), generated with kicad-footprint-generator ipc_gullwing_generator.py', 'tags': 'HTSSOP SO', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/HTSSOP-28-1EP_4.4x9.7mm_P0.65mm_EP2.85x5.4mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_SO : HTSSOP-28-1EP_4.4x9.7mm_P0.65mm_EP2.85x5.4mm_ThermalVias')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

