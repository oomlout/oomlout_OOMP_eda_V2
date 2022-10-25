
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Converter_ACDC"
    oIndex = "Converter_ACDC_CUI_PBO-3-Sxx_THT_Vertical"
    hexID = "FZKCONCONCUIPBO3SXXTHTVERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Converter_ACDC_CUI_PBO-3-Sxx_THT_Vertical', 'description': 'ACDC-Converter, 3W, CUI PBO-3, THT https://www.cui.com/product/resource/pbo-3.pdf', 'tags': 'Converter AC-DC THT Vertical', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Converter_ACDC.3dshapes/Converter_ACDC_CUI_PBO-3-Sxx_THT_Vertical.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Converter_ACDC : Converter_ACDC_CUI_PBO-3-Sxx_THT_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

