
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "UDFN-4-1EP_1x1mm_P0.65mm_EP0.48x0.48mm"
    hexID = "FZKDFNUDFN41EP1X1P65EP48X48"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'UDFN-4-1EP_1x1mm_P0.65mm_EP0.48x0.48mm', 'description': 'UDFN-4_1x1mm_P0.65mm, http://ww1.microchip.com/downloads/en/DeviceDoc/MIC550x-300mA-Single-Output-LDO-in-Small-Packages-DS20006006A.pdf', 'tags': 'UDFN-4_1x1mm_P0.65mm', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/UDFN-4-1EP_1x1mm_P0.65mm_EP0.48x0.48mm.wrl', 'pins': {'type': 'smd', 'shape': 'custom'}})
    newPart['name'].append('Package_DFN_QFN : UDFN-4-1EP_1x1mm_P0.65mm_EP0.48x0.48mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

