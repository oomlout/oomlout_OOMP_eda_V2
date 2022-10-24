
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SO"
    oIndex = "MSOP-8-1EP_3x3mm_P0.65mm_EP1.95x2.15mm_ThermalVias"
    hexID = "FZKSOMS81EP3X3P65EP195X215THERMALVIAS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'MSOP-8-1EP_3x3mm_P0.65mm_EP1.95x2.15mm_ThermalVias', 'description': 'MSOP, 8 Pin (http://www.st.com/resource/en/datasheet/pm8834.pdf), generated with kicad-footprint-generator ipc_gullwing_generator.py', 'tags': 'MSOP SO', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/MSOP-8-1EP_3x3mm_P0.65mm_EP1.95x2.15mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_SO : MSOP-8-1EP_3x3mm_P0.65mm_EP1.95x2.15mm_ThermalVias')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

