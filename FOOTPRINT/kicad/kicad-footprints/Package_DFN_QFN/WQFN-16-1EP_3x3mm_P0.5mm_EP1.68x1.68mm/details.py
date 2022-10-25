
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "WQFN-16-1EP_3x3mm_P0.5mm_EP1.68x1.68mm"
    hexID = "FZKDFNWQFN161EP3X3P5EP168X168"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'WQFN-16-1EP_3x3mm_P0.5mm_EP1.68x1.68mm', 'description': 'WQFN, 16 Pin (https://www.ti.com/lit/ds/symlink/tlv9064.pdf#page=44), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'WQFN NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/WQFN-16-1EP_3x3mm_P0.5mm_EP1.68x1.68mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_DFN_QFN : WQFN-16-1EP_3x3mm_P0.5mm_EP1.68x1.68mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

