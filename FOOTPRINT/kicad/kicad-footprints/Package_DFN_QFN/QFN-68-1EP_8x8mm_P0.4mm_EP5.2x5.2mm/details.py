
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "QFN-68-1EP_8x8mm_P0.4mm_EP5.2x5.2mm"
    hexID = "FZKDFNQFN681EP8X8P4EP52X52"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'QFN-68-1EP_8x8mm_P0.4mm_EP5.2x5.2mm', 'description': 'QFN, 68 Pin (https://cdn.microsemi.com/documents/1bf6886f-5919-4508-a50b-b1dbf3fdf0f4/download/#page=98), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'QFN NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/QFN-68-1EP_8x8mm_P0.4mm_EP5.2x5.2mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_DFN_QFN : QFN-68-1EP_8x8mm_P0.4mm_EP5.2x5.2mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

