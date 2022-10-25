
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Sensor_Pressure"
    oIndex = "Honeywell_40PCxxxG1A"
    hexID = "FZKSENPRESSUREHONEYWELL4PCXXXG1A"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Honeywell_40PCxxxG1A', 'description': 'https://www.honeywellscportal.com/index.php?ci_id=138832', 'tags': 'pressure sensor automotive honeywell', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Sensor_Pressure.3dshapes/Honeywell_40PCxxxG1A.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Sensor_Pressure : Honeywell_40PCxxxG1A')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

