
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "QFN-24-1EP_3x4mm_P0.4mm_EP1.65x2.65mm_ThermalVias"
    hexID = "FZKDFNQFN241EP3X4P4EP165X265THERMALVIAS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'QFN-24-1EP_3x4mm_P0.4mm_EP1.65x2.65mm_ThermalVias', 'description': 'QFN, 24 Pin (http://www.analog.com/media/en/package-pcb-resources/package/pkg_pdf/ltc-legacy-qfn/QFN_20_05-08-1742.pdf), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'QFN NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/QFN-24-1EP_3x4mm_P0.4mm_EP1.65x2.65mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_DFN_QFN : QFN-24-1EP_3x4mm_P0.4mm_EP1.65x2.65mm_ThermalVias')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

