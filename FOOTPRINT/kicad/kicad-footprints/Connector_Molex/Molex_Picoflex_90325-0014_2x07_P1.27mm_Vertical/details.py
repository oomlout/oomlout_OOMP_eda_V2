
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Molex"
    oIndex = "Molex_Picoflex_90325-0014_2x07_P1.27mm_Vertical"
    hexID = "FZKCNMXMXPICOFLEX9325142X7P127VERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Molex_Picoflex_90325-0014_2x07_P1.27mm_Vertical', 'description': 'Molex Picoflex Ribbon-Cable Connectors, 90325-0014, 14 Pins (http://www.molex.com/pdm_docs/sd/903250004_sd.pdf), generated with kicad-footprint-generator', 'tags': 'connector Molex Picoflex side entry', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Molex.3dshapes/Molex_Picoflex_90325-0014_2x07_P1.27mm_Vertical.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_Molex : Molex_Picoflex_90325-0014_2x07_P1.27mm_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

