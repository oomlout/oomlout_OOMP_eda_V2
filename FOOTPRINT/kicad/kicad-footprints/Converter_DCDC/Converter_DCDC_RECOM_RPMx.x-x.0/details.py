
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Converter_DCDC"
    oIndex = "Converter_DCDC_RECOM_RPMx.x-x.0"
    hexID = "FZKCONCONRECOMRPMXXX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Converter_DCDC_RECOM_RPMx.x-x.0', 'description': 'https://www.recom-power.com/pdf/Innoline/RPM-6.0.pdf', 'tags': 'dc-dc recom buck lga-25 pitch 2.29mm', 'attributeType': 'smd', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Converter_DCDC : Converter_DCDC_RECOM_RPMx.x-x.0')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

