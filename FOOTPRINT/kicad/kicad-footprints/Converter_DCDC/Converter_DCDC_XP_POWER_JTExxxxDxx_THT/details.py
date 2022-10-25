
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Converter_DCDC"
    oIndex = "Converter_DCDC_XP_POWER_JTExxxxDxx_THT"
    hexID = "FZKCONCONXPPOWERJTEXXXXDXXTHT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Converter_DCDC_XP_POWER_JTExxxxDxx_THT', 'description': 'DCDC-Converter, XP POWER, Type JTE06 Series,  Dual Output', 'tags': 'DCDC-Converter XP_POWER JTE06 Dual', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Converter_DCDC.3dshapes/Converter_DCDC_XP_POWER_JTExxxxDxx_THT.wrl', 'pins': {'type': 'thru_hole', 'shape': 'oval'}})
    newPart['name'].append('Converter_DCDC : Converter_DCDC_XP_POWER_JTExxxxDxx_THT')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

