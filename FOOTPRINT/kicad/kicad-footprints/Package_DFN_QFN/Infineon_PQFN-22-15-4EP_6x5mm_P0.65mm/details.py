
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "Infineon_PQFN-22-15-4EP_6x5mm_P0.65mm"
    hexID = "FZKDFNINFINEONPQFN22154EP6X5P65"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Infineon_PQFN-22-15-4EP_6x5mm_P0.65mm', 'description': 'PQFN 22 leads, 5x6mm, 0.127mm stencil (https://www.infineon.com/dgdl/ir4301.pdf?fileId=5546d462533600a4015355d5fc691819, https://www.infineon.com/dgdl/Infineon-AN1170-AN-v05_00-EN.pdf?fileId=5546d462533600a40153559ac3e51134)', 'tags': 'pqfn 22 5x6mm', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/Infineon_PQFN-22-15-4EP_6x5mm_P0.65mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_DFN_QFN : Infineon_PQFN-22-15-4EP_6x5mm_P0.65mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

