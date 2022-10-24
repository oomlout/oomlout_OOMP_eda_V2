
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_CSP"
    oIndex = "LFCSP-WD-10-1EP_3x3mm_P0.5mm_EP1.64x2.38mm_ThermalVias"
    hexID = "FZKCSPLFCSPWD11EP3X3P5EP164X238THERMALVIAS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'LFCSP-WD-10-1EP_3x3mm_P0.5mm_EP1.64x2.38mm_ThermalVias', 'description': 'LFCSP-WD, 10 Pin (https://www.analog.com/media/en/package-pcb-resources/package/pkg_pdf/lfcspcp/cp-10/CP_10_9.pdf), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'LFCSP-WD NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_CSP.3dshapes/LFCSP-WD-10-1EP_3x3mm_P0.5mm_EP1.64x2.38mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_CSP : LFCSP-WD-10-1EP_3x3mm_P0.5mm_EP1.64x2.38mm_ThermalVias')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

