
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "UQFN-20-1EP_3x3mm_P0.4mm_EP1.85x1.85mm"
    hexID = "FZKDFNUQFN21EP3X3P4EP185X185"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'UQFN-20-1EP_3x3mm_P0.4mm_EP1.85x1.85mm', 'description': 'UQFN, 20 Pin (http://ww1.microchip.com/downloads/en/PackagingSpec/00000049BQ.pdf#page=332), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'UQFN NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/UQFN-20-1EP_3x3mm_P0.4mm_EP1.85x1.85mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_DFN_QFN : UQFN-20-1EP_3x3mm_P0.4mm_EP1.85x1.85mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

