
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Converter_DCDC"
    oIndex = "Converter_DCDC_Cincon_EC5BExx_Single_THT"
    hexID = "FZKCONCONCINCONEC5BEXXSINGLETHT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Converter_DCDC_Cincon_EC5BExx_Single_THT', 'description': 'DCDC-Converter, CINCON, EC5BExx, 18-36VDC to dual output, http://www.cincon.com/upload/media/data%20sheets/Data%20Sheet%20(DC)/B%20CASE/SPEC-EC5BE-V24.pdf', 'tags': 'DCDC-Converter CINCON EC5BExx 18-36VDC to dual output', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Converter_DCDC.3dshapes/Converter_DCDC_Cincon_EC5BExx_Single_THT.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Converter_DCDC : Converter_DCDC_Cincon_EC5BExx_Single_THT')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

