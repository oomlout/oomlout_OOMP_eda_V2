
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Relay_THT"
    oIndex = "Relay_SPST_StandexMeder_MS_Form1AB"
    hexID = "FZKRELRELAYSPSTSTANDEXMEDERMSFORM1AB"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Relay_SPST_StandexMeder_MS_Form1AB', 'description': 'Standex-Meder MS SIL-relais, Form 1A/1B, see https://standexelectronics.com/de/produkte/ms-reed-relais/', 'tags': 'Standex Meder MS SIL reed relais', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Relay_THT.3dshapes/Relay_SPST_StandexMeder_MS_Form1AB.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Relay_THT : Relay_SPST_StandexMeder_MS_Form1AB')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

