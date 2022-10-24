
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Sensor_Current"
    oIndex = "Allegro_CB_PSF"
    hexID = "FZKSENCURRENTALLEGROCBPSF"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Allegro_CB_PSF', 'description': 'Allegro MicroSystems, CB-PSF Package (http://www.allegromicro.com/en/Products/Current-Sensor-ICs/Fifty-To-Two-Hundred-Amp-Integrated-Conductor-Sensor-ICs/ACS758.aspx)', 'tags': 'Allegro CB-PSF', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Sensor_Current.3dshapes/Allegro_CB_PSF.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Sensor_Current : Allegro_CB_PSF')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

