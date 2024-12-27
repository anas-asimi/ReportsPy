const JSON_URL = "./assets/data.json";
const devicePixelRatio = 2;
const CHART_COLORS = {
	red: "rgb(255, 99, 132)",
	orange: "rgb(255, 159, 64)",
	yellow: "rgb(255, 205, 86)",
	green: "rgb(75, 192, 192)",
	blue: "rgb(54, 162, 235)",
	purple: "rgb(153, 102, 255)",
	grey: "rgb(201, 203, 207)",
};

// ================ Main func ================
async function main() {
	// Fetching data
	let data = await fetchJson(JSON_URL);
	console.log(data);

	// ================ the tables ================
	// Temperature daily table
	const allMin = {
		count: 0,
		sum: 0,
	};
	const allMax = {
		count: 0,
		sum: 0,
	};
	const allMoy = {
		count: 0,
		sum: 0,
	};
	const tableBody = document.querySelector("#table-1 tbody");
	for (const zone in data) {
		const stationsCount = data[zone].length;
		let count = 0;
		for (const station of data[zone]) {
			const stationName = station.name;
			const lastRecord = station.records[station.records.length - 1];
			const Tmin = parseFloat(lastRecord.Temperature_Min).toFixed(2);
			allMin.sum += parseFloat(Tmin);
			allMin.count++;
			const Tmax = parseFloat(lastRecord.Temperature_Max).toFixed(2);
			allMax.sum += parseFloat(Tmax);
			allMax.count++;
			const Tmoy = parseFloat(lastRecord.Temperature).toFixed(2);
			allMoy.sum += parseFloat(Tmoy);
			allMoy.count++;

			let tableRow = `
				<td>${stationName}</td>
				<td>${Tmin}</td>
				<td>${Tmax}</td>
				<td>${Tmoy}</td>
			`;
			// if the first row in a zone add zone field
			if (count == 0)
				tableRow =
					`<td rowspan="${stationsCount}">${zone}</td>` + tableRow;
			// add to tbody element
			tableBody.innerHTML += `<tr>${tableRow}</tr>`;
			count++;
		}
	}
	console.log(allMin, allMax, allMoy);
	const moyMin = document.getElementById("moy-min");
	moyMin.textContent = parseFloat(allMin.sum / allMin.count).toFixed(2);
	const moyMax = document.getElementById("moy-max");
	moyMax.textContent = parseFloat(allMax.sum / allMax.count).toFixed(2);
	const moyMoy = document.getElementById("moy-moy");
	moyMoy.textContent = parseFloat(allMoy.sum / allMin.count).toFixed(2);

	// ================ the charts ================
	// Temperature daily chart
	const ctx = document.getElementById("chart-temp-chart");
	const chartData = {
		labels: [
			"00",
			"02",
			"04",
			"06",
			"08",
			"10",
			"12",
			"14",
			"16",
			"18",
			"20",
			"22",
			"24",
		],
		datasets: [
			{
				label: "st 1",
				data: [30, 16, 5, 21, 12, 18, 24, 12, 13, 15, 17, 23, 19],
				fill: false,
				borderColor: CHART_COLORS.blue,
				tension: 0.4,
			},
			{
				label: "st 2",
				data: [12, 20, 16, 30, 24, 30, 17, 22, 12, 9, 8, 29, 5],
				fill: false,
				borderColor: CHART_COLORS.red,
				tension: 0.4,
			},
		],
	};
	const chart = new Chart(ctx, {
		type: "line",
		data: chartData,
		options: {
			plugins: {
				legend: {
					position: "top",
				},
			},
			animation: {
				duration: 0,
			},
			devicePixelRatio,
			aspectRatio: 2,
			scales: {
				x: {
					title: {
						text: "Hours",
						display: true,
					},
				},
				y: {
					title: {
						text: "°C",
						display: true,
					},
				},
			},
		},
	});
	chart.options.animation = false; // disable the animation
}

main();

// ================ Other funcs ================

async function fetchJson(url) {
	try {
		const response = await fetch(JSON_URL);
		if (!response.ok) {
			throw new Error(`HTTP error! status: ${response.status}`);
		}
		return await response.json();
	} catch (error) {
		console.error("Error fetching JSON data:", error);
	}
}
