
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_CSP"
    oIndex = "LFCSP-16-1EP_3x3mm_P0.5mm_EP1.3x1.3mm_ThermalVias"
    hexID = "FZKCSPLFCSP161EP3X3P5EP13X13THERMALVIAS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'LFCSP-16-1EP_3x3mm_P0.5mm_EP1.3x1.3mm_ThermalVias', 'description': 'LFCSP, 16 Pin (https://www.analog.com/media/en/package-pcb-resources/package/pkg_pdf/lfcspcp/cp-16/CP_16_21.pdf), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'LFCSP NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_CSP.3dshapes/LFCSP-16-1EP_3x3mm_P0.5mm_EP1.3x1.3mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_CSP : LFCSP-16-1EP_3x3mm_P0.5mm_EP1.3x1.3mm_ThermalVias')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

