
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Rotary_Encoder"
    oIndex = "RotaryEncoder_Alps_EC11E-Switch_Vertical_H20mm_CircularMountingHoles"
    hexID = "FZKREROTARYENCODERALPSEC11ESWITCHVERTICALH2CIRCULARHOLS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'RotaryEncoder_Alps_EC11E-Switch_Vertical_H20mm_CircularMountingHoles', 'description': 'Alps rotary encoder, EC12E... with switch, vertical shaft, mounting holes with circular drills, http://www.alps.com/prod/info/E/HTML/Encoder/Incremental/EC11/EC11E15204A3.html', 'tags': 'rotary encoder', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Rotary_Encoder.3dshapes/RotaryEncoder_Alps_EC11E-Switch_Vertical_H20mm_CircularMountingHoles.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Rotary_Encoder : RotaryEncoder_Alps_EC11E-Switch_Vertical_H20mm_CircularMountingHoles')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

