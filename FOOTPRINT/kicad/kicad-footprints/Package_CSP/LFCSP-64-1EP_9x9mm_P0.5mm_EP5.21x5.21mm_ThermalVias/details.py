
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_CSP"
    oIndex = "LFCSP-64-1EP_9x9mm_P0.5mm_EP5.21x5.21mm_ThermalVias"
    hexID = "FZKCSPLFCSP641EP9X9P5EP521X521THERMALVIAS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'LFCSP-64-1EP_9x9mm_P0.5mm_EP5.21x5.21mm_ThermalVias', 'description': 'LFCSP, 64 Pin (https://www.analog.com/media/en/package-pcb-resources/package/pkg_pdf/lfcspcp/cp_64_7.pdf), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'LFCSP NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_CSP.3dshapes/LFCSP-64-1EP_9x9mm_P0.5mm_EP5.21x5.21mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_CSP : LFCSP-64-1EP_9x9mm_P0.5mm_EP5.21x5.21mm_ThermalVias')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

