// from data.js
var tableData = data;

// add options for filter 
var city_opt = [];
var state_opt = [];
var country_opt = [];
var shape_opt = [];
tableData.forEach(item => {
	Object.entries(item).forEach(([key, value]) => {
		if (key == "city" && city_opt.indexOf(value) == -1 ) {
			city_opt.push(value);
		} else if (key == "state" && state_opt.indexOf(value) == -1 ) {
			state_opt.push(value);
		} else if (key == "country" && country_opt.indexOf(value) == -1 ) {
			country_opt.push(value);	
		} else if (key == "shape" && shape_opt.indexOf(value) == -1 ) {
			shape_opt.push(value);
		}
	});
});

city_opt.sort().forEach(x => d3.select("#city_filter").append("option").text(x));
state_opt.sort().forEach(x => d3.select("#state_filter").append("option").text(x));
country_opt.sort().forEach(x => d3.select("#country_filter").append("option").text(x));
shape_opt.sort().forEach(x => d3.select("#shape_filter").append("option").text(x));

// function to append data to table 
function renderTable(data) {
	var tbody = d3.select("tbody");
	tbody.html("");
	data.forEach(item => {
		var row = tbody.append("tr");
		Object.entries(item).forEach(([key, value]) => {
			var cell = row.append("td");
			cell.text(value);
		});
	});
}

renderTable(tableData);

// add filter to filter data
var submit = d3.select("#filter-btn");
submit.on("click", function() {
	d3.event.preventDefault();

	var filteredData = tableData;
	var datetime = d3.select("#datetime").property("value");
	if (datetime) {
		var filteredData = filteredData.filter(ufo => ufo.datetime === datetime);
	}
	
	var city = d3.select("#city_filter").node().value;
	if (city != "None") {
		var filteredData = filteredData.filter(ufo => ufo.city === city);
	}

	var state = d3.select("#state_filter").node().value;
	if (state != "None") {
		var filteredData = filteredData.filter(ufo => ufo.state === state);
	}

	var country = d3.select("#country_filter").node().value;
	if (country != "None") {
		var filteredData = filteredData.filter(ufo => ufo.country === country);
	}

	var shape = d3.select("#shape_filter").node().value;
	if (shape != "None") {
		var filteredData = filteredData.filter(ufo => ufo.shape === shape);
	}
	
	renderTable(filteredData);
});


