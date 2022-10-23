
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Converter_DCDC"
    oIndex = "Converter_DCDC_Murata_MGJ3"
    hexID = "FZKCONCONMMGJ3"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Converter_DCDC_Murata_MGJ3', 'description': 'Murata MGJ3, 5.2kVDC Isolated 3W Gate Drive, 15V/5V/5V Configurable, 22.61x23.11x14.19mm, https://power.murata.com/datasheet?/data/power/ncl/kdc_mgj3.pdf', 'tags': 'DCDC SMD', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Converter_DCDC.3dshapes/Converter_DCDC_Murata_MGJ3.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Converter_DCDC : Converter_DCDC_Murata_MGJ3')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

