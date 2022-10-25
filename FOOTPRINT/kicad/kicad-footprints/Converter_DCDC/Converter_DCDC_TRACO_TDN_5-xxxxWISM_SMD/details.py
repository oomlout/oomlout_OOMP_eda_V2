
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Converter_DCDC"
    oIndex = "Converter_DCDC_TRACO_TDN_5-xxxxWISM_SMD"
    hexID = "FZKCONCONTRACOTDN5XXXXWISMSM"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Converter_DCDC_TRACO_TDN_5-xxxxWISM_SMD', 'description': 'Traco TDN 5WISM Series, 5W, SMD (https://assets.tracopower.com/20200225170127/TDN5WISM/documents/tdn5wism-datasheet.pdf#page=3)', 'tags': 'dcdc traco 5w smd', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Converter_DCDC.3dshapes/Converter_DCDC_TRACO_TDN_5-xxxxWISM_SMD.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Converter_DCDC : Converter_DCDC_TRACO_TDN_5-xxxxWISM_SMD')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

