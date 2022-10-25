
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "WQFN-20-1EP_3x3mm_P0.4mm_EP1.7x1.7mm"
    hexID = "FZKDFNWQFN21EP3X3P4EP17X17"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'WQFN-20-1EP_3x3mm_P0.4mm_EP1.7x1.7mm', 'description': 'WQFN, 20 Pin (https://www.ti.com/lit/ds/symlink/ts3ds10224.pdf#page=29), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'WQFN NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/WQFN-20-1EP_3x3mm_P0.4mm_EP1.7x1.7mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_DFN_QFN : WQFN-20-1EP_3x3mm_P0.4mm_EP1.7x1.7mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

