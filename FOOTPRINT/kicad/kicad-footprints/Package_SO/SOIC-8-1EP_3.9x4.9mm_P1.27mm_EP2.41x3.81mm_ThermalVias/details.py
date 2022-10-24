
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SO"
    oIndex = "SOIC-8-1EP_3.9x4.9mm_P1.27mm_EP2.41x3.81mm_ThermalVias"
    hexID = "FZKSOSOIC81EP39X49P127EP241X381THERMALVIAS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SOIC-8-1EP_3.9x4.9mm_P1.27mm_EP2.41x3.81mm_ThermalVias', 'description': 'SOIC, 8 Pin (https://www.analog.com/media/en/technical-documentation/data-sheets/ada4898-1_4898-2.pdf#page=29), generated with kicad-footprint-generator ipc_gullwing_generator.py', 'tags': 'SOIC SO', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/SOIC-8-1EP_3.9x4.9mm_P1.27mm_EP2.41x3.81mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_SO : SOIC-8-1EP_3.9x4.9mm_P1.27mm_EP2.41x3.81mm_ThermalVias')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

