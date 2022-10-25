
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "MLF-6-1EP_1.6x1.6mm_P0.5mm_EP0.5x1.26mm"
    hexID = "FZKDFNMLF61EP16X16P5EP5X126"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'MLF-6-1EP_1.6x1.6mm_P0.5mm_EP0.5x1.26mm', 'description': 'MLF, 6 Pin (http://ww1.microchip.com/downloads/en/DeviceDoc/mic5353.pdf), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'MLF NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/MLF-6-1EP_1.6x1.6mm_P0.5mm_EP0.5x1.26mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_DFN_QFN : MLF-6-1EP_1.6x1.6mm_P0.5mm_EP0.5x1.26mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

