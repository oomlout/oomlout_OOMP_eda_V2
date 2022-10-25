
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "QFN-72-1EP_10x10mm_P0.5mm_EP6x6mm"
    hexID = "FZKDFNQFN721EP1X1P5EP6X6"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'QFN-72-1EP_10x10mm_P0.5mm_EP6x6mm', 'description': 'QFN, 72 Pin (http://ww1.microchip.com/downloads/en/DeviceDoc/00001682C.pdf#page=70), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'QFN NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/QFN-72-1EP_10x10mm_P0.5mm_EP6x6mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_DFN_QFN : QFN-72-1EP_10x10mm_P0.5mm_EP6x6mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

