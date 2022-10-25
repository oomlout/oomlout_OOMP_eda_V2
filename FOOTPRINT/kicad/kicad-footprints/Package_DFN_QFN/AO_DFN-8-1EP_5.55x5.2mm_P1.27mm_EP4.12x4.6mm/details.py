
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "AO_DFN-8-1EP_5.55x5.2mm_P1.27mm_EP4.12x4.6mm"
    hexID = "FZKDFNAODFN81EP555X52P127EP412X46"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'AO_DFN-8-1EP_5.55x5.2mm_P1.27mm_EP4.12x4.6mm', 'description': 'DD Package; 8-Lead Plastic DFN (5.55mm x 5.2mm), Pin 5-8 connected to EP (http://www.aosmd.com/res/packaging_information/DFN5x6_8L_EP1_P.pdf)', 'tags': 'dfn ', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/AO_DFN-8-1EP_5.55x5.2mm_P1.27mm_EP4.12x4.6mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_DFN_QFN : AO_DFN-8-1EP_5.55x5.2mm_P1.27mm_EP4.12x4.6mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

