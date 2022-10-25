
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Converter_DCDC"
    oIndex = "Converter_DCDC_RECOM_R-78S-0.1_THT"
    hexID = "FZKCONCONRECOMR78S1THT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Converter_DCDC_RECOM_R-78S-0.1_THT', 'description': 'DCDC-Converter, RECOM, RECOM_R-78S-0.1, SIP-4, pitch 2.54mm, package size 11.6x8.5x10.4mm^3, https://www.recom-power.com/pdf/Innoline/R-78Sxx-0.1.pdf', 'tags': 'dc-dc recom buck sip-4 pitch 2.54mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Converter_DCDC.3dshapes/Converter_DCDC_RECOM_R-78S-0.1_THT.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Converter_DCDC : Converter_DCDC_RECOM_R-78S-0.1_THT')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

