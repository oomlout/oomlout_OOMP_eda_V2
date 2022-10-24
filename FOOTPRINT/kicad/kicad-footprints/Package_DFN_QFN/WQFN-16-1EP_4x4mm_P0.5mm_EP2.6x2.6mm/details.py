
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "WQFN-16-1EP_4x4mm_P0.5mm_EP2.6x2.6mm"
    hexID = "FZKDFNWQFN161EP4X4P5EP26X26"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'WQFN-16-1EP_4x4mm_P0.5mm_EP2.6x2.6mm', 'description': 'WQFN, 16 Pin (http://www.ti.com/lit/ds/symlink/ldc1312.pdf#page=59), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'WQFN NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/WQFN-16-1EP_4x4mm_P0.5mm_EP2.6x2.6mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_DFN_QFN : WQFN-16-1EP_4x4mm_P0.5mm_EP2.6x2.6mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

