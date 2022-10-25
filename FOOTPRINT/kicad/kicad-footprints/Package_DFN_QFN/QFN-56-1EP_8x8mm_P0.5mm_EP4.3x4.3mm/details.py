
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "QFN-56-1EP_8x8mm_P0.5mm_EP4.3x4.3mm"
    hexID = "FZKDFNQFN561EP8X8P5EP43X43"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'QFN-56-1EP_8x8mm_P0.5mm_EP4.3x4.3mm', 'description': 'QFN, 56 Pin (http://ww1.microchip.com/downloads/en/DeviceDoc/00002142A.pdf#page=40), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'QFN NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/QFN-56-1EP_8x8mm_P0.5mm_EP4.3x4.3mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_DFN_QFN : QFN-56-1EP_8x8mm_P0.5mm_EP4.3x4.3mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

