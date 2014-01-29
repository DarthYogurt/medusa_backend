
function drawPieGraph() {

// Setup all the constants
var duration = 500;
var width = 850
var height = 500
var radius = Math.floor(Math.min(width/2, height/2) * 0.9);
var colors = ["#d62728", "#ff9900", "#004963", "#3497D3"];

var totalYes = 0,
	totalNo = 0;
	
for (i=0;i<logData.stepLog.length;i++){
	if (isNaN(logData.stepLog[i].yes) == false){
		totalYes += logData.stepLog[i].yes;
	}
	if (isNaN(logData.stepLog[i].no) == false){
		totalNo += logData.stepLog[i].no;
	}
}

var d1 = [ { label: 'Yes: ' +totalYes, value: 100 },
           { label: 'No: ' +totalNo, value: 0 }
           ];

var d2 = [ { label: 'Yes', value: totalYes},
		  	{ label: 'No', value: totalNo} ];




// Set the initial data
var data = d1

var updateChart = function(dataset) {
  arcs.data(donut(dataset))
      .enter()
      .append("path")
      .attr("stroke", "white")
      .attr("stroke-width", 0.8)
      .attr("fill", function(d, i) { return color(i); })
      .attr("d", arc);
  arcs.transition()
    .duration(duration)
    .attrTween("d", arcTween);
  sliceLabel.data(donut(dataset));
  sliceLabel.transition()
    .duration(duration)
    .attr("transform", function(d) { return "translate(" + (arc.centroid(d)) + ")"; })
    .style("fill-opacity", function(d) {
      if (d.value === 0) { return 1e-6; }
      else { return 1; }
    });
    
    sliceLabel.data(donut(dataset)).enter()
  .append("text")
  .attr("class", "arcLabel")
  .attr("transform", function(d) { return "translate(" + (arc.centroid(d)) + ")"; })
  .attr("text-anchor", "middle")
  .style("fill-opacity", function(d) {
    if (d.value === 0) { return 1e-6; }
    else { return 1; }
  })
  .text(function(d) { return d.data.label; });
};

var color = d3.scale.category20();
var donut = d3.layout.pie()
  .sort(null)
  .value(function(d) { return d.value; });
var arc = d3.svg.arc()
  .innerRadius(radius * .4)
  .outerRadius(radius);
var svg = d3.select("#pieGraph")
  .append("svg")
  .append("svg")
  .attr("width", width)
  .attr("height", height);

var arc_grp = svg.append("g")
  .attr("class", "arcGrp")
  .attr("transform", "translate(" + (width / 2) + "," + (height / 2) + ")");
var label_group = svg.append("g")
  .attr("class", "lblGroup")
  .attr("transform", "translate(" + (width / 2) + "," + (height / 2) + ")");

var arcs = arc_grp.selectAll("path")
  .data(donut(data));
arcs.enter()
  .append("path")
  .attr("stroke", "white")
  .attr("stroke-width", 0.8)
  .attr("fill", function(d, i) { return color(i); })
  .attr("d", arc)
  .each(function(d) { return this.current = d; });

var sliceLabel = label_group.selectAll("text")
  .data(donut(data));
sliceLabel.enter()
  .append("text")
  .attr("class", "arcLabel")
  .attr("transform", function(d) { return "translate(" + (arc.centroid(d)) + ")"; })
  .attr("text-anchor", "middle")
  .style("fill-opacity", function(d) {
    if (d.value === 0) { return 1e-6; }
    else { return 1; }
  })
  .text(function(d) { return d.data.label});


// Update the data
setInterval(function(model) {
  return updateChart(d2);
}, 500);

// Tween Function
var arcTween = function(a) {
  var i = d3.interpolate(this.current, a);
  this.current = i(0);
  return function(t) { return arc(i(t)); };
};
}