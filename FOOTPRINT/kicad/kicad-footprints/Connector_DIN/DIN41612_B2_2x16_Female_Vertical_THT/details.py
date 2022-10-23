
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_DIN"
    oIndex = "DIN41612_B2_2x16_Female_Vertical_THT"
    hexID = "FZKCNDINDIN41612B22X16FEMALEVERTICALTHT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'DIN41612_B2_2x16_Female_Vertical_THT', 'description': 'DIN41612 connector, type B/2, Vertical, 2 rows 16 pins wide, https://www.erni-x-press.com/de/downloads/kataloge/englische_kataloge/erni-din41612-iec60603-2-e.pdf', 'tags': 'DIN 41612 IEC 60603 B/2', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_DIN.3dshapes/DIN41612_B2_2x16_Female_Vertical_THT.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_DIN : DIN41612_B2_2x16_Female_Vertical_THT')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

