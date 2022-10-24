
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Rotary_Encoder"
    oIndex = "RotaryEncoder_Alps_EC12E_Vertical_H20mm"
    hexID = "FZKREROTARYENCODERALPSEC12EVERTICALH2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'RotaryEncoder_Alps_EC12E_Vertical_H20mm', 'description': 'Alps rotary encoder, EC12E..., vertical shaft, http://www.alps.com/prod/info/E/HTML/Encoder/Incremental/EC12E/EC12E1240405.html', 'tags': 'rotary encoder', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Rotary_Encoder.3dshapes/RotaryEncoder_Alps_EC12E_Vertical_H20mm.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Rotary_Encoder : RotaryEncoder_Alps_EC12E_Vertical_H20mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

