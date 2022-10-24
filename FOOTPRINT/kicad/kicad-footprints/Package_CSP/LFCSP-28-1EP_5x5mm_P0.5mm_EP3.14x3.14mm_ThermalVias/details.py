
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_CSP"
    oIndex = "LFCSP-28-1EP_5x5mm_P0.5mm_EP3.14x3.14mm_ThermalVias"
    hexID = "FZKCSPLFCSP281EP5X5P5EP314X314THERMALVIAS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'LFCSP-28-1EP_5x5mm_P0.5mm_EP3.14x3.14mm_ThermalVias', 'description': 'LFCSP, 28 Pin (https://www.analog.com/media/en/package-pcb-resources/package/pkg_pdf/lfcspcp/cp-28/CP_28_10.pdf), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'LFCSP NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_CSP.3dshapes/LFCSP-28-1EP_5x5mm_P0.5mm_EP3.14x3.14mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_CSP : LFCSP-28-1EP_5x5mm_P0.5mm_EP3.14x3.14mm_ThermalVias')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

