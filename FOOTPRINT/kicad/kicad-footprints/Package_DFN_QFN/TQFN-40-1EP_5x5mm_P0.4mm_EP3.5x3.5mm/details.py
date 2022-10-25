
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "TQFN-40-1EP_5x5mm_P0.4mm_EP3.5x3.5mm"
    hexID = "FZKDFNTQFN41EP5X5P4EP35X35"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TQFN-40-1EP_5x5mm_P0.4mm_EP3.5x3.5mm', 'description': 'TQFN, 40 Pin (https://pdfserv.maximintegrated.com/package_dwgs/21-0140.PDF (T4055-1)), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'TQFN NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/TQFN-40-1EP_5x5mm_P0.4mm_EP3.5x3.5mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_DFN_QFN : TQFN-40-1EP_5x5mm_P0.4mm_EP3.5x3.5mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

