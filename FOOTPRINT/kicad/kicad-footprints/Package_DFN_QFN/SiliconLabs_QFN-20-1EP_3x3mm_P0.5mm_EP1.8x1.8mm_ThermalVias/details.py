
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "SiliconLabs_QFN-20-1EP_3x3mm_P0.5mm_EP1.8x1.8mm_ThermalVias"
    hexID = "FZKDFNSILICONLABSQFN21EP3X3P5EP18X18THERMALVIAS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SiliconLabs_QFN-20-1EP_3x3mm_P0.5mm_EP1.8x1.8mm_ThermalVias', 'description': '20-Lead Plastic Quad Flat, No Lead Package - 3x3 mm Body [QFN] with corner pads and thermal vias; see figure 8.2 of https://www.silabs.com/documents/public/data-sheets/efm8bb1-datasheet.pdf', 'tags': 'QFN 0.5', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/SiliconLabs_QFN-20-1EP_3x3mm_P0.5mm_EP1.8x1.8mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_DFN_QFN : SiliconLabs_QFN-20-1EP_3x3mm_P0.5mm_EP1.8x1.8mm_ThermalVias')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

