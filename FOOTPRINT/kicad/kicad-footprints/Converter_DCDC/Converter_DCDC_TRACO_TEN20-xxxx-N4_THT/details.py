
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Converter_DCDC"
    oIndex = "Converter_DCDC_TRACO_TEN20-xxxx-N4_THT"
    hexID = "FZKCONCONTRACOTEN2XXXXN4THT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Converter_DCDC_TRACO_TEN20-xxxx-N4_THT', 'description': 'DCDC-Converter TRACO TEN20 Generic, https://assets.tracopower.com/20171102100522/TEN20/documents/ten20-datasheet.pdf', 'tags': 'DCDC-Converter TRACO TEN20 Generic', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Converter_DCDC.3dshapes/Converter_DCDC_TRACO_TEN20-xxxx-N4_THT.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Converter_DCDC : Converter_DCDC_TRACO_TEN20-xxxx-N4_THT')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

