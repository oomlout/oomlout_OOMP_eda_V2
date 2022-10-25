
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "UQFN-16-1EP_4x4mm_P0.65mm_EP2.6x2.6mm"
    hexID = "FZKDFNUQFN161EP4X4P65EP26X26"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'UQFN-16-1EP_4x4mm_P0.65mm_EP2.6x2.6mm', 'description': 'UQFN, 16 Pin (http://ww1.microchip.com/downloads/en/DeviceDoc/16L_UQFN_4x4x0_5mm_JQ_C04257A.pdf), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'UQFN NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/UQFN-16-1EP_4x4mm_P0.65mm_EP2.6x2.6mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_DFN_QFN : UQFN-16-1EP_4x4mm_P0.65mm_EP2.6x2.6mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

