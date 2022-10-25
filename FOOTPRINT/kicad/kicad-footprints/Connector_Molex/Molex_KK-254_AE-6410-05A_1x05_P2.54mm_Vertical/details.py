
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Molex"
    oIndex = "Molex_KK-254_AE-6410-05A_1x05_P2.54mm_Vertical"
    hexID = "FZKCNMXMXKK254AE6415A1X5P254VERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Molex_KK-254_AE-6410-05A_1x05_P2.54mm_Vertical', 'description': 'Molex KK-254 Interconnect System, old/engineering part number: AE-6410-05A example for new part number: 22-27-2051, 5 Pins (http://www.molex.com/pdm_docs/sd/022272021_sd.pdf), generated with kicad-footprint-generator', 'tags': 'connector Molex KK-254 vertical', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Molex.3dshapes/Molex_KK-254_AE-6410-05A_1x05_P2.54mm_Vertical.wrl', 'pins': {'type': 'thru_hole', 'shape': 'roundrect'}})
    newPart['name'].append('Connector_Molex : Molex_KK-254_AE-6410-05A_1x05_P2.54mm_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

