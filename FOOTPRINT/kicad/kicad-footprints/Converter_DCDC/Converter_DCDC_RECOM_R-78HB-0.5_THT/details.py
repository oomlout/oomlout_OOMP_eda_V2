
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Converter_DCDC"
    oIndex = "Converter_DCDC_RECOM_R-78HB-0.5_THT"
    hexID = "FZKCONCONRECOMR78HB5THT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Converter_DCDC_RECOM_R-78HB-0.5_THT', 'description': 'DCDC-Converter, RECOM, RECOM_R-78HB-0.5, SIP-3, pitch 2.54mm, package size 11.5x8.5x17.5mm^3, https://www.recom-power.com/pdf/Innoline/R-78HBxx-0.5_L.pdf', 'tags': 'dc-dc recom buck sip-3 pitch 2.54mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Converter_DCDC.3dshapes/Converter_DCDC_RECOM_R-78HB-0.5_THT.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Converter_DCDC : Converter_DCDC_RECOM_R-78HB-0.5_THT')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

