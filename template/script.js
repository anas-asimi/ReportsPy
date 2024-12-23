const ctx = document.getElementById("myChart");

const chart = new Chart(ctx, {
	type: "bar",
	data: {
		labels: ["Red", "Blue", "Yellow", "Green", "Purple", "Orange"],
		datasets: [
			{
				label: "# of Votes",
				data: [12, 19, 3, 5, 2, 3],
				borderWidth: 1,
			},
		],
	},
	options: {
		animation: {
			duration: 0,
		},
		devicePixelRatio: 2,
		aspectRatio: 3 / 2,
	},
});

chart.options.animation = false; // disables all animations
