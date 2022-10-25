
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "DFN-6-1EP_1.2x1.2mm_P0.4mm_EP0.3x0.94mm_PullBack"
    hexID = "FZKDFNDFN61EP12X12P4EP3X94PULLBACK"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'DFN-6-1EP_1.2x1.2mm_P0.4mm_EP0.3x0.94mm_PullBack', 'description': 'DFN, 6 Pin (http://www.onsemi.com/pub/Collateral/NCP133-D.PDF), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'DFN NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/DFN-6-1EP_1.2x1.2mm_P0.4mm_EP0.3x0.94mm_PullBack.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_DFN_QFN : DFN-6-1EP_1.2x1.2mm_P0.4mm_EP0.3x0.94mm_PullBack')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

