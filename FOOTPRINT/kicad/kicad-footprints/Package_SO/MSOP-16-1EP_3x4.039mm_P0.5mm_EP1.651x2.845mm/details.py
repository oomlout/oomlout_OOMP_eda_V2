
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SO"
    oIndex = "MSOP-16-1EP_3x4.039mm_P0.5mm_EP1.651x2.845mm"
    hexID = "FZKSOMS161EP3X439P5EP1651X2845"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'MSOP-16-1EP_3x4.039mm_P0.5mm_EP1.651x2.845mm', 'description': 'MSOP, 16 Pin (https://www.analog.com/media/en/package-pcb-resources/package/pkg_pdf/ltc-legacy-msop/05081667_F_MSE16.pdf), generated with kicad-footprint-generator ipc_gullwing_generator.py', 'tags': 'MSOP SO', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/MSOP-16-1EP_3x4.039mm_P0.5mm_EP1.651x2.845mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_SO : MSOP-16-1EP_3x4.039mm_P0.5mm_EP1.651x2.845mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

