
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "DFN-6-1EP_2x2mm_P0.5mm_EP0.6x1.37mm"
    hexID = "FZKDFNDFN61EP2X2P5EP6X137"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'DFN-6-1EP_2x2mm_P0.5mm_EP0.6x1.37mm', 'description': 'DFN, 6 Pin (https://www.analog.com/media/en/package-pcb-resources/package/pkg_pdf/ltc-legacy-dfn/05081703_C_DC6.pdf), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'DFN NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/DFN-6-1EP_2x2mm_P0.5mm_EP0.6x1.37mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_DFN_QFN : DFN-6-1EP_2x2mm_P0.5mm_EP0.6x1.37mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

