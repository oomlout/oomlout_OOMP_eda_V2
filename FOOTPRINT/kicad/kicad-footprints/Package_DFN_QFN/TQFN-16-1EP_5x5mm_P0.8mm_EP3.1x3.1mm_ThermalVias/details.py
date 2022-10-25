
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "TQFN-16-1EP_5x5mm_P0.8mm_EP3.1x3.1mm_ThermalVias"
    hexID = "FZKDFNTQFN161EP5X5P8EP31X31THERMALVIAS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TQFN-16-1EP_5x5mm_P0.8mm_EP3.1x3.1mm_ThermalVias', 'description': 'TQFN, 16 Pin (https://pdfserv.maximintegrated.com/package_dwgs/21-0140.PDF (T1655-2)), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'TQFN NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/TQFN-16-1EP_5x5mm_P0.8mm_EP3.1x3.1mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_DFN_QFN : TQFN-16-1EP_5x5mm_P0.8mm_EP3.1x3.1mm_ThermalVias')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

