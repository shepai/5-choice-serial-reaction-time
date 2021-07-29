Smoothness = 360;
tol = 0.1;
Walls = 2;


x_Box = 145;
y_Box = 195;
z_Box = 20+Walls;


tray = 1;

module tray(){
difference(){
    translate([-x_Box/2,-y_Box/2,0])cube([x_Box, y_Box, z_Box]);
    
    translate([-x_Box/2+Walls,-y_Box/2+Walls,Walls])cube([x_Box-2*Walls, y_Box-2*Walls, z_Box]);
}
}


if (tray == 1){tray();}
