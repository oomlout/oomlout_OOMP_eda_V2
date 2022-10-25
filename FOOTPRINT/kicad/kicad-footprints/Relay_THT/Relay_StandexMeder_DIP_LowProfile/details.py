
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Relay_THT"
    oIndex = "Relay_StandexMeder_DIP_LowProfile"
    hexID = "FZKRELRELAYSTANDEXMEDERDIPLOWPROFILE"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Relay_StandexMeder_DIP_LowProfile', 'description': 'package for Standex Meder DIP reed relay series, see https://standexelectronics.com/wp-content/uploads/datasheet_reed_relay_DIP.pdf', 'tags': 'DIL DIP PDIP 2.54mm 7.62mm 300mil reed relay', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Relay_THT.3dshapes/Relay_StandexMeder_DIP_LowProfile.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Relay_THT : Relay_StandexMeder_DIP_LowProfile')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

