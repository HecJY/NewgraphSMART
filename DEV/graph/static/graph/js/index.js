function Popularity(likes, retweets){

  //Assuming we are only look at the tweets that have more that 1000 likes or 500 retweets
  var like_log = math.log1000(likes)
  var retweets_log = math.log1000(retweets)
  //Also since it is harder to have re-tweets than likes, thus, the weight of retweets is higher than the weight of the likes
  var pop = like_log + power(retweets_log,1.5)
  return pop
} //This function returns the size of the bubbl on the graph.

var two_D = [
  [39600,5225],
  [3300,4170],
  [1500,4043],
  [17400,2647]
]

function chartmaker(two_D) {
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
			{ x: two_D[0][0], y: two_D[0][1], z: Popularity(two_D[0][0],two_D[0][1]), name:"Obama's tweets" },
			{ x: two_D[1][0], y: two_D[1][1], z: Popularity(two_D[1][0],two_D[1][1]), name:"Trump's tweets" },
			{ x: two_D[2][0], y: two_D[2][1], z: Popularity(two_D[2][0],two_D[2][1]), name:"ALy's tweets" },
			{ x: two_D[3][0], y: two_D[3][1], z: Popularity(two_D[3][0],two_D[3][1]), name:"Wang's tweets" },
		]
	}]
});
chart.render();
}
