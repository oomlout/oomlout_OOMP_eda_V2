
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_CSP"
    oIndex = "LFCSP-8-1EP_3x3mm_P0.5mm_EP1.6x2.34mm_ThermalVias"
    hexID = "FZKCSPLFCSP81EP3X3P5EP16X234THERMALVIAS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'LFCSP-8-1EP_3x3mm_P0.5mm_EP1.6x2.34mm_ThermalVias', 'description': 'LFCSP, 8 Pin (https://www.analog.com/media/en/package-pcb-resources/package/pkg_pdf/lfcspcp/CP_8_11.pdf), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'LFCSP NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_CSP.3dshapes/LFCSP-8-1EP_3x3mm_P0.5mm_EP1.6x2.34mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_CSP : LFCSP-8-1EP_3x3mm_P0.5mm_EP1.6x2.34mm_ThermalVias')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

