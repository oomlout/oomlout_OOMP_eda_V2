
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SO"
    oIndex = "TSSOP-16-1EP_4.4x5mm_P0.65mm_EP3x3mm_ThermalVias"
    hexID = "FZKSOTSS161EP44X5P65EP3X3THERMALVIAS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TSSOP-16-1EP_4.4x5mm_P0.65mm_EP3x3mm_ThermalVias', 'description': 'TSSOP, 16 Pin (Allegro A4954 https://www.allegromicro.com/-/media/Files/Datasheets/A4954-Datasheet.ashx), generated with kicad-footprint-generator ipc_gullwing_generator.py', 'tags': 'TSSOP SO', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/TSSOP-16-1EP_4.4x5mm_P0.65mm_EP3x3mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_SO : TSSOP-16-1EP_4.4x5mm_P0.65mm_EP3x3mm_ThermalVias')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

