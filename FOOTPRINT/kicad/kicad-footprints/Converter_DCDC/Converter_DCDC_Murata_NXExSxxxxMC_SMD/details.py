
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Converter_DCDC"
    oIndex = "Converter_DCDC_Murata_NXExSxxxxMC_SMD"
    hexID = "FZKCONCONMNXEXSXXXXMCSM"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Converter_DCDC_Murata_NXExSxxxxMC_SMD', 'description': 'Isolated 1W or 2W Single Output SM DC/DC Converters https://www.murata.com/products/productdata/8807031865374/kdc-nxe1.pdf#page=8 https://www.murata.com/products/productdata/8807031898142/kdc-nxe2.pdf#page=9', 'tags': 'Isolated 1W or 2W Single Output SM DC/DC Converters', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Converter_DCDC.3dshapes/Converter_DCDC_Murata_NXE2SxxxxMC_SMD.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Converter_DCDC : Converter_DCDC_Murata_NXExSxxxxMC_SMD')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

