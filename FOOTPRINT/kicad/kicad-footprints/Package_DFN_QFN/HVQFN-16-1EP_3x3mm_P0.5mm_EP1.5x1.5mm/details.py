
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "HVQFN-16-1EP_3x3mm_P0.5mm_EP1.5x1.5mm"
    hexID = "FZKDFNHVQFN161EP3X3P5EP15X15"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'HVQFN-16-1EP_3x3mm_P0.5mm_EP1.5x1.5mm', 'description': 'HVQFN, 16 Pin (https://www.nxp.com/docs/en/package-information/SOT758-1.pdf), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'HVQFN NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/HVQFN-16-1EP_3x3mm_P0.5mm_EP1.5x1.5mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_DFN_QFN : HVQFN-16-1EP_3x3mm_P0.5mm_EP1.5x1.5mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

