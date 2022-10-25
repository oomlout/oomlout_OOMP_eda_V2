
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Converter_DCDC"
    oIndex = "Converter_DCDC_RECOM_R5xxxPA_THT"
    hexID = "FZKCONCONRECOMR5XXXPATHT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Converter_DCDC_RECOM_R5xxxPA_THT', 'description': 'DCDC-Converter, RECOM, RECOM_R5xxxPA, SIP-12, pitch 2.54mm, package size 32.2x9.1x15mm^3, https://www.recom-power.com/pdf/Innoline/R-5xxxPA_DA.pdf', 'tags': 'dc-dc recom buck sip-12 pitch 2.54mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Converter_DCDC.3dshapes/Converter_DCDC_RECOM_R5xxxPA_THT.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Converter_DCDC : Converter_DCDC_RECOM_R5xxxPA_THT')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

