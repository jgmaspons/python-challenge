// Assign the data from data.js to a descriptive variable 
var tableData = data;

// Select the submit button
var submit = d3.select("#filter-btn"); 

submit.on("click", function() {

    // Prevent the page from refreshing
    d3.event.preventDefault();

    // Select the input element and get the raw HTML node
    var inputElement = d3.select("#datetime");

    // Get the value property of the input element
    var inputValue = inputElement.property("value");

    //console.log(inputValue);  
    //console.log(tableData); 

// Filter data based on submitted date
    var filteredData = tableData.filter(UFOs => UFOs.datetime === inputValue);

    console.log(filteredData);

// Get a reference to the table body
    var tbody = d3.select("tbody");

// // Step 1: Loop Through `data` and console.log each UFO sighting object
    filteredData.forEach(function(UFOReport) {
    console.log(UFOReport);
});

// // Step 2:  Use d3 to append one table row `tr` for each UFO sighting object
// // Don't worry about adding cells or text yet, just try appending the `tr` elements.
    filteredData.forEach(function(UFOReport) {
    console.log(UFOReport);
    var row = tbody.append("tr");
});
     

// // Step 3:  Use `Object.entries` to console.log each UFO sighting value
    filteredData.forEach(function(UFOReport) {
    console.log(UFOReport);
    var row = tbody.append("tr");
 
    Object.entries(UFOReport).forEach(function([key, value]) {
      console.log(key, value);
    });
  });
// // Step 4: Use d3 to append 1 cell per UFO sighting value 
filteredData.forEach(function(UFOReport) {
    console.log(UFOReport);
    var row = tbody.append("tr");
 
    Object.entries(UFOReport).forEach(function([key, value]) {
      console.log(key, value);
      // Append a cell to the row for each value
 //     // in the UFO sighting object
      var cell = tbody.append("td");
    });
  });
// // Step 5: Use d3 to update each cell's text with
// // UFO sighting values (weekday, date, high, low)
    filteredData.forEach(function(UFOReport) {
    console.log(UFOReport);
    var row = tbody.append("tr");
    Object.entries(UFOReport).forEach(function([key, value]) {
      console.log(key, value);
 //     // Append a cell to the row for each value
 //     // in the UFO sighting object
      var cell = tbody.append("td");
      cell.text(value);
    });
  });


});