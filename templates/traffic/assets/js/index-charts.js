"use strict";
window.chartColors = {green: "#75c181", gray: "#a9b5c9", text: "#252930", border: "#e7e9ed"};
var randomDataPoint = function () {
    return Math.round(Math.random() * 10000)
};
var lineChartConfig = {
    type: "line",
    data: {
        labels: ["Day 1", "Day 2", "Day 3", "Day 4", "Day 5", "Day 6", "Day 7"],
        datasets: [{
            label: "Current week",
            fill: false,
            backgroundColor: window.chartColors.green,
            borderColor: window.chartColors.green,
            data: [randomDataPoint(), randomDataPoint(), randomDataPoint(), randomDataPoint(), randomDataPoint(), randomDataPoint(), randomDataPoint()],
        }, {
            label: "Previous week",
            borderDash: [3, 5],
            backgroundColor: window.chartColors.gray,
            borderColor: window.chartColors.gray,
            data: [randomDataPoint(), randomDataPoint(), randomDataPoint(), randomDataPoint(), randomDataPoint(), randomDataPoint(), randomDataPoint()],
            fill: false,
        }]
    },
    options: {
        responsive: true,
        aspectRatio: 1.5,
        legend: {display: true, position: "bottom", align: "end",},
        title: {display: true, text: "Chart.js Line Chart Example",},
        tooltips: {
            mode: "index",
            intersect: false,
            titleMarginBottom: 10,
            bodySpacing: 10,
            xPadding: 16,
            yPadding: 16,
            borderColor: window.chartColors.border,
            borderWidth: 1,
            backgroundColor: "#fff",
            bodyFontColor: window.chartColors.text,
            titleFontColor: window.chartColors.text,
            callbacks: {
                label: function (b, a) {
                    if (parseInt(b.value) >= 1000) {
                        return "$" + b.value.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",")
                    } else {
                        return "$" + b.value
                    }
                }
            },
        },
        hover: {mode: "nearest", intersect: true},
        scales: {
            xAxes: [{
                display: true,
                gridLines: {drawBorder: false, color: window.chartColors.border,},
                scaleLabel: {display: false,}
            }],
            yAxes: [{
                display: true,
                gridLines: {drawBorder: false, color: window.chartColors.border,},
                scaleLabel: {display: false,},
                ticks: {
                    beginAtZero: true, userCallback: function (b, a, c) {
                        return "$" + b.toLocaleString()
                    }
                },
            }]
        }
    }
};
var barChartConfig = {
    type: "bar",
    data: {
        labels: ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
        datasets: [{
            label: "Orders",
            backgroundColor: window.chartColors.green,
            borderColor: window.chartColors.green,
            borderWidth: 1,
            maxBarThickness: 16,
            data: [23, 45, 76, 75, 62, 37, 83]
        }]
    },
    options: {
        responsive: true,
        aspectRatio: 1.5,
        legend: {position: "bottom", align: "end",},
        title: {display: true, text: "Chart.js Bar Chart Example"},
        tooltips: {
            mode: "index",
            intersect: false,
            titleMarginBottom: 10,
            bodySpacing: 10,
            xPadding: 16,
            yPadding: 16,
            borderColor: window.chartColors.border,
            borderWidth: 1,
            backgroundColor: "#fff",
            bodyFontColor: window.chartColors.text,
            titleFontColor: window.chartColors.text,
        },
        scales: {
            xAxes: [{display: true, gridLines: {drawBorder: false, color: window.chartColors.border,},}],
            yAxes: [{display: true, gridLines: {drawBorder: false, color: window.chartColors.borders,},}]
        }
    }
};
window.addEventListener("load", function () {
    var b = document.getElementById("canvas-linechart").getContext("2d");
    window.myLine = new Chart(b, lineChartConfig);
    var a = document.getElementById("canvas-barchart").getContext("2d");
    window.myBar = new Chart(a, barChartConfig);
});