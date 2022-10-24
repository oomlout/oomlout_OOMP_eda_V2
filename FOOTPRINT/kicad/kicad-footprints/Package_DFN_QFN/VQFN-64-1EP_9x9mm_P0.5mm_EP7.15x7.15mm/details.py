
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "VQFN-64-1EP_9x9mm_P0.5mm_EP7.15x7.15mm"
    hexID = "FZKDFNVQFN641EP9X9P5EP715X715"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'VQFN-64-1EP_9x9mm_P0.5mm_EP7.15x7.15mm', 'description': 'VQFN, 64 Pin (http://ww1.microchip.com/downloads/en/DeviceDoc/64L_QFN_9x9_MR_C04-00149e.pdf), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'VQFN NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/VQFN-64-1EP_9x9mm_P0.5mm_EP7.15x7.15mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_DFN_QFN : VQFN-64-1EP_9x9mm_P0.5mm_EP7.15x7.15mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

