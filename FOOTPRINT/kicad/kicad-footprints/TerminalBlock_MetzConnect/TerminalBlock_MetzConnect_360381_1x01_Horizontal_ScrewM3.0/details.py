
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "TerminalBlock_MetzConnect"
    oIndex = "TerminalBlock_MetzConnect_360381_1x01_Horizontal_ScrewM3.0"
    hexID = "FZKTBMETZCONNECTTBMETZCONNECT363811X1HORIZONTALSCREWM3"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TerminalBlock_MetzConnect_360381_1x01_Horizontal_ScrewM3.0', 'description': 'single screw terminal block Metz Connect 360381, block size 5x5mm^2, drill diamater 1.5mm, 2 pads, pad diameter 3mm, see http://www.metz-connect.com/de/system/files/METZ_CONNECT_U_Contact_Katalog_Anschlusssysteme_fuer_Leiterplatten_DE_31_07_2017_OFF_024803.pdf?language=en page 133, script-generated using https://github.com/pointhi/kicad-footprint-generator/scripts/TerminalBlock_MetzConnect', 'tags': 'THT single screw terminal block Metz Connect 360381 size 5x5mm^2 drill 1.5mm pad 3mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/TerminalBlock_MetzConnect.3dshapes/TerminalBlock_MetzConnect_360381_1x01_Horizontal_ScrewM3.0.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('TerminalBlock_MetzConnect : TerminalBlock_MetzConnect_360381_1x01_Horizontal_ScrewM3.0')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

