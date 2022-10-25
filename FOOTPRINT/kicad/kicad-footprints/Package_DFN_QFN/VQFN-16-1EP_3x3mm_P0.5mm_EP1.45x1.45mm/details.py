
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "VQFN-16-1EP_3x3mm_P0.5mm_EP1.45x1.45mm"
    hexID = "FZKDFNVQFN161EP3X3P5EP145X145"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'VQFN-16-1EP_3x3mm_P0.5mm_EP1.45x1.45mm', 'description': 'VQFN, 16 Pin (http://www.ti.com/lit/ds/sbos354a/sbos354a.pdf, JEDEC MO-220 variant VEED-6), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'VQFN NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/VQFN-16-1EP_3x3mm_P0.5mm_EP1.45x1.45mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_DFN_QFN : VQFN-16-1EP_3x3mm_P0.5mm_EP1.45x1.45mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

