
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_CSP"
    oIndex = "LFCSP-8-1EP_3x3mm_P0.5mm_EP1.45x1.74mm"
    hexID = "FZKCSPLFCSP81EP3X3P5EP145X174"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'LFCSP-8-1EP_3x3mm_P0.5mm_EP1.45x1.74mm', 'description': 'LFCSP, 8 Pin (https://www.analog.com/media/en/package-pcb-resources/package/pkg_pdf/lfcspcp/cp-8/CP_8_13.pdf), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'LFCSP NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_CSP.3dshapes/LFCSP-8-1EP_3x3mm_P0.5mm_EP1.45x1.74mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_CSP : LFCSP-8-1EP_3x3mm_P0.5mm_EP1.45x1.74mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

