
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SO"
    oIndex = "SOP-8-1EP_4.57x4.57mm_P1.27mm_EP4.57x4.45mm_ThermalVias"
    hexID = "FZKSOS81EP457X457P127EP457X445THERMALVIAS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SOP-8-1EP_4.57x4.57mm_P1.27mm_EP4.57x4.45mm_ThermalVias', 'description': 'SOP, 8 Pin (https://ww2.minicircuits.com/case_style/XX112.pdf), generated with kicad-footprint-generator ipc_gullwing_generator.py', 'tags': 'SOP SO', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/SOP-8-1EP_4.57x4.57mm_P1.27mm_EP4.57x4.45mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_SO : SOP-8-1EP_4.57x4.57mm_P1.27mm_EP4.57x4.45mm_ThermalVias')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

