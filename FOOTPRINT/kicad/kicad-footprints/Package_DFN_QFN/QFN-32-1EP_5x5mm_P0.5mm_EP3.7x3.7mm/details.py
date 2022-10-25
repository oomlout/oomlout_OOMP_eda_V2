
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "QFN-32-1EP_5x5mm_P0.5mm_EP3.7x3.7mm"
    hexID = "FZKDFNQFN321EP5X5P5EP37X37"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'QFN-32-1EP_5x5mm_P0.5mm_EP3.7x3.7mm', 'description': 'QFN, 32 Pin (https://www.espressif.com/sites/default/files/documentation/0a-esp8285_datasheet_en.pdf), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'QFN NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/QFN-32-1EP_5x5mm_P0.5mm_EP3.7x3.7mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_DFN_QFN : QFN-32-1EP_5x5mm_P0.5mm_EP3.7x3.7mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

