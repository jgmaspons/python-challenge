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
var chartWidth = svgWidth - margin.left - margin.right;
var chartHeight = svgHeight - margin.top - margin.bottom;

// Create an SVG container by selecting the body, appending SVG area
//   to it, and setting its dimensions
var svg = d3.select("body").append("svg")
  .attr("width", svgWidth)
  .attr("height", svgHeight);