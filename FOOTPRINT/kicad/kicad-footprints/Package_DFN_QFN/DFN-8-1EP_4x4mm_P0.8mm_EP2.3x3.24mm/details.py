
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "DFN-8-1EP_4x4mm_P0.8mm_EP2.3x3.24mm"
    hexID = "FZKDFNDFN81EP4X4P8EP23X324"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'DFN-8-1EP_4x4mm_P0.8mm_EP2.3x3.24mm', 'description': 'DFN, 8 Pin (https://www.st.com/resource/en/datasheet/ld1086.pdf#page=35), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'DFN NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/DFN-8-1EP_4x4mm_P0.8mm_EP2.3x3.24mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_DFN_QFN : DFN-8-1EP_4x4mm_P0.8mm_EP2.3x3.24mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

