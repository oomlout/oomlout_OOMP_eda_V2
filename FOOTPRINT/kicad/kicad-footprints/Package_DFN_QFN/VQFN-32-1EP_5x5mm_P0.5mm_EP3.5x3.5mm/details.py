
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "VQFN-32-1EP_5x5mm_P0.5mm_EP3.5x3.5mm"
    hexID = "FZKDFNVQFN321EP5X5P5EP35X35"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'VQFN-32-1EP_5x5mm_P0.5mm_EP3.5x3.5mm', 'description': 'VQFN, 32 Pin (https://www.ftdichip.com/Support/Documents/DataSheets/ICs/DS_FT4222H.pdf#page=40), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'VQFN NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/VQFN-32-1EP_5x5mm_P0.5mm_EP3.5x3.5mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_DFN_QFN : VQFN-32-1EP_5x5mm_P0.5mm_EP3.5x3.5mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

