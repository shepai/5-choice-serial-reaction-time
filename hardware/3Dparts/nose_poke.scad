screwD = 4;

noseHoleD = 12;
noseHoleH = 12;
tolerance = 0.1;

ledDx = 8; // main LED
ledD = 5;
ledH = 6;
wallT = 2.5;

backWallL = 170;
backWallD = 130;
backWallH = 170;

pokeAreaH = 185;

// for the sides to slide
// slideWallx = 12
// slideWally = 29
// slideWallz = 185


module nosePoke(){
    $fn=30;
difference(){
union(){
cylinder(d=noseHoleD+wallT,h=noseHoleH+wallT);
cylinder(d=noseHoleD+2*screwD+7,h=wallT);
translate([0,0,noseHoleH+wallT]){
cylinder(d=ledDx+2,h=ledH);
}//end translate

translate([(noseHoleD+1)/2,0,ledD]){
rotate([0,90,0]){
    cylinder(d=ledD+wallT,h=ledH);
}//end rotate
}//end translate

translate([-(noseHoleD+1)/2,0,ledD]){
rotate([0,-90,0]){
    cylinder(d=ledD+wallT,h=ledH);
}//end rotate
}//end translate
}//end union


translate([0,0,-1]){
cylinder(d=noseHoleD,h=noseHoleH);
cylinder(d=ledDx,h=ledH+noseHoleH+wallT+5);
}//end translate

translate([(noseHoleD+1)/2-wallT,0,ledD]){
rotate([0,90,0]){
    cylinder(d=ledD+2*tolerance,h=ledH+3);
}//end rotate
}//end translate

translate([-(noseHoleD+1)/2+wallT,0,ledD]){
rotate([0,-90,0]){
    cylinder(d=ledD+2*tolerance,h=ledH+3);
}//end rotate
}//end translate

translate([0,(noseHoleD)/2+screwD,-1]){
cylinder(d=screwD,h=10);
}//end translate

translate([0,-(noseHoleD)/2-screwD,-1]){
cylinder(d=screwD,h=10);
}//end translate
}//end difference
}//end module



module backWall(){
    $fn=16;
    
    
    difference(){
    
    cylinder(d=backWallD,h=pokeAreaH);
    
    union(){
    translate([0,0,-1]){
    
        cylinder(d=backWallD-15,h=pokeAreaH+2);
        
    }//end transalte

    translate([-backWallD/2,-30,-1]){
    cube([backWallD+4,backWallD,pokeAreaH+2]);
    }//end translate
    
    translate([0,-(backWallD)/2+10,pokeAreaH/3-noseHoleD/2]){ 
      rotate([90,0,0]){ 
      cylinder(d=noseHoleD,h=15);
      }// end rotate
     }// end translate
     
    translate([0,(noseHoleD)/2+screwD,-1]){
    rotate([90,0,0]){
        cylinder(d=screwD,h=10);
    }// end rotate
    }//end translate

    translate([0,-(noseHoleD)/2-screwD,-1]){
    rotate([90,0,0]){
    cylinder(d=screwD,h=10);
    }//end rotate
    }//end translate
    
}//end union
}//end difference
    }//end module

//backWall(); 
  //translate([0,-(backWallD)/2+10,pokeAreaH/2-noseHoleD/2]){ 
     //rotate([90,0,0]){ 
    //cylinder(d=noseHoleD+wallT,h=15);
    // }//end rotate
  //}//end translate
  
  nosePoke();
  //backWall() ;