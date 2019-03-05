

function bubble_chart() {
var chart = new CanvasJS.Chart("chartContainer", {
animationEnabled: true,
zoomEnabled: true,
theme: "light2",
title:{
  text: "Sample bubble graph that will be presenting on the map"
},
axisX: {
  title:"The sum of likes and re-tweets",
  suffix: "k",
  minimum: 0, //We can log the number of re-tweets in the power of 10^3
  maximum: 61,
  gridThickness: 1
},
axisY:{
  title: "Popularity of the tweets",
  suffix: "none"
},
data: [{
  type: "bubble",
  toolTipContent: "<b>{name}</b><br/>The sum of likes and re-tweets {x}% <br/> Popularity rate <br/> Number of comments",
  dataPoints: [
    { x: 39.6, y: 5.225, z:1347, name:"Obama's tweets" },
    { x: 3.3, y: 4.17, z:21.49, name:"Trump's tweets" },
    { x: 1.5, y: 4.043, z:304.09, name:"ALy's tweets" },
    { x: 17.4, y: 2.647, z:2.64, name:"Wang's tweets" },
  ]
}]
});
chart.render();
}
