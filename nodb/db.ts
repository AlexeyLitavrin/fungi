import * as fs from 'fs';

const IMGPATH = "./images/"
const FILEPATH = "./mushrooms/"

const FAMILIES: string[] = fs.readFileSync( "./families" ,'utf8').trim().split("\n");
const ZONES: string[] = fs.readFileSync( "./zones" ,'utf8').trim().split("\n");

//console.log( ZONES )

class Mushroom {
  public readonly appendDate: Date;
  public readonly name: string;
  public readonly index: number | string;
  public readonly zone: number[];
  public readonly gmapsLink: string;
  public readonly redBook: boolean | string;
  public readonly eatable: boolean | string;
  public readonly description: string;
  public readonly familie: number[];

  constructor ( list: string[] ){

    this.appendDate= new Date ( Date.parse( list[0] ));
    this.name= list[1];
    this.index= list[2]; 

    this.zone = list[3].slice(0,-1).split(";").map ( item => +item);

    this.gmapsLink= list[4];

    if ( list[5] == "1" ) this.redBook = true;
    else if ( list[5] == "0" ) this.redBook = false;
    else this.redBook = list[5];

    if ( list[6] == "1" ) this.eatable = true;
    else if ( list[6] == "0" ) this.eatable = false;
    else this.eatable = "50/50";

    this.description = list[7];

    this.familie = list[8].slice(0,-1).split(";").map ( item => +item);
  }

  show () {
    console.log ( "\n=== " + this.name + " ===\n" );
    console.log ( "Append date: " + this.appendDate.toString() );
    console.log ( this.index );
    console.log ( this.zone );
    console.log ( this.gmapsLink );
    console.log ( this.redBook );
    console.log ( this.eatable );
    console.log ( this.description );
    console.log ( this.familie );
  }

  getImgSrc () {
    return IMGPATH + this.index.toString () + ".jpg";
  }
}

function getFileList ( path: string = FILEPATH ): string[] {

  let output: string[] = [];

  fs.readdirSync(path).forEach((filename) => {
    output.push ( filename );
  });

  return output;
}

function parseMushrooms ( filelist: string[] ): Mushroom[] {
  let output: Mushroom[] = [];
  for ( let i = 0; i < filelist.length; i++ ){
    output.push ( new Mushroom ( fs.readFileSync( FILEPATH + filelist[i] ,'utf8').trim().split("\n"))); 
  }
  return output;
}

let mushrooms: Mushroom[] = parseMushrooms ( getFileList () )

for ( let i = 0; i < mushrooms.length; i++ ){
  mushrooms[i].show()
}

