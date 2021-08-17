//cylinder(10,10,25, $fn = 200);


module doorhole(){
 translate([]){   
 cylinder(50,50,10, $fn = 200);   
    
    
}}




module outerring(){
  translate(0,0,-2){
 cylinder(12,d=72,d=72, $fn = 200);   
    
    
}}




module outerring2(){
      translate(0,0,-2){

     cylinder(12,d=51,d=51, $fn = 200);   
}
}

difference(){
    outerring();
    outerring2();
        

}


module innerring1(){
   translate([0,0,10]){ 
 cylinder(5.5,d=51,d=51, $fn = 200);   
    
   }
}

module innerring2(){
   translate([0,0,10]){ 
 cylinder(10,d=44,d=44, $fn = 200);   
    
   }
}
difference(){
    innerring1();
    innerring2();
}