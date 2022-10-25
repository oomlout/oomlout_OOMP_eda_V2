
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "Infineon_PQFN-44-31-5EP_7x7mm_P0.5mm"
    hexID = "FZKDFNINFINEONPQFN44315EP7X7P5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Infineon_PQFN-44-31-5EP_7x7mm_P0.5mm', 'description': 'PQFN 44 leads, 7x7mm, 0.127mm stencil (https://www.infineon.com/dgdl/ir4302.pdf?fileId=5546d462533600a4015355d602a9181d, https://www.infineon.com/dgdl/Infineon-AN1170-AN-v05_00-EN.pdf?fileId=5546d462533600a40153559ac3e51134)', 'tags': 'pqfn 44 7x7mm', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/Infineon_PQFN-44-31-5EP_7x7mm_P0.5mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_DFN_QFN : Infineon_PQFN-44-31-5EP_7x7mm_P0.5mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

