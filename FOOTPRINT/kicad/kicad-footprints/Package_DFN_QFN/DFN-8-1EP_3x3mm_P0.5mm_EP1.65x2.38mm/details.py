
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "DFN-8-1EP_3x3mm_P0.5mm_EP1.65x2.38mm"
    hexID = "FZKDFNDFN81EP3X3P5EP165X238"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'DFN-8-1EP_3x3mm_P0.5mm_EP1.65x2.38mm', 'description': 'DFN, 8 Pin (https://www.analog.com/media/en/technical-documentation/data-sheets/4320fb.pdf), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'DFN NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/DFN-8-1EP_3x3mm_P0.5mm_EP1.65x2.38mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_DFN_QFN : DFN-8-1EP_3x3mm_P0.5mm_EP1.65x2.38mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

