
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_QFP"
    oIndex = "TQFP-52-1EP_10x10mm_P0.65mm_EP6.5x6.5mm"
    hexID = "FZKQFPTQFP521EP1X1P65EP65X65"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TQFP-52-1EP_10x10mm_P0.65mm_EP6.5x6.5mm', 'description': 'TQFP, 52 Pin (http://www.analog.com/media/en/package-pcb-resources/package/pkg_pdf/tqfp_edsv/sv_52_1.pdf), generated with kicad-footprint-generator ipc_qfp_generator.py', 'tags': 'TQFP QFP', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_QFP.3dshapes/TQFP-52-1EP_10x10mm_P0.65mm_EP6.5x6.5mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_QFP : TQFP-52-1EP_10x10mm_P0.65mm_EP6.5x6.5mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

