
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Converter_DCDC"
    oIndex = "Converter_DCDC_RECOM_RPA60-xxxxSFW"
    hexID = "FZKCONCONRECOMRPA6XXXXSFW"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Converter_DCDC_RECOM_RPA60-xxxxSFW', 'description': 'RPA60-FW 60W Isolated DC to DC Converters', 'tags': 'DCDC Regulator Single', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Converter_DCDC.3dshapes/Converter_DCDC_RECOM_RPA60-xxxxSFW.wrl', 'pins': {'type': 'thru_hole', 'shape': 'roundrect'}})
    newPart['name'].append('Converter_DCDC : Converter_DCDC_RECOM_RPA60-xxxxSFW')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

