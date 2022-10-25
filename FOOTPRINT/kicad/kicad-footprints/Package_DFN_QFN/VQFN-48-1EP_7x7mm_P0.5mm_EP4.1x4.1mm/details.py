
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "VQFN-48-1EP_7x7mm_P0.5mm_EP4.1x4.1mm"
    hexID = "FZKDFNVQFN481EP7X7P5EP41X41"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'VQFN-48-1EP_7x7mm_P0.5mm_EP4.1x4.1mm', 'description': 'VQFN, 48 Pin (http://www.ti.com/lit/ds/symlink/cc430f5137.pdf#page=128), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'VQFN NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/VQFN-48-1EP_7x7mm_P0.5mm_EP4.1x4.1mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_DFN_QFN : VQFN-48-1EP_7x7mm_P0.5mm_EP4.1x4.1mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

