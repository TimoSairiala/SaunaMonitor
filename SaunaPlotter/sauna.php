<?php   


 /* pChart library inclusions */
 include("../class/pData.class.php");
 include("../class/pDraw.class.php");
 include("../class/pImage.class.php");

$mysql_query_measurements = "select heat, humidity, time from mittaukset WHERE time >= DATE_SUB( NOW(), INTERVAL 1 DAY);";
$mysqli = new mysqli( "dbhost", "dbuser", "dbpwd", "sauna" );
if ($mysqli->connect_errno) {
    echo "Failed to connect to MySQL: (" . $mysqli->connect_errno . ") " . $mysqli->connect_error;
}

$res = $mysqli->query( $mysql_query_measurements );

while( $row = $res->fetch_assoc( ) ) {
        $temperature[] = $row["heat"];
        $humidity[] = $row["humidity"];
        $timestamp[] = $row["time"];
}

 /* Create and populate the pData object */
 $MyData = new pData();  
 $MyData->addPoints($temperature, "DEFCA");
 $MyData->setAxisName(0,"lämpöö");
 $MyData->setAxisDisplay(0,AXIS_FORMAT_CURRENCY);
// $MyData->addPoints(array("Jan","Feb","Mar","Apr","May","Jun","Jul","Aou","Sep","Oct","Nov","Dec"),"Labels");
 $MyData->setSerieDescription("Labels","Months");
 $MyData->setAbscissa("Labels");
 $MyData->setPalette("DEFCA",array("R"=>55,"G"=>91,"B"=>127));

 /* Create the pChart object */
 $myPicture = new pImage(700,230,$MyData);
 $myPicture->drawGradientArea(0,0,700,230,DIRECTION_VERTICAL,array("StartR"=>220,"StartG"=>220,"StartB"=>220,"EndR"=>255,"EndG"=>255,"EndB"=>255,"Alpha"=>100));
 $myPicture->drawRectangle(0,0,699,229,array("R"=>200,"G"=>200,"B"=>200));
 
 /* Write the picture title */ 
 $myPicture->setFontProperties(array("FontName"=>"../fonts/Forgotte.ttf","FontSize"=>11));
 $myPicture->drawText(60,35,"Saunatontun mittaukset",array("FontSize"=>20,"Align"=>TEXT_ALIGN_BOTTOMLEFT));

 /* Do some cosmetic and draw the chart */
 $myPicture->setGraphArea(60,40,670,190);
 $myPicture->drawFilledRectangle(60,40,670,190,array("R"=>255,"G"=>255,"B"=>255,"Surrounding"=>-200,"Alpha"=>10));
 $myPicture->drawScale(array("GridR"=>180,"GridG"=>180,"GridB"=>180));

 /* Draw a spline chart on top */
 $myPicture->setFontProperties(array("FontName"=>"../fonts/pf_arma_five.ttf","FontSize"=>6));
 $myPicture->drawFilledSplineChart();

 $myPicture->setShadow(TRUE,array("X"=>2,"Y"=>2,"R"=>0,"G"=>0,"B"=>0,"Alpha"=>10));
 $myPicture->drawSplineChart();
 $myPicture->setShadow(FALSE);

 /* Write the chart legend */ 
 $myPicture->drawLegend(643,210,array("Style"=>LEGEND_NOBORDER,"Mode"=>LEGEND_HORIZONTAL));

 /* Render the picture (choose the best way) */
 $myPicture->autoOutput("pictures/example.drawSimple.png");
?>
