
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "QFN-32-1EP_4x4mm_P0.4mm_EP2.65x2.65mm"
    hexID = "FZKDFNQFN321EP4X4P4EP265X265"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'QFN-32-1EP_4x4mm_P0.4mm_EP2.65x2.65mm', 'description': 'QFN, 32 Pin (https://www.renesas.com/eu/en/package-image/pdf/outdrawing/l32.4x4a.pdf), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'QFN NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/QFN-32-1EP_4x4mm_P0.4mm_EP2.65x2.65mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_DFN_QFN : QFN-32-1EP_4x4mm_P0.4mm_EP2.65x2.65mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

