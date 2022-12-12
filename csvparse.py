import drive.parser

formating = [
        "time",
        "name",
        "image",
        "zones",
        "gmapsLink",
        "redBook",
        "eatable",
        "description",
        "familie"
        ]

def getFamiliesIds ( famlist ):
    rstr = ""
    with open ( "./nodb/families", "r" ) as file:
        families = file.read().strip().split("\n")

        for fam in famlist:
            for index, el in enumerate ( families ):
                if fam == el:
                    rstr+= str ( index ) + ";"
                    break

    return rstr

def getZoneIds ( zonelist ):
    rstr = ""
    with open ( "./nodb/zones", "r" ) as file:
        zones = file.read().strip().split("\n")

        for zone in zonelist:
            for index, el in enumerate ( zones ):
                if zone == el:
                    rstr+= str ( index ) + ";"
                    break

    return rstr


with open ("answers.csv", "r") as file:
    answers = file.read ().strip().split("\n")[1:]
    answLists = []
    for answer in answers:
        answer = answer.split ("\"")
        answList = []
        for index in range ( 1, len ( answer), 2 ):
             answList.append ( answer[index] )


        drive.parser.downloadFiles ( [answList[2].split("id=")[-1]] )
        answList[2] = "require ( \"./images/" + answList[2].split("id=")[-1] + ".jpg\")"
        #drive.parser.downloadFiles ( [answList[2]] )
        answList[3] = getZoneIds ( answList[3].strip().split (";") )

        answList[-1] = getFamiliesIds (  answList[-1][2:].split(";") )

        if answList[5] == "Да": answList[5] = 1
        elif answList[5] == "Нет": answList[5] = 0

        if answList[6] == "Да": answList[6] = 1
        elif answList[6] == "Нет": answList[6] = 0
        elif answList[6]: answList[6] = 2

        answLists.append (answList )

    with open ( "./nodb/mushrooms.tsx", "w" ) as file:
        file.write ( "const Mushrooms = {\n\t\"mushrooms\" : [\n" )
        for alIndex, answList in enumerate ( answLists ):
            file.write ( "\t{\n" )
            for index, item in enumerate ( answList ):

                if index == len (answList) - 1: file.write ( "\t\t\"" + formating[index] + "\" : \"" + str ( item ) + "\"\n" )
                elif "image" == formating[index]: file.write ( "\t\t\"" + formating[index] + "\" : " + str ( item ) + ",\n" )
                else: file.write ( "\t\t\"" + formating[index] + "\" : \"" + str ( item ) + "\",\n" )

            print ( alIndex )
            print (len ( answLists ) - 1 ) 
            if ( alIndex == len ( answLists ) - 1 ): file.write ( "\n\t}\n" )
            else:file.write ( "\n\t},\n" )

        file.write ( "\t]\n};\n\nexport default Mushrooms;" )
