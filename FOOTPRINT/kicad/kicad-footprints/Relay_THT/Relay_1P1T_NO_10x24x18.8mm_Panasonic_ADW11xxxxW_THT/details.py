
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Relay_THT"
    oIndex = "Relay_1P1T_NO_10x24x18.8mm_Panasonic_ADW11xxxxW_THT"
    hexID = "FZKRELRELAY1P1TNO1X24X188PANASONICADW11XXXXWTHT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Relay_1P1T_NO_10x24x18.8mm_Panasonic_ADW11xxxxW_THT', 'description': 'Panasonic Relay SPST 10mm 24mm, https://www.panasonic-electric-works.com/pew/es/downloads/ds_dw_hl_en.pdf', 'tags': 'Panasonic Relay SPST', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Relay_THT.3dshapes/Relay_1P1T_NO_10x24x18.8mm_Panasonic_ADW11xxxxW_THT.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Relay_THT : Relay_1P1T_NO_10x24x18.8mm_Panasonic_ADW11xxxxW_THT')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

