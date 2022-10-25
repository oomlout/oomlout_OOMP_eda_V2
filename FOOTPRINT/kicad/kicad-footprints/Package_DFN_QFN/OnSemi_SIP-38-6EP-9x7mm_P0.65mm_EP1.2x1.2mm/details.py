
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "OnSemi_SIP-38-6EP-9x7mm_P0.65mm_EP1.2x1.2mm"
    hexID = "FZKDFNONSEMISIP386EP9X7P65EP12X12"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'OnSemi_SIP-38-6EP-9x7mm_P0.65mm_EP1.2x1.2mm', 'description': 'On Semiconductor, SIP-38, 9x7mm, (https://www.onsemi.com/pub/Collateral/AX-SIP-SFEU-D.PDF#page=19)', 'tags': 'On Semiconductor SIP', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/OnSemi_SIP-38-6EP-9x7mm_P0.65mm_EP1.2x1.2mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_DFN_QFN : OnSemi_SIP-38-6EP-9x7mm_P0.65mm_EP1.2x1.2mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

