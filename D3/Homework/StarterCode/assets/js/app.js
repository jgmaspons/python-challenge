// Step 1: Set up our chart
//= ================================

// Define the area dimensions of the SVG container
var svgWidth = 960;
var svgHeight = 500;

// Define the chart's margin as an object
var margin = {
  top: 20,
  right: 40,
  bottom: 60,
  left: 50
};

// Define the dimensions of the chart area
var width = svgWidth - margin.left - margin.right;
var height = svgHeight - margin.top - margin.bottom;

// Create an SVG container by selecting the body, appending SVG area
//   to it, and setting its dimensions
var svg = d3
    .select("#scatter")
    .append("svg")
    .attr("width", svgWidth)
    .attr("height", svgHeight);

// Shifting everything by the margins
var chartGroup = svg.append("g")
    .attr("transform", `translate(${margin.left}, ${margin.top})`);


// Step 2: Scale the graph into proportions
//= ================================  

// Import the data
d3.csv("data.csv").then(function(healthData){

// Scaling the graph into proportions
var yLinearScale = d3.scaleLinear().range([height, 0]);
var xLinearScale = d3.scaleLinear().range([0, width]);

console.log(healthData);

// Setting variables to store max & min values
var xMin;
var xMax;
var yMin;
var yMax;

// console.log(yMin);
// console.log(yMax);
// console.log(xMin);
// console.log(xMax);

// Parse the data and format the data as numbers
healthData.forEach(function(data) {
    data.poverty = +data.poverty;
    data.healthcare = +data.healthcare; 

// Finding min and max for y-axis and x-axis

yMin = d3.min(healthData, d => d.healthcare);
yMax = d3.max(healthData, d => d.healthcare);

xMin = d3.min(healthData, d => d.poverty);
xMax = d3.max(healthData, d => d.poverty);

yLinearScale.domain([yMin * 0.85, yMax * 1.02]);
xLinearScale.domain([xMin * 0.98 , xMax * 1.04]);


});// END FOR EACH LOOP

// Step 3: Create the axies and display them
//= ================================  

// Creating axes 
var leftAxis = d3.axisLeft(yLinearScale);
var bottomAxis = d3.axisBottom(xLinearScale);

// Add y axis
chartGroup.append("g").call(leftAxis);

// Add x axis
chartGroup.append("g")
    .attr("transform", `translate(0, ${height})`)
    .call(bottomAxis);


// Step 4: Load data into graph
//= ================================  

// Create circles
var circlesGroup = chartGroup.selectAll("circle")
  .data(healthData)
  .enter()
  .append("circle")
  .attr("cx", d => xLinearScale(d.poverty))
  .attr("cy", d => yLinearScale(d.healthcare))
  .attr("r", "10")
  .attr("fill", "#0066cc")
  .attr("opacity", .5)

// Add labels to circles

chartGroup.append("text")
.style("font-size", "10px")
.selectAll("tspan")
.data(healthData)
.enter()
.append("tspan")
    .attr("x", function(data) {
        return xLinearScale(data.poverty -0.1);
    })
    .attr("y", function(data) {
        return yLinearScale(data.healthcare -0.1);
    })
    .text(function(data) {
        return data.abbr
    });

 // Add axis labels   

chartGroup.append("text")
  .attr("transform", "rotate(-90)")
  .attr("y", 0 - margin.left)
  .attr("x", 0 - (height / 1.5))
  .attr("dy", "1em")
  .attr("class", "axisText")
  .text("Lacks Healthcare (%)");

chartGroup.append("text")
  .attr("transform", `translate(${width / 2.25}, ${height = margin.top + 450})`)
  .attr("font-size", "16px")
  .attr("class", "axisText")
  .text("In Poverty (%)");

});