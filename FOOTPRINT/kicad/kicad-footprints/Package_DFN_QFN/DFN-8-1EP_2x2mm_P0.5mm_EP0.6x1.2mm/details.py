
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "DFN-8-1EP_2x2mm_P0.5mm_EP0.6x1.2mm"
    hexID = "FZKDFNDFN81EP2X2P5EP6X12"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'DFN-8-1EP_2x2mm_P0.5mm_EP0.6x1.2mm', 'description': 'DFN, 8 Pin (https://www.qorvo.com/products/d/da001879), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'DFN NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/DFN-8-1EP_2x2mm_P0.5mm_EP0.6x1.2mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_DFN_QFN : DFN-8-1EP_2x2mm_P0.5mm_EP0.6x1.2mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

