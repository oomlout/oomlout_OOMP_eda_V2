
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "TQFN-16-1EP_3x3mm_P0.5mm_EP1.6x1.6mm"
    hexID = "FZKDFNTQFN161EP3X3P5EP16X16"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TQFN-16-1EP_3x3mm_P0.5mm_EP1.6x1.6mm', 'description': 'TQFN, 16 Pin (https://www.diodes.com/assets/Datasheets/PI6C5946002.pdf#page=12), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'TQFN NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/TQFN-16-1EP_3x3mm_P0.5mm_EP1.6x1.6mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_DFN_QFN : TQFN-16-1EP_3x3mm_P0.5mm_EP1.6x1.6mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

