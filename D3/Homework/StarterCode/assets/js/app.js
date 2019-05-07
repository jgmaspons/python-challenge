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
d3.csv("data.csv").then(data =>{
      

// Print the data    
    //console.log(data);

// Parse the data and format the data as numbers
data.forEach(function(data) {
    data.poverty = +data.poverty;
    data.healthcare = +data.healthcare;  
 
});  
    console.log(data);

// Scaling the graph into proportions

var yLinearScale = d3.scaleLinear().range([height, 0]);
var xLinearScale = d3.scaleLinear().range([0, width]);

// Setting variables to store max & min values
var xMin;
var xMax;
var yMin;
var yMax;

// Finding min and max for y-axis and x-axis

yMin = d3.min(data, d => d.healthcare);
yMax = d3.max(data, d => d.healthcare);

xMin = d3.min(data, d => d.poverty);
xMax = d3.max(data, d => d.poverty);

yLinearScale.domain([yMin, yMax*1.1]);
xLinearScale.domain([xMin, xMax*1.05]);

console.log(yMin);
console.log(yMax);
console.log(xMin);
console.log(xMax);

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

});

